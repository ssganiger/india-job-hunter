#!/usr/bin/env python3
"""Build the Claude skill archive and the standalone prompt from shared sources."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "india-job-hunter"
SEED = SKILL / "references" / "target-companies.md"
CORE_PROMPT = ROOT / "prompts" / "core-prompt.md"
PASTE_PROMPT = ROOT / "prompts" / "paste-ready-prompt.md"
PACKAGE = ROOT / "dist" / "india-job-hunter.skill"


def main() -> None:
    core = CORE_PROMPT.read_text(encoding="utf-8").rstrip()
    seed = SEED.read_text(encoding="utf-8").rstrip()
    PASTE_PROMPT.write_text(
        f"{core}\n\n---\n\n## Appendix: target-company seed (unverified)\n\n{seed}\n",
        encoding="utf-8",
    )

    PACKAGE.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(PACKAGE, "w", ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(SKILL.parent))

    with ZipFile(PACKAGE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Skill archive failed integrity check")
        if "india-job-hunter/SKILL.md" not in archive.namelist():
            raise RuntimeError("Skill archive lacks SKILL.md")

    print(f"Built {PASTE_PROMPT.relative_to(ROOT)} and {PACKAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
