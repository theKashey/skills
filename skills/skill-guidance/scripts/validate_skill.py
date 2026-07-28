#!/usr/bin/env python3
"""Deterministic structural validation for one standalone Agent Skill package.

Checks only mechanically decidable properties: frontmatter contract, text
encoding, forbidden artifacts, local link closure, README runtime exclusion,
literal network references in runtime files, and parent-directory escapes in
scripts and structured data. Semantic questions -- whether prose creates an
external dependency, whether a network mention is load-bearing -- belong to
the audit route, not this gate. PASS therefore claims exactly what was
checked and nothing more.
"""

from __future__ import annotations

import argparse
import codecs
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_RE = re.compile(r"(?m)^([A-Za-z][\w-]*):\s*(.*?)\s*$")
# Assembled so this file's own source never contains a literal scheme
# separator and stays clean under its own runtime scan.
_SEP = ":" + "//"
REMOTE_URL_RE = re.compile(
    r"\b(?:ftp|git|https?|ssh)" + re.escape(_SEP) + r"\S+", re.IGNORECASE
)
SCP_REMOTE_RE = re.compile(r"(?<![\w.-])[\w.-]+@[\w.-]+:[\w~./-]{2,}")
NETWORK_COMMAND_RE = re.compile(
    r"\b(?:curl|wget)(?=\s|$)|\b(?:git\s+clone|npx|bunx|pip\d*\s+install|"
    r"(?:npm|pnpm|yarn)\s+(?:add|install))\b",
    re.IGNORECASE,
)
SCHEMA_LINE_RE = re.compile(r"""["']?\$schema["']?\s*:""")
PARENT_TOKEN_RE = re.compile(r"""(?:^|[\s"'`=(\[{,;])((?:\.\./)+[\w@()./-]*)""")
TEXT_SUFFIXES = {
    ".css", ".csv", ".html", ".ini", ".js", ".json", ".jsx", ".md", ".mjs",
    ".ps1", ".py", ".rb", ".sh", ".svg", ".toml", ".ts", ".tsx", ".txt",
    ".xml", ".yaml", ".yml",
}
ESCAPE_SCAN_SUFFIXES = {
    ".js", ".json", ".mjs", ".ps1", ".py", ".rb", ".sh", ".ts", ".tsx",
    ".yaml", ".yml",
}
COMMAND_SURFACES = {".md", ".ps1", ".sh", ".txt", ".yaml", ".yml"}
RUNTIME_ROOTS = {"agents", "references", "scripts"}
MAX_DESCRIPTION = 240


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
        if path.name == "SKILL.md" or path.suffix.lower() in TEXT_SUFFIXES or mode & 0o111:
            return None, "runtime or executable text is not UTF-8/UTF-16"
        return None, None


def parse_frontmatter(text: str) -> tuple[str | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return None, None
    body = lines[1 : lines[1:].index("---") + 1]
    fields = {m.group(1): m.group(2) for m in FIELD_RE.finditer("\n".join(body))}
    name = (fields.get("name") or "").strip("\"'") or None
    description = (fields.get("description") or "").strip("\"'")
    if description in {"", ">", "|", ">-", "|-"}:
        start = next((i for i, l in enumerate(body) if l.startswith("description:")), -1)
        block = []
        for line in body[start + 1 :]:
            if line and not line[0].isspace():
                break
            block.append(line.strip())
        description = " ".join(part for part in block if part)
    return name, description or None


def without_fences(text: str) -> str:
    out: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = line.lstrip()[:3]
        if fence is None and marker in {"```", "~~~"}:
            fence = marker
        elif fence is not None and line.lstrip().startswith(fence):
            fence = None
        elif fence is None:
            out.append(line)
            continue
        out.append("\n" if line.endswith("\n") else "")
    return "".join(out)


def without_inline_code(text: str) -> str:
    return re.sub(
        r"``[^`\n](?:[^`\n]|`(?!`))*``|`[^`\n]*`",
        lambda m: " " * len(m.group(0)),
        text,
    )


def markdown_destinations(text: str) -> list[str]:
    text = without_inline_code(without_fences(text))
    found: list[str] = []
    index = 0
    while index < len(text):
        if text[index] != "[" or (index and text[index - 1] == "\\"):
            index += 1
            continue
        close = index + 1
        while close < len(text) and not (text[close] == "]" and text[close - 1] != "\\"):
            close += 1
        if close >= len(text):
            break
        index = close + 1
        if index >= len(text) or text[index] != "(":
            continue
        depth, index = 1, index + 1
        start = index
        while index < len(text) and depth:
            char = text[index]
            if char == "\\":
                index += 2
                continue
            depth += char == "("
            depth -= char == ")"
            if not depth:
                found.append(text[start:index].strip())
            index += 1
    for line in text.splitlines():
        match = re.match(r"^\s*\[([^\]^][^\]]*)\]:\s*(\S+)", line)
        if match:
            found.append(match.group(2))
    return found


def local_link_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0] if target else ""
    if not target or target.startswith("#") or urlsplit(target).scheme:
        return None
    return unquote(target.split("#", 1)[0])


def network_errors(relative: Path, text: str) -> list[str]:
    errors: list[str] = []
    suffix = relative.suffix.lower()
    for number, line in enumerate(text.splitlines(), start=1):
        if suffix in {".svg", ".xml", ".html"} and "xmlns" in line:
            continue
        if suffix in {".json", ".yaml", ".yml"} and SCHEMA_LINE_RE.search(line):
            continue
        if REMOTE_URL_RE.search(line) or SCP_REMOTE_RE.search(line):
            errors.append(f"{relative}:{number}: literal network reference in runtime file")
        elif suffix in COMMAND_SURFACES and NETWORK_COMMAND_RE.search(line):
            errors.append(f"{relative}:{number}: network command in runtime file")
    return errors


def escape_errors(relative: Path, path: Path, root: Path, text: str) -> list[str]:
    errors: list[str] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for match in PARENT_TOKEN_RE.finditer(line):
            resolved = (path.parent / match.group(1)).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{relative}:{number}: parent path escapes package")
    return errors


def fenced_shell_escape_errors(relative: Path, path: Path, root: Path, text: str) -> list[str]:
    """Check executable Markdown fences without treating ordinary prose as code."""
    errors: list[str] = []
    fence: str | None = None
    shell_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        marker = line.lstrip()
        if fence is None and marker.startswith(("```", "~~~")):
            fence = marker[:3]
            language = marker[3:].strip().casefold()
            shell_fence = language in {"bash", "sh", "shell", "zsh"}
            continue
        if fence is not None and marker.startswith(fence):
            fence = None
            shell_fence = False
            continue
        if not shell_fence:
            continue
        for match in PARENT_TOKEN_RE.finditer(line):
            resolved = (path.parent / match.group(1)).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{relative}:{number}: parent path escapes package")
    return errors


def validate_skill(skill_root: Path) -> list[str]:
    if skill_root.is_symlink():
        return [f"{skill_root}: package root must not be a symlink"]
    root = skill_root.resolve()
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_root}: missing SKILL.md"]

    errors: list[str] = []
    text, decode_error = decode_text(skill_file)
    if decode_error or text is None:
        return [f"{skill_file}: {decode_error or 'unreadable'}"]
    name, description = parse_frontmatter(text)
    if not name or not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid or missing frontmatter name")
    elif name != root.name:
        errors.append(f"{skill_file}: name {name!r} does not match directory")
    if not description:
        errors.append(f"{skill_file}: missing frontmatter description")
    elif len(description) > MAX_DESCRIPTION:
        errors.append(f"{skill_file}: description exceeds {MAX_DESCRIPTION} characters")

    texts: dict[Path, str] = {}
    links: dict[Path, list[Path]] = {}
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
        content, decode_error = decode_text(path)
        if decode_error:
            errors.append(f"{skill_root}/{relative}: {decode_error}")
            continue
        if content is None:
            continue
        texts[relative] = content
        if path.suffix.lower() != ".md":
            continue
        for raw in markdown_destinations(content):
            target = local_link_target(raw)
            if target is None:
                continue
            if Path(target).is_absolute() or re.match(r"^[A-Za-z]:[\\/]", target):
                errors.append(f"{skill_root}/{relative}: absolute local link {target!r}")
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f"{skill_root}/{relative}: link escapes package: {target!r}")
                continue
            if not resolved.exists():
                errors.append(f"{skill_root}/{relative}: broken local link {target!r}")
            elif resolved.is_file():
                links.setdefault(relative, []).append(resolved.relative_to(root))

    runtime = {
        relative
        for relative in texts
        if relative.name == "SKILL.md" or relative.parts[0] in RUNTIME_ROOTS
    }
    queue = list(runtime)
    while queue:
        for linked in links.get(queue.pop(), []):
            if linked not in runtime:
                runtime.add(linked)
                queue.append(linked)
    if Path("README.md") in runtime:
        errors.append(
            f"{skill_root}/README.md: maintainer README must not be a runtime dependency"
        )

    for relative, content in texts.items():
        if relative in runtime:
            errors.extend(network_errors(relative, content))
        if relative.suffix.lower() in ESCAPE_SCAN_SUFFIXES:
            errors.extend(escape_errors(relative, root / relative, root, content))
        elif relative.suffix.lower() == ".md":
            errors.extend(fenced_shell_escape_errors(relative, root / relative, root, content))
    return errors


def run_self_test() -> tuple[list[str], int]:
    failures: list[str] = []
    count = 0
    up = "../"  # kept separate from tails so this source holds no resolvable escape literal
    url = "https" + _SEP
    with tempfile.TemporaryDirectory(prefix="skill-gate-") as temp:
        workspace = Path(temp)

        def make(name, body, description="Exercise the gate.", files=()):
            package = workspace / name
            package.mkdir()
            (package / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: {description}\n---\n\n# {name}\n\n{body}\n",
                encoding="utf-8",
            )
            for rel, content in files:
                target = package / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            return package

        def expect(label, package, ok, contains=""):
            nonlocal count
            count += 1
            result = validate_skill(package)
            if ok and result:
                failures.append(f"{label} rejected: {result[0]}")
            elif not ok and not result:
                failures.append(f"{label} accepted")
            elif not ok and contains and not any(contains in e for e in result):
                failures.append(f"{label} wrong reason: {result[0]}")

        expect("valid package", make("valid-skill", "Use only bundled material."), True)
        expect("overlong description", make("overlong", "Body.", "x" * 241), False, "exceeds")
        expect("name mismatch", make("mismatch", "Body.", files=[
            ("SKILL.md", "---\nname: other-name\ndescription: D.\n---\n# x\n")]),
            False, "does not match directory")
        expect("broken link", make("broken", "See [a](references/a.md)."), False, "broken local link")
        expect("escaping link", make("escapee", f"See [a]({up}shared.md)."), False, "escapes package")
        expect("absolute link", make("absolute", "See [a](/etc/hosts)."), False, "absolute local link")
        expect("balanced nested link", make("nested", "See [a](references/a.md).", files=[
            ("references/a.md", f"[asset]({up}assets/a_(b).txt)\n\nClaim.[^1]\n\n[^1]: Note.\n"),
            ("assets/a_(b).txt", "bundled\n")]), True)
        expect("inline-code link", make("inline", "Literal: `[a](m.md)` and ``[b](g.md)``."), True)
        expect("runtime README", make("readme-rt", "Read [notes](README.md).", files=[
            ("README.md", "Maintainer notes.\n")]), False, "runtime dependency")
        expect("runtime URL", make("rt-url", f"Fetch {url}example.invalid/x first."),
            False, "literal network reference")
        expect("non-runtime URL", make("rd-url", "Use only bundled material.", files=[
            ("README.md", f"Background: {url}example.invalid/paper.\n")]), True)
        expect("network command", make("net-cmd", "Run `pip install requests` first."),
            False, "network command")
        expect("command-like prose", make("curl-like", "Keep curl-like labels descriptive."), True)
        expect("svg namespace", make("svg-ns", "Use [icon](assets/i.svg).", files=[
            ("assets/i.svg", f'<svg xmlns="{url}www.w3.org/2000/svg"></svg>\n')]), True)
        expect("schema identifier", make("schema-id", "Use [s](references/s.json).", files=[
            ("references/s.json", f'{{"$schema": "{url}json-schema.org/x"}}\n')]), True)
        expect("script escape", make("s-escape", "Run the bundled script.", files=[
            ("scripts/run.js", f'import "{up}{up}shared/r.js";\n')]), False, "escapes package")
        expect("shell fence escape", make("fence-escape", "Run this:\n```bash\nsource " + up + "shared.sh\n```"),
            False, "escapes package")
        expect("script internal", make("s-internal", "Run the bundled script.", files=[
            ("scripts/run.js", f'import "{up}assets/d.json";\n'),
            ("assets/d.json", "{}\n")]), True)
        artifact = make("artifact", "Use only bundled material.")
        (artifact / "__pycache__").mkdir()
        (artifact / "__pycache__" / "x.pyc").write_bytes(b"\x00")
        expect("generated artifact", artifact, False, "generated artifact")
        missing = workspace / "missing"
        missing.mkdir()
        expect("missing SKILL.md", missing, False, "missing SKILL.md")
    return failures, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("skill", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    if args.self_test:
        failures, count = run_self_test()
        if failures:
            errors.extend(f"validator self-test: {f}" for f in failures)
        else:
            print(f"PASS validator self-test: {count} cases")
    if args.skill:
        target = args.skill.resolve()
        errors.extend(validate_skill(target))
        if not errors:
            files = sum(1 for p in target.rglob("*") if p.is_file())
            print(f"PASS {target.name}: {files} files, mechanical checks and runtime isolation")
    elif not args.self_test:
        parser.error("provide a skill directory or --self-test")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
