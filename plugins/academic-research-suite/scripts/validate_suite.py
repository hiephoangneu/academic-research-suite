#!/usr/bin/env python3
"""Validate the Academic Research Suite source tree."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


EXPECTED_SKILLS = {
    "q1-manuscript-writer",
    "strict-peer-reviewer",
    "research-proposal-writer",
    "panel-econometrics-auditor",
    "pls-sem-fsqca-reviewer",
    "citation-integrity-auditor",
    "reviewer-response-manager",
    "literature-review",
}
EM_DASH = chr(8212)
SCAFFOLD_PLACEHOLDER = "[" + "TODO:"


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated YAML frontmatter")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"{path}: invalid frontmatter line: {line}")
        fields[key.strip()] = value.strip()
    if set(fields) != {"name", "description"}:
        raise ValueError(
            f"{path}: frontmatter must contain only name and description"
        )
    return fields


def validate() -> list[str]:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    manifest_path = root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{manifest_path}: invalid JSON: {exc}"]

    if manifest.get("name") != root.name:
        errors.append("plugin name must match the plugin directory")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin manifest must point skills to ./skills/")
    if manifest.get("version") != "1.1.0":
        errors.append("unexpected plugin version")

    skill_root = root / "skills"
    actual_skills = {path.name for path in skill_root.iterdir() if path.is_dir()}
    if actual_skills != EXPECTED_SKILLS:
        errors.append(
            f"skill set mismatch: expected {sorted(EXPECTED_SKILLS)}, "
            f"found {sorted(actual_skills)}"
        )

    for skill_name in sorted(EXPECTED_SKILLS):
        skill_dir = skill_root / skill_name
        skill_path = skill_dir / "SKILL.md"
        agent_path = skill_dir / "agents" / "openai.yaml"
        try:
            text = skill_path.read_text(encoding="utf-8")
            fields = parse_frontmatter(text, skill_path)
        except Exception as exc:
            errors.append(str(exc))
            continue

        if fields["name"] != skill_name:
            errors.append(f"{skill_path}: name must match directory")
        if len(fields["description"]) < 80:
            errors.append(f"{skill_path}: description is too vague")
        if "TODO" in text:
            errors.append(f"{skill_path}: contains TODO")
        if EM_DASH in text:
            errors.append(f"{skill_path}: contains an em dash")

        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in link or link.startswith("#"):
                continue
            target = (skill_dir / link).resolve()
            if not target.is_file():
                errors.append(f"{skill_path}: broken local link {link}")

        if not agent_path.is_file():
            errors.append(f"{agent_path}: missing")
        else:
            agent_text = agent_path.read_text(encoding="utf-8")
            if f"${skill_name}" not in agent_text:
                errors.append(
                    f"{agent_path}: default prompt must mention ${skill_name}"
                )
            if EM_DASH in agent_text or "TODO" in agent_text:
                errors.append(f"{agent_path}: contains forbidden placeholder or dash")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        if SCAFFOLD_PLACEHOLDER in text:
            errors.append(f"{path}: contains scaffold placeholder")
        if EM_DASH in text:
            errors.append(f"{path}: contains an em dash")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Academic Research Suite validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
