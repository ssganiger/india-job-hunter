# India Job Hunter

A reusable India job-search skill for Claude and Codex, with a standalone prompt for assistants that cannot load local skills. It uses a candidate's real experience to find and assess current openings, then produces a sourced tracker.

## Files

```text
skills/india-job-hunter/SKILL.md
skills/india-job-hunter/references/source-playbook.md
skills/india-job-hunter/agents/openai.yaml
dist/india-job-hunter.skill
prompts/paste-ready-prompt.md
REVIEW.md
```

## Install

**Claude.ai:** Download [the skill package](dist/india-job-hunter.skill) and upload it in Customize → Skills. Enable Code execution and file creation if your account requires it. Claude Code users can copy `skills/india-job-hunter/` to `~/.claude/skills/` or a project's `.claude/skills/`. These installations are separate.

**Codex in ChatGPT desktop / Codex CLI:** Copy `skills/india-job-hunter/` to `~/.agents/skills/` for personal use or to `.agents/skills/` in a repository. You can also ask `$skill-installer` to install the skill from this repository. Restart Codex if a new skill does not appear.

**ChatGPT without local skill support:** Paste [the standalone prompt](prompts/paste-ready-prompt.md) into a conversation or appropriate custom instructions. A GitHub repository alone does not install a standalone skill in ChatGPT web.

See the current [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude skill documentation](https://support.claude.com/en/articles/12512180-use-skills-in-claude) if the interface changes.

## Use

Ask: “Find India jobs that match my resume.” Attach a resume or describe your experience. Optionally add target titles, cities, remote preference, salary floor, excluded companies, and freshness. The assistant should label verified openings separately from unverified leads and cite a direct listing for each.

For a repeat sweep, give it your prior tracker so it can preserve statuses and identify new, changed, and closed roles. Review each listing before applying; postings can close after a search.

## Privacy and limits

Do not commit a personal resume, tracker, credentials, or private correspondence to this public repository. Search and document processing depend on the AI product and tools you use; check their privacy settings. The skill does not grant access to logged-in job boards or guarantee complete market coverage.

## License

MIT
