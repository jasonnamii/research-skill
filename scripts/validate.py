#!/usr/bin/env python3
"""
research-frame validate.py
스킬 구조·트리거·INVARIANT·evals 5케이스 회귀 검증.

Usage: python scripts/validate.py [skill_path]
"""
import json
import re
import sys
from pathlib import Path


def check_structure(skill_path: Path) -> list[str]:
    """필수 파일·디렉토리 존재 확인."""
    errors = []
    required = [
        "SKILL.md",
        "CHANGELOG.md",
        "references/why.md",
        "references/how.md",
        "references/scope.md",
        "references/output-template.md",
        "references/invariants.md",
        "evals/cases.json",
        "scripts/validate.py",
    ]
    for rel in required:
        if not (skill_path / rel).exists():
            errors.append(f"MISSING: {rel}")
    return errors


def check_triggers(skill_md: str) -> list[str]:
    """트리거 티어 최소 요건 — frontmatter description 우선, HTML 주석 fallback."""
    errors = []
    # Prefer frontmatter description (scanner compatibility)
    fm = re.search(r"^---\n(.*?)\n---", skill_md, re.DOTALL)
    block = ""
    if fm and re.search(r"P1:", fm.group(1)):
        block = fm.group(1)
    else:
        trigger_block = re.search(r"<!-- Trigger Conditions(.*?)-->", skill_md, re.DOTALL)
        if trigger_block:
            block = trigger_block.group(1)
    if not block:
        return ["Trigger block not found"]

    p1_line = re.search(r"P1:\s*(.+)", block)
    if p1_line:
        p1_items = [x.strip() for x in p1_line.group(1).split(",") if x.strip()]
        if len(p1_items) < 5:
            errors.append(f"P1 < 5 (got {len(p1_items)})")
    else:
        errors.append("P1 missing")

    for tier, min_count in [("P2", 2), ("P3", 2), ("P5", 1)]:
        line = re.search(rf"{tier}:\s*(.+)", block)
        if not line:
            errors.append(f"{tier} missing")
            continue
        items = [x.strip() for x in line.group(1).split(",") if x.strip()]
        if len(items) < min_count:
            errors.append(f"{tier} < {min_count} (got {len(items)})")

    if "NOT:" not in block:
        errors.append("NOT clause missing")
    return errors


def check_hub_size(skill_md_path: Path) -> list[str]:
    """SKILL.md 허브 크기 — 목표 5KB, 최대 7KB(여유)."""
    size = skill_md_path.stat().st_size
    if size > 7168:
        return [f"SKILL.md too large: {size}B > 7168B"]
    return []


def check_invariants_doc(skill_path: Path) -> list[str]:
    """invariants.md INVARIANT 6개 존재."""
    errors = []
    inv_path = skill_path / "references/invariants.md"
    if not inv_path.exists():
        return ["invariants.md missing"]
    content = inv_path.read_text()
    required_sections = ["INVARIANT", "PREFLIGHT", "RESET", "STEALTH"]
    for sec in required_sections:
        if sec not in content:
            errors.append(f"invariants.md: {sec} section missing")
    return errors


def check_evals(skill_path: Path) -> list[str]:
    """evals/cases.json 스키마 + 최소 케이스 수."""
    errors = []
    evals_path = skill_path / "evals/cases.json"
    if not evals_path.exists():
        return ["evals/cases.json missing"]
    try:
        data = json.loads(evals_path.read_text())
    except json.JSONDecodeError as e:
        return [f"cases.json parse error: {e}"]
    cases = data.get("cases", [])
    if len(cases) < 5:
        errors.append(f"cases < 5 (got {len(cases)})")
    for c in cases:
        if "id" not in c or "expected" not in c:
            errors.append(f"case schema incomplete: {c.get('id', '?')}")
    return errors


def check_self_check_section(skill_md: str) -> list[str]:
    """Self-Check 섹션 존재."""
    if "Self-Check" not in skill_md and "self-check" not in skill_md.lower():
        return ["Self-Check section missing in SKILL.md"]
    return []


def check_version_field(skill_md: str) -> list[str]:
    """frontmatter version 필드."""
    fm = re.search(r"^---\n(.*?)\n---", skill_md, re.DOTALL)
    if not fm:
        return ["frontmatter missing"]
    if "version:" not in fm.group(1):
        return ["version field missing in frontmatter"]
    return []


def main():
    skill_path = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not (skill_path / "SKILL.md").exists():
        print(f"ERROR: SKILL.md not found at {skill_path}")
        sys.exit(2)

    skill_md = (skill_path / "SKILL.md").read_text()

    all_errors = []
    for name, fn in [
        ("structure", lambda: check_structure(skill_path)),
        ("triggers", lambda: check_triggers(skill_md)),
        ("hub_size", lambda: check_hub_size(skill_path / "SKILL.md")),
        ("invariants_doc", lambda: check_invariants_doc(skill_path)),
        ("evals", lambda: check_evals(skill_path)),
        ("self_check", lambda: check_self_check_section(skill_md)),
        ("version", lambda: check_version_field(skill_md)),
    ]:
        errors = fn()
        status = "PASS" if not errors else "FAIL"
        print(f"[{status}] {name}")
        for e in errors:
            print(f"  - {e}")
        all_errors.extend([(name, e) for e in errors])

    print()
    if all_errors:
        print(f"Total: {len(all_errors)} errors")
        sys.exit(1)
    else:
        print("All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
