#!/usr/bin/env python3
"""Validate one Agent Skill package without relying on repository context."""

from __future__ import annotations

import argparse
import codecs
import glob as globlib
import re
import shlex
import stat
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_FIELD_RE = re.compile(r"(?m)^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*?)\s*$")
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
QUOTED_VALUE_RE = re.compile(r"""["']([^"'\r\n]+)["']""")
SKILL_TOKEN_RE = re.compile(r"\$([a-z][a-z0-9-]*)", re.IGNORECASE)
BACKTICK_NAME_RE = re.compile(r"^([a-z][a-z0-9-]*)$", re.IGNORECASE)
SKILL_ACTION_RE = re.compile(
    r"\b(?:use|invoke|load|consult|apply|require|delegate(?:\s+to)?|"
    r"route(?:\s+to)?|hand\s+off(?:\s+to)?|return(?:[^.\n]{0,30}\s+to)?)\b",
    re.IGNORECASE,
)
NEGATION_RE = re.compile(
    r"\b(?:never|cannot|can't|do\s+not|don't|must\s+not|without|forbid(?:s|den)?)\b",
    re.IGNORECASE,
)
RESOURCE_ACTION_RE = re.compile(
    r"\b(?:read|load|open|run|execute|source|follow|consult|import|include|apply)\b",
    re.IGNORECASE,
)
TARGET_ARTIFACT_RE = re.compile(
    r"\b(?:target|subject|input|user-provided|artifact|under review)\b",
    re.IGNORECASE,
)
REMOTE_URL_RE = re.compile(
    r"\b(?:ftp|git|https?|ssh)://[^\s)`>\]]+",
    re.IGNORECASE,
)
SCP_REMOTE_RE = re.compile(
    r"(?<![\w.-])[\w.-]+@[\w.-]+:[^\s)`>\]]+",
    re.IGNORECASE,
)
REQUIRED_NETWORK_RE = re.compile(
    r"\b(?:required|must|before|fetch|download|clone|install|read|load|"
    r"consult|follow|source|execute|run)\b",
    re.IGNORECASE,
)
OPTIONAL_NETWORK_RE = re.compile(
    r"\b(?:attribution only|historical background|not required|optional|"
    r"supplemental|citation only)\b",
    re.IGNORECASE,
)
NETWORK_COMMAND_RE = re.compile(
    r"\b(?:curl|wget|git\s+clone|npx|bunx|"
    r"(?:python\d*(?:\s+-m)?\s+)?pip\d*\s+install|"
    r"(?:npm|pnpm|yarn)\s+(?:add|install))\b",
    re.IGNORECASE,
)
ATTRIBUTION_RE = re.compile(
    r"\b(?:attribution|not required|influence|inspired|credit|"
    r"acknowledg|bibliograph|citation)\b",
    re.IGNORECASE,
)
STRUCTURED_PATH_RE = re.compile(
    r"""^\s*["']?(?:asset|file|href|import|include|instructions|path|"""
    r"""reference|script|source|src|template)["']?\s*:\s*(.+?)\s*,?\s*$""",
    re.IGNORECASE,
)
HTML_RESOURCE_RE = re.compile(
    r"""\b(?:href|src|xlink:href)\s*=\s*["']([^"']+)["']""",
    re.IGNORECASE,
)
CSS_RESOURCE_RE = re.compile(
    r"""(?:url\(\s*["']?([^"')]+)|@import\s+["']([^"']+))""",
    re.IGNORECASE,
)
SHELL_SOURCE_RE = re.compile(
    r"""^\s*(?:source|\.)\s+["']?([^"' \t;&|]+)""",
    re.IGNORECASE,
)
WINDOWS_ABSOLUTE_RE = re.compile(r"^[a-zA-Z]:[\\/]")
INTERPRETERS = {
    "bash",
    "node",
    "perl",
    "php",
    "pwsh",
    "python",
    "python3",
    "ruby",
    "sh",
    "source",
}
STATUS_TOKENS = {
    "block",
    "needs-human-decision",
    "no-op",
    "pass",
    "unvalidated",
}
TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".rb",
    ".sh",
    ".svg",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
SCRIPT_SUFFIXES = {".js", ".mjs", ".ps1", ".py", ".rb", ".sh", ".ts"}
PATH_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".rb",
    ".sh",
    ".svg",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
ATTRIBUTION_HEADINGS = {
    "acknowledgements",
    "attribution",
    "credits",
    "influences",
    "license",
    "sources",
}
W3_NAMESPACE_PREFIX = "http" + ":" + "/" + "/" + "www.w3.org/"
SCHEME_SEPARATOR = ":" + "/" + "/"


def decode_text(path: Path) -> tuple[str | None, str | None]:
    try:
        data = path.read_bytes()
    except OSError as error:
        return None, f"cannot read file: {error}"

    try:
        if data.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
            return data.decode("utf-16"), None
        return data.decode("utf-8-sig"), None
    except UnicodeDecodeError:
        mode = path.stat().st_mode
        must_be_text = (
            path.name == "SKILL.md"
            or path.suffix.lower() in TEXT_SUFFIXES
            or bool(mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
        )
        if must_be_text:
            return None, "runtime or executable text is not UTF-8/UTF-16"
        return None, None


def parse_frontmatter(skill_file: Path) -> tuple[str | None, str | None]:
    text, error = decode_text(skill_file)
    if error or text is None:
        return None, None
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, None
    try:
        boundary = lines[1:].index("---") + 1
    except ValueError:
        return None, None

    frontmatter = "\n".join(lines[1:boundary])
    fields = {
        match.group(1): match.group(2)
        for match in FRONTMATTER_FIELD_RE.finditer(frontmatter)
    }
    name = fields.get("name")
    description = fields.get("description")
    if name:
        name = name.strip("\"'")
    if description:
        description = description.strip("\"'")
    if description in {"", ">", "|", ">-", "|-"}:
        start = next(
            (
                index
                for index, line in enumerate(frontmatter.splitlines())
                if line.startswith("description:")
            ),
            -1,
        )
        block: list[str] = []
        for line in frontmatter.splitlines()[start + 1 :]:
            if line and not line[0].isspace():
                break
            block.append(line.strip())
        description = " ".join(part for part in block if part)
    return name, description


def without_fenced_code(text: str) -> str:
    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        marker = stripped[:3]
        if fence is None and marker in {"```", "~~~"}:
            fence = marker
            output.append("\n" if line.endswith("\n") else "")
        elif fence is not None and stripped.startswith(fence):
            fence = None
            output.append("\n" if line.endswith("\n") else "")
        elif fence is None:
            output.append(line)
        else:
            output.append("\n" if line.endswith("\n") else "")
    return "".join(output)


def without_inline_code(text: str) -> str:
    output = list(text)
    index = 0
    while index < len(text):
        if text[index] != "`":
            index += 1
            continue
        run_end = index
        while run_end < len(text) and text[run_end] == "`":
            run_end += 1
        marker = text[index:run_end]
        close = text.find(marker, run_end)
        if close == -1 or "\n" in text[run_end:close]:
            index = run_end
            continue
        for position in range(index, close + len(marker)):
            output[position] = " "
        index = close + len(marker)
    return "".join(output)


def markdown_destinations(text: str) -> list[str]:
    """Return inline and reference destinations while ignoring code and footnotes."""
    text = without_inline_code(without_fenced_code(text))
    destinations: list[str] = []
    index = 0

    while index < len(text):
        if text[index] != "[" or (index and text[index - 1] == "\\"):
            index += 1
            continue
        close = index + 1
        while close < len(text):
            if text[close] == "]" and text[close - 1] != "\\":
                break
            close += 1
        if close >= len(text):
            break
        cursor = close + 1
        if cursor < len(text) and text[cursor] == "(":
            depth = 1
            cursor += 1
            start = cursor
            while cursor < len(text) and depth:
                if text[cursor] == "\\":
                    cursor += 2
                    continue
                if text[cursor] == "(":
                    depth += 1
                elif text[cursor] == ")":
                    depth -= 1
                    if depth == 0:
                        destinations.append(text[start:cursor].strip())
                        break
                cursor += 1
            index = max(cursor + 1, close + 1)
        else:
            index = close + 1

    for line in text.splitlines():
        match = re.match(r"^\s*\[([^\]]+)\]:\s*(.+?)\s*$", line)
        if not match or match.group(1).startswith("^"):
            continue
        destinations.append(match.group(2))
    return destinations


def local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    if not target or target.startswith("#"):
        return None
    scheme = urlsplit(target).scheme.lower()
    if scheme:
        return None
    return unquote(target.split("#", 1)[0])


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def is_negated(line: str, action_start: int) -> bool:
    clause_start = max(
        line.rfind(".", 0, action_start),
        line.rfind(";", 0, action_start),
        line.rfind(":", 0, action_start),
    )
    return bool(NEGATION_RE.search(line[clause_start + 1 : action_start]))


def skill_dependency_errors(
    text: str,
    relative: Path,
    own_name: str | None,
    known_names: set[str],
) -> list[str]:
    errors: list[str] = []
    own = own_name.casefold() if own_name else ""
    known = {name.casefold() for name in known_names if name.casefold() != own}
    prose = without_fenced_code(text) if relative.suffix.lower() == ".md" else text
    full_lines = text.splitlines()
    prose_lines = prose.splitlines()

    for line_number, full_line in enumerate(full_lines, start=1):
        prose_line = prose_lines[line_number - 1] if line_number <= len(prose_lines) else ""
        full_clauses = re.split(r";", full_line)
        prose_clauses = re.split(r";", prose_line)

        for clause_index, clause in enumerate(full_clauses):
            prose_clause = (
                prose_clauses[clause_index]
                if clause_index < len(prose_clauses)
                else ""
            )

            for token_match in SKILL_TOKEN_RE.finditer(prose_clause):
                token = token_match.group(1).casefold()
                if token == own or token in STATUS_TOKENS:
                    continue
                if is_negated(prose_clause, token_match.start()):
                    continue
                prerequisite = re.search(
                    r"\b(?:prerequisite|required|approval)\b",
                    prose_clause[: token_match.start()],
                    re.IGNORECASE,
                )
                if "-" in token or token in known or prerequisite:
                    errors.append(
                        f"{relative}:{line_number}: invokes external skill "
                        f"${token_match.group(1)}"
                    )

            for action in SKILL_ACTION_RE.finditer(clause):
                if is_negated(clause, action.start()):
                    continue
                tail = clause[action.end() : action.end() + 140]
                action_word = action.group(0).casefold()
                if action_word == "use" and re.match(
                    r"\s+when\b", tail, re.IGNORECASE
                ):
                    continue

                token_match = SKILL_TOKEN_RE.search(tail)
                if token_match:
                    token = token_match.group(1).casefold()
                    if token != own and token not in STATUS_TOKENS:
                        errors.append(
                            f"{relative}:{line_number}: invokes external skill "
                            f"${token_match.group(1)}"
                        )
                        continue

                code_names = [
                    match.group(1)
                    for span in CODE_SPAN_RE.findall(tail)
                    if (match := BACKTICK_NAME_RE.fullmatch(span))
                ]
                external_code_names = [
                    value
                    for value in code_names
                    if value.casefold() != own
                    and value.casefold() not in STATUS_TOKENS
                    and ("-" in value or value.casefold() in known)
                ]
                if external_code_names:
                    errors.append(
                        f"{relative}:{line_number}: requires external workflow "
                        f"{external_code_names[0]!r}"
                    )
                    continue

                plain_external = next(
                    (
                        name
                        for name in known
                        if re.search(
                            rf"(?<![a-z0-9-]){re.escape(name)}(?![a-z0-9-])",
                            tail,
                            re.IGNORECASE,
                        )
                    ),
                    None,
                )
                if plain_external:
                    errors.append(
                        f"{relative}:{line_number}: requires sibling skill "
                        f"{plain_external!r}"
                    )
                    continue

                strong_action = re.match(r"(?:consult|invoke|load)", action_word)
                hyphenated = re.search(
                    r"^\s+(?:the\s+)?"
                    r"([a-z][a-z0-9]+(?:-[a-z0-9]+)+)(?![a-z0-9-])",
                    without_inline_code(tail),
                    re.IGNORECASE,
                )
                if strong_action and hyphenated:
                    errors.append(
                        f"{relative}:{line_number}: requires external workflow "
                        f"{hyphenated.group(1)!r}"
                    )
                    continue

                if re.search(
                    r"\b(?:this|target|own|current)\s+skill\b", tail, re.I
                ):
                    continue
                if re.search(
                    r"\b(?:another|external|separate|discovered)\b"
                    r"[^\n.]{0,80}\bskill\b",
                    tail,
                    re.I,
                ):
                    errors.append(
                        f"{relative}:{line_number}: routes to an external skill"
                    )
    return errors


def path_like(value: str) -> bool:
    clean = value.split("#", 1)[0].strip(",;:()[]{}")
    if not clean or clean in {".", "/"}:
        return False
    if clean in {"..", "AGENTS.md", "SKILL.md"}:
        return True
    if clean.startswith(("./", "../", "/", ".\\", "..\\")):
        return True
    if WINDOWS_ABSOLUTE_RE.match(clean):
        return True
    if "/" in clean or "\\" in clean:
        return (
            clean.casefold() == clean
            or clean.endswith(("/", "\\"))
            or "$" in clean
            or globlib.has_magic(clean)
        )
    return Path(clean).suffix.lower() in PATH_SUFFIXES


def path_candidates(snippet: str) -> set[str]:
    candidates = {
        match.group(1)
        for match in QUOTED_VALUE_RE.finditer(snippet)
        if path_like(match.group(1))
    }
    try:
        tokens = shlex.split(snippet)
    except ValueError:
        tokens = snippet.split()
    for token in tokens:
        clean = token.lstrip("`\"',;:()[]{}").rstrip("`\"',;:()[]{}.")
        if token.strip() == "..":
            clean = ".."
        if "](" in clean or SCHEME_SEPARATOR in clean:
            continue
        if path_like(clean):
            candidates.add(clean)
    return candidates


def check_required_path(
    candidate: str,
    source: Path,
    root: Path,
) -> str | None:
    candidate = candidate.split("#", 1)[0].strip()
    if not candidate or candidate.startswith("<"):
        return None
    if (
        candidate.startswith("data:")
        or REMOTE_URL_RE.match(candidate)
        or SCP_REMOTE_RE.match(candidate)
    ):
        return None
    if "$" in candidate or re.search(r"%[A-Za-z_][A-Za-z0-9_]*%", candidate):
        return f"variable-dependent path is not bundled: {candidate!r}"
    portable_candidate = candidate.replace("\\", "/")
    if WINDOWS_ABSOLUTE_RE.match(candidate) or Path(portable_candidate).is_absolute():
        return f"absolute local path dependency {candidate!r}"

    bases = (source.parent, root)
    if globlib.has_magic(portable_candidate):
        matches = [
            Path(match).resolve()
            for base in bases
            for match in globlib.glob(str(base / portable_candidate))
        ]
        if matches and all(is_within(match, root) for match in matches):
            return None
        if any(not is_within(match, root) for match in matches):
            return f"path glob escapes package {candidate!r}"
        return f"required local resource glob has no bundled matches: {candidate!r}"

    resolved_candidates = [
        (base / portable_candidate).resolve() for base in bases
    ]
    for resolved in resolved_candidates:
        if is_within(resolved, root) and resolved.exists():
            return None
    if any(not is_within(resolved, root) for resolved in resolved_candidates):
        return f"path escapes package {candidate!r}"
    return f"required local resource is not bundled: {candidate!r}"


def resource_path_errors(text: str, path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(root)
    instruction_file = (
        path.name == "SKILL.md"
        or path.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".json"}
    )

    def record(line_number: int, candidates: set[str]) -> None:
        for candidate in candidates:
            failure = check_required_path(candidate, path, root)
            if failure:
                errors.append(f"{relative}:{line_number}: {failure}")

    if instruction_file:
        for line_number, line in enumerate(text.splitlines(), start=1):
            spans = CODE_SPAN_RE.findall(line)
            action = RESOURCE_ACTION_RE.search(line)
            target_artifact = TARGET_ARTIFACT_RE.search(line)
            structured = STRUCTURED_PATH_RE.match(line)

            if action and not target_artifact:
                record(line_number, path_candidates(line))

            if structured:
                record(line_number, path_candidates(structured.group(1)))

            if path.suffix.lower() in {".json", ".yaml", ".yml"}:
                record(line_number, path_candidates(line))

            for span in spans:
                try:
                    tokens = shlex.split(span)
                except ValueError:
                    tokens = []
                is_command = bool(
                    tokens and Path(tokens[0]).name in INTERPRETERS
                )
                if is_command:
                    record(line_number, path_candidates(span))

        in_fence = False
        fence = ""
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.lstrip()
            if not in_fence and stripped[:3] in {"```", "~~~"}:
                in_fence = True
                fence = stripped[:3]
                continue
            if in_fence and stripped.startswith(fence):
                in_fence = False
                continue
            if not in_fence:
                continue
            try:
                tokens = shlex.split(stripped.lstrip("$> "))
            except ValueError:
                continue
            if not tokens or Path(tokens[0]).name not in INTERPRETERS:
                continue
            record(line_number, path_candidates(" ".join(tokens[1:])))

    if path.suffix.lower() in {".html", ".svg", ".xml"}:
        for line_number, line in enumerate(text.splitlines(), start=1):
            candidates = {
                match.group(1)
                for match in HTML_RESOURCE_RE.finditer(line)
                if path_like(match.group(1))
            }
            record(line_number, candidates)

    if path.suffix.lower() == ".css":
        for line_number, line in enumerate(text.splitlines(), start=1):
            candidates = {
                candidate
                for match in CSS_RESOURCE_RE.finditer(line)
                for candidate in match.groups()
                if candidate and path_like(candidate)
            }
            record(line_number, candidates)

    if path.suffix.lower() in SCRIPT_SUFFIXES:
        for line_number, line in enumerate(text.splitlines(), start=1):
            shell_source = SHELL_SOURCE_RE.match(line)
            if shell_source:
                record(line_number, {shell_source.group(1)})

            try:
                command_tokens = shlex.split(line.lstrip())
            except ValueError:
                command_tokens = []
            if command_tokens and Path(command_tokens[0]).name in INTERPRETERS:
                record(line_number, path_candidates(" ".join(command_tokens[1:])))

            for candidate in path_candidates(line):
                if not (
                    candidate == ".."
                    or candidate.startswith(("../", "..\\", "/"))
                    or WINDOWS_ABSOLUTE_RE.match(candidate)
                ):
                    continue
                failure = check_required_path(candidate, path, root)
                if failure:
                    errors.append(f"{relative}:{line_number}: {failure}")
    return errors


def attribution_context(line: str, heading: str) -> bool:
    normalized_heading = re.sub(r"[^a-z ]", "", heading.casefold()).strip()
    return (
        normalized_heading in ATTRIBUTION_HEADINGS
        or bool(ATTRIBUTION_RE.search(line))
    )


def network_errors(
    text: str,
    relative: Path,
    runtime_files: set[Path],
) -> list[str]:
    errors: list[str] = []
    heading = ""
    for line_number, line in enumerate(text.splitlines(), start=1):
        heading_match = re.match(r"^\s*#{1,6}\s+(.+?)\s*$", line)
        if heading_match:
            heading = heading_match.group(1)
        runtime = relative in runtime_files
        network_reference = bool(
            REMOTE_URL_RE.search(line) or SCP_REMOTE_RE.search(line)
        )
        command_surface = (
            relative.name == "SKILL.md"
            or relative.suffix.lower()
            in {".md", ".ps1", ".sh", ".txt", ".yaml", ".yml"}
        )
        network_command = bool(
            runtime and command_surface and NETWORK_COMMAND_RE.search(line)
        )
        if not (network_reference or network_command):
            continue
        svg_namespace = (
            relative.suffix.lower() == ".svg"
            and "xmlns" in line
            and W3_NAMESPACE_PREFIX in line
        )
        schema_identifier = (
            relative.suffix.lower() in {".json", ".yaml", ".yml"}
            and re.search(r"""["']?\$schema["']?\s*:""", line)
        )
        if (svg_namespace or schema_identifier) and not network_command:
            continue
        required = bool(REQUIRED_NETWORK_RE.search(line))
        optional = bool(OPTIONAL_NETWORK_RE.search(line))
        if required and not optional:
            errors.append(
                f"{relative}:{line_number}: required network dependency"
            )
            continue
        if optional or attribution_context(line, heading):
            continue
        top_level_readme = len(relative.parts) == 1 and relative.name == "README.md"
        if runtime or required or not top_level_readme:
            errors.append(
                f"{relative}:{line_number}: network resource is not "
                "supplemental attribution"
            )
    return errors


def validate_skill(skill_root: Path, known_names: set[str]) -> list[str]:
    errors: list[str] = []
    if skill_root.is_symlink():
        return [f"{skill_root}: package root must not be a symlink"]
    root = skill_root.resolve()
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_root}: missing SKILL.md"]

    name, description = parse_frontmatter(skill_file)
    if not name or not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid or missing frontmatter name")
    elif name != skill_root.name:
        errors.append(f"{skill_file}: name {name!r} does not match directory")
    if not description:
        errors.append(f"{skill_file}: missing frontmatter description")
    elif len(description) > 1024:
        errors.append(f"{skill_file}: description exceeds 1024 characters")

    texts: dict[Path, str] = {}
    local_links: dict[Path, list[Path]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"{skill_root}/{relative}: symlinks are forbidden")
            continue
        if not path.is_file():
            continue
        if (
            "__pycache__" in relative.parts
            or path.suffix.lower() in {".pyc", ".pyo"}
            or path.name == ".DS_Store"
        ):
            errors.append(f"{skill_root}/{relative}: generated artifact is forbidden")
            continue
        text, text_error = decode_text(path)
        if text_error:
            errors.append(f"{skill_root}/{relative}: {text_error}")
            continue
        if text is None:
            continue
        texts[relative] = text

        if path.suffix.lower() != ".md" and path.name != "SKILL.md":
            continue
        for raw_target in markdown_destinations(text):
            target = local_link_target(raw_target)
            if target is None:
                continue
            if WINDOWS_ABSOLUTE_RE.match(target) or Path(target).is_absolute():
                errors.append(
                    f"{skill_root}/{relative}: absolute local link {target!r}"
                )
                continue
            resolved = (path.parent / target).resolve()
            if not is_within(resolved, root):
                errors.append(
                    f"{skill_root}/{relative}: link escapes package: {target!r}"
                )
            elif not resolved.exists():
                errors.append(
                    f"{skill_root}/{relative}: broken local link {target!r}"
                )
            elif resolved.is_file():
                local_links.setdefault(relative, []).append(resolved.relative_to(root))

    runtime_files = {
        relative
        for relative in texts
        if relative.name == "SKILL.md"
        or relative.parts[0] in {"agents", "references", "scripts"}
    }
    queue = list(runtime_files)
    while queue:
        current = queue.pop()
        for linked in local_links.get(current, []):
            if linked not in runtime_files:
                runtime_files.add(linked)
                queue.append(linked)

    for relative, text in texts.items():
        path = root / relative
        errors.extend(skill_dependency_errors(text, relative, name, known_names))
        errors.extend(resource_path_errors(text, path, root))
        errors.extend(network_errors(text, relative, runtime_files))

    return errors


def run_self_test() -> tuple[list[str], int]:
    failures: list[str] = []
    case_count = 0
    with tempfile.TemporaryDirectory(prefix="skill-isolation-") as temp:
        workspace = Path(temp)

        def make_skill(name: str, body: str) -> Path:
            package = workspace / name
            package.mkdir()
            (package / "SKILL.md").write_text(
                "---\n"
                f"name: {name}\n"
                "description: Exercise the standalone package gate.\n"
                "---\n\n"
                f"# {name}\n\n{body}\n",
                encoding="utf-8",
            )
            return package

        def expect(
            label: str,
            package: Path,
            should_pass: bool,
            known: set[str] | None = None,
            contains: str | None = None,
        ) -> None:
            nonlocal case_count
            case_count += 1
            result = validate_skill(package, known or {package.name})
            if should_pass and result:
                failures.append(f"{label} was rejected: {result[0]}")
            if not should_pass and not result:
                failures.append(f"{label} was accepted")
            if (
                not should_pass
                and result
                and contains
                and not any(contains in error for error in result)
            ):
                failures.append(
                    f"{label} failed for the wrong reason: {result[0]}"
                )

        valid = make_skill("valid-skill", "Use only bundled instructions.")
        expect("valid standalone package", valid, True)

        nested = make_skill("nested-link", "Read [the reference](references/a.md).")
        (nested / "references").mkdir()
        (nested / "assets").mkdir()
        (nested / "references" / "a.md").write_text(
            "[asset](../assets/a_(b).txt)\n\nClaim.[^1]\n\n"
            "[^1]: A bundled explanatory footnote.\n",
            encoding="utf-8",
        )
        (nested / "assets" / "a_(b).txt").write_text("bundled\n", encoding="utf-8")
        expect("nested and balanced links", nested, True)

        shell_variable = make_skill("shell-variable", "Run the bundled script.")
        (shell_variable / "scripts").mkdir()
        (shell_variable / "scripts" / "run.sh").write_text(
            'printf "%s\\n" "$input"\n',
            encoding="utf-8",
        )
        expect("shell variable", shell_variable, True)

        negated = make_skill(
            "negated-dependency",
            "Never use `" + "external-" + "audit`; remain self-contained.",
        )
        expect("negated external workflow", negated, True)

        attribution = make_skill(
            "attribution-link",
            "Attribution only (not required): "
            + "https"
            + ":"
            + "/"
            + "/"
            + "example.invalid/paper.",
        )
        expect("supplemental attribution", attribution, True)

        local_skills_dir = make_skill(
            "local-skills-dir",
            "Read `skills/data/policy.txt`.",
        )
        (local_skills_dir / "skills" / "data").mkdir(parents=True)
        (local_skills_dir / "skills" / "data" / "policy.txt").write_text(
            "bundled\n",
            encoding="utf-8",
        )
        expect("bundled skills directory", local_skills_dir, True)

        ordinary_word = make_skill(
            "ordinary-word",
            "Run testing locally before completion.",
        )
        expect(
            "ordinary sibling-name word",
            ordinary_word,
            True,
            {"ordinary-word", "testing"},
        )

        missing_root = make_skill(
            "missing-root-file",
            "Read the repository-root `AGENTS.md` before acting.",
        )
        expect(
            "repository-root dependency",
            missing_root,
            False,
            contains="required local resource",
        )

        missing_tool = make_skill(
            "missing-tool",
            "Run `python3 tooling/check.py`; the checkout supplies it.",
        )
        expect(
            "unbundled command",
            missing_tool,
            False,
            contains="required local resource",
        )

        absolute = make_skill(
            "absolute-path",
            "Read `" + "/" + "opt/repository/shared.json` before acting.",
        )
        expect(
            "absolute local dependency",
            absolute,
            False,
            contains="absolute local path",
        )

        composed_parent = make_skill(
            "composed-parent",
            "In Python, load `Path(\"." + ".\") / \"shared.json\"`.",
        )
        expect(
            "composed parent dependency",
            composed_parent,
            False,
            contains="path escapes package",
        )

        external_workflow = make_skill(
            "external-workflow",
            "Consult `" + "external-" + "audit` before editing.",
        )
        expect(
            "external workflow",
            external_workflow,
            False,
            contains="external workflow",
        )

        casefold_peer = make_skill(
            "casefold-peer",
            "Consult Beta before editing.",
        )
        expect(
            "case-shifted sibling dependency",
            casefold_peer,
            False,
            {"casefold-peer", "beta"},
            contains="sibling skill",
        )

        generic_route = make_skill(
            "generic-route",
            "Route to a separately discovered "
            + "artifact-verification "
            + "skill.",
        )
        expect(
            "generic external-skill route",
            generic_route,
            False,
            contains="external skill",
        )

        linked_readme = make_skill(
            "linked-readme",
            "Before running, follow [setup](README.md).",
        )
        (linked_readme / "README.md").write_text(
            "Required: fetch "
            + "https"
            + ":"
            + "/"
            + "/"
            + "example.invalid/policy before each run.\n",
            encoding="utf-8",
        )
        expect(
            "runtime-linked network setup",
            linked_readme,
            False,
            contains="network",
        )

        scp_remote = make_skill(
            "scp-remote",
            "Clone `"
            + "git"
            + "@github.com:org/policy.git` before each run.",
        )
        expect(
            "scp-style network dependency",
            scp_remote,
            False,
            contains="network",
        )

        utf16 = make_skill("utf16-script", "Run the bundled policy check.")
        (utf16 / "scripts").mkdir()
        (utf16 / "scripts" / "run.ps1").write_text(
            "Consult `" + "external-" + "audit` before running.",
            encoding="utf-16",
        )
        expect(
            "UTF-16 external workflow",
            utf16,
            False,
            contains="external workflow",
        )

        plain_root = make_skill(
            "plain-root-file",
            "Read repository-root AGENTS.md before acting.",
        )
        expect(
            "plain repository-root dependency",
            plain_root,
            False,
            contains="required local resource",
        )

        variable_path = make_skill(
            "variable-path",
            "Read `"
            + "$"
            + "REPO_ROOT/shared/policy.md` before acting.",
        )
        expect(
            "variable-dependent path",
            variable_path,
            False,
            contains="variable-dependent path",
        )

        yaml_escape = make_skill(
            "yaml-escape",
            "Use the bundled agent configuration.",
        )
        (yaml_escape / "agents").mkdir()
        (yaml_escape / "agents" / "openai.yaml").write_text(
            "instructions: " + "." + "." + "/" + "shared/prompt.md\n",
            encoding="utf-8",
        )
        expect(
            "structured YAML escape",
            yaml_escape,
            False,
            contains="path escapes package",
        )

        html_escape = make_skill(
            "html-escape",
            "Render [the template](templates/page.html).",
        )
        (html_escape / "templates").mkdir()
        (html_escape / "templates" / "page.html").write_text(
            '<script src="'
            + "."
            + "."
            + "/"
            + 'shared/runtime.js"></script>\n',
            encoding="utf-8",
        )
        expect(
            "HTML resource escape",
            html_escape,
            False,
            contains="path escapes package",
        )

        shell_source = make_skill(
            "shell-source",
            "Run `scripts/run.sh`.",
        )
        (shell_source / "scripts").mkdir()
        (shell_source / "scripts" / "run.sh").write_text(
            "#!/bin/sh\n" + "source " + "tooling/common.sh\n",
            encoding="utf-8",
        )
        expect(
            "unbundled shell source",
            shell_source,
            False,
            contains="required local resource",
        )

        git_remote = make_skill(
            "git-remote",
            "Before running, follow [setup]("
            + "git"
            + ":"
            + "/"
            + "/"
            + "github.com/org/policy.git).",
        )
        expect(
            "git protocol dependency",
            git_remote,
            False,
            contains="network",
        )

        package_install = make_skill(
            "package-install",
            "Run `python3 -m "
            + "pip "
            + "install requests` before acting.",
        )
        expect(
            "runtime package installation",
            package_install,
            False,
            contains="network",
        )

        required_license = make_skill(
            "required-license",
            "Download the required license from "
            + "https"
            + ":"
            + "/"
            + "/"
            + "example.invalid/policy before running.",
        )
        expect(
            "required license download",
            required_license,
            False,
            contains="required network",
        )

        plain_external = make_skill(
            "plain-external",
            "Consult " + "external-" + "audit before editing.",
        )
        expect(
            "plain external workflow",
            plain_external,
            False,
            contains="external workflow",
        )

        prerequisite_skill = make_skill(
            "prerequisite-skill",
            "Prerequisite: " + "$" + "review approval is required.",
        )
        expect(
            "single-word prerequisite skill",
            prerequisite_skill,
            False,
            contains="external skill",
        )

        fenced_external = make_skill(
            "fenced-external",
            "Required workflow:\n\n```text\nConsult "
            + "external-"
            + "audit before editing.\n```",
        )
        expect(
            "fenced external workflow",
            fenced_external,
            False,
            contains="external workflow",
        )

        pytest_tool = make_skill(
            "pytest-tool",
            "Use `pytest` to run the bundled tests.",
        )
        expect("backticked tool", pytest_tool, True)

        mixed_negation = make_skill(
            "mixed-negation",
            "Use this skill; do not use `"
            + "external-"
            + "audit`.",
        )
        expect("clause-local negation", mixed_negation, True)

        inline_markdown = make_skill(
            "inline-markdown",
            "Literal syntax: `[label](missing.md)` is illustrative.",
        )
        expect("inline-code Markdown", inline_markdown, True)

        svg_namespace = make_skill(
            "svg-namespace",
            "Use [the bundled icon](assets/icon.svg).",
        )
        (svg_namespace / "assets").mkdir()
        (svg_namespace / "assets" / "icon.svg").write_text(
            '<svg xmlns="'
            + "http"
            + ":"
            + "/"
            + "/"
            + 'www.w3.org/2000/svg"></svg>\n',
            encoding="utf-8",
        )
        expect("SVG namespace", svg_namespace, True)

        optional_background = make_skill(
            "optional-background",
            "Read [the background](references/background.md).",
        )
        (optional_background / "references").mkdir()
        (optional_background / "references" / "background.md").write_text(
            "Historical background: "
            + "https"
            + ":"
            + "/"
            + "/"
            + "example.invalid/paper. Optional context only.\n",
            encoding="utf-8",
        )
        expect("optional external background", optional_background, True)

        bundled_glob = make_skill(
            "bundled-glob",
            "Read `references/*.md` before deciding.",
        )
        (bundled_glob / "references").mkdir()
        (bundled_glob / "references" / "a.md").write_text(
            "bundled\n",
            encoding="utf-8",
        )
        expect("bundled resource glob", bundled_glob, True)

        js_import_escape = make_skill(
            "js-import-escape",
            "Run the bundled JavaScript.",
        )
        (js_import_escape / "scripts").mkdir()
        (js_import_escape / "scripts" / "run.js").write_text(
            'import "'
            + "."
            + "."
            + "/"
            + 'shared/runtime.js";\n',
            encoding="utf-8",
        )
        expect(
            "JavaScript import escape",
            js_import_escape,
            False,
            contains="path escapes package",
        )

        json_list_escape = make_skill(
            "json-list-escape",
            "Use the bundled configuration.",
        )
        (json_list_escape / "assets").mkdir()
        (json_list_escape / "assets" / "config.json").write_text(
            '["' + "." + "." + "/" + 'shared/policy.json"]\n',
            encoding="utf-8",
        )
        expect(
            "JSON list escape",
            json_list_escape,
            False,
            contains="path escapes package",
        )

        json_schema = make_skill(
            "json-schema-id",
            "Use the bundled schema.",
        )
        (json_schema / "assets").mkdir()
        (json_schema / "assets" / "schema.json").write_text(
            '{"$schema":"'
            + "https"
            + ":"
            + "/"
            + "/"
            + 'json-schema.org/draft/2020-12/schema"}\n',
            encoding="utf-8",
        )
        expect("JSON schema identifier", json_schema, True)

        double_inline = make_skill(
            "double-inline-code",
            "Literal syntax: ``[label](missing.md)`` is illustrative.",
        )
        expect("double-backtick inline code", double_inline, True)

        npx_install = make_skill(
            "npx-runtime",
            "Run `npx remote-tool` before acting.",
        )
        expect(
            "runtime npx dependency",
            npx_install,
            False,
            contains="network",
        )

        missing_entrypoint = workspace / "missing-entrypoint"
        missing_entrypoint.mkdir()
        expect(
            "missing SKILL.md",
            missing_entrypoint,
            False,
            contains="missing SKILL.md",
        )

    return failures, case_count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate one standalone Agent Skill package."
    )
    parser.add_argument("skill", nargs="?", type=Path)
    parser.add_argument(
        "--known-name",
        action="append",
        default=[],
        help="a sibling skill name that must not become a dependency",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run the bundled adversarial validator fixtures",
    )
    args = parser.parse_args()

    errors: list[str] = []
    if args.self_test:
        failures, case_count = run_self_test()
        if failures:
            errors.extend(f"validator self-test: {failure}" for failure in failures)
        else:
            print(f"PASS validator self-test: {case_count} cases")

    if args.skill:
        known_names = set(args.known_name) | {args.skill.name}
        errors.extend(validate_skill(args.skill, known_names))
        if not errors:
            file_count = sum(1 for path in args.skill.rglob("*") if path.is_file())
            print(
                f"PASS {args.skill.name}: {file_count} files, "
                "structurally isolated"
            )
    elif not args.self_test:
        parser.error("provide a skill directory or --self-test")

    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
