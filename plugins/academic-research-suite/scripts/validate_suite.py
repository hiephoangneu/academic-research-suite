#!/usr/bin/env python3
"""Validate the Academic Research Suite source tree."""

from __future__ import annotations

import hashlib
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
    "academic-paper-q1-ssci-skill",
}
UPSTREAM_SHA256 = {
    "01-master-instructions.md": "2586492da125760453949e9ca20a43fd58cd7057a626961ee51c9d1e06972d6e",
    "02-paper-structure.md": "5d9de68de2ec49653e8dd3006d6716f06b668052464790ed37117ba242e2040c",
    "03-writing-guidelines.md": "55bf28a6ca48081b5472a80a6be0223b1caf482be9ad99ddee6213129bf751a4",
    "04-methodology-templates.md": "b1038e402e30a18d31281439ac225f9da936a28a4b038a4d3a03fa0496083905",
    "05-quality-checklist.md": "b4f1ab737f55da35b6652380e5d1b3cd4cd54c2e6dd2b9f50487a3d0f75819ac",
    "06-literature-review-guide.md": "0fbd6d3af45c38ea326ec982b90e5887eb9d34d21cf748bcbaf08df19844d308",
    "07-common-reviewer-comments.md": "00c7f5d40e48f85d9d3d28704f7def093276d14947544a36423a0fc050703ab9",
    "09-academic-phrases-bank.md": "a27cab7a7025aab48fdfc21f0e1c9f3d0fc9769cbdb714b51e52b4586fd08c37",
    "10-response-letter-template.md": "3592b2255e48dd9cad69912ab46688382e9f11b918ad25a5062c8b970d8e7af0",
    "README.md": "3176fdaa1ad0b0fb04b9f53bb63bdb52ab7889cc11132054ff293c147195bc3f",
    "SKILL.md": "c14aa0582a5a8cfba4dfba1161e3d8b4be47b370ee5317bf547a231c4e5bb736",
    "examples_sample-abstract.md": "ef72b5665e12e9356700de97ab61c20644073d3bebab5c75351539947d975c73",
    "examples_sample-hypothesis-args.md": "767b3bd5253c7bef188081a57579d49333c080f07c7a1ed70e69a52d276dcb56",
    "examples_sample-introduction.md": "4ec511bcb8fd6ed0fd8008fde0b75ce20ee06c266246b9e0e35640dd5e1af1e9",
    "examples_sample-response-letter.md": "7d5304e146defe86e57fd05e313578142f8c4e62d8fb11532dc93ca82f46c69a",
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
    if manifest.get("version") != "1.2.0":
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

    upstream_root = (
        skill_root
        / "academic-paper-q1-ssci-skill"
        / "references"
        / "upstream"
    )
    actual_upstream = (
        {path.name for path in upstream_root.iterdir() if path.is_file()}
        if upstream_root.is_dir()
        else set()
    )
    if actual_upstream != set(UPSTREAM_SHA256):
        errors.append(
            "vendored upstream file set mismatch: "
            f"expected {sorted(UPSTREAM_SHA256)}, found {sorted(actual_upstream)}"
        )
    for filename, expected_hash in UPSTREAM_SHA256.items():
        path = upstream_root / filename
        if not path.is_file():
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            errors.append(f"{path}: differs from the pinned upstream source")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".py"}:
            continue
        if upstream_root in path.parents:
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
