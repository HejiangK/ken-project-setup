# CLAUDE.md

This repository contains the `ken-project-setup` Skill.

Use it to initialize a Chinese office AI workspace for Word, Excel, PPT, and PDF deliverables.

## Primary Files

- `SKILL.md`: source of truth for when and how the Skill should be used.
- `scripts/init_ken_project.py`: deterministic initializer for project folders.
- `agents/openai.yaml`: Codex UI metadata.
- `.cursor/rules/ken-project-setup.mdc`: Cursor-compatible project rule.

## Behavior

When asked to initialize a project:

1. Use the target directory provided by the user.
2. If no directory is provided, ask for a project name unless the current directory is clearly intended.
3. Prefer running:

   ```bash
   python scripts/init_ken_project.py <target-directory>
   ```

4. Use `--force` only when the user explicitly asks to overwrite existing template files.
5. Preserve existing user files.

## Generated Structure

```text
<project>/
├─ AGENTS.md
├─ raw/
├─ docs/
│  ├─ source-notes.md
│  └─ questions.md
├─ output/
└─ memory-bank/
   └─ PROJECT-MEMORY.md
```

## Required Rules

Generated projects must keep these rules:

- `raw/` stores original materials and should be treated as read-only.
- `docs/` stores process notes, source notes, drafts, and open questions.
- `output/` stores final Word, Excel, PPT, PDF, screenshots, and previews.
- `memory-bank/` stores durable project background and preferences only.
- Do not store secrets, API keys, credentials, or private customer data in `memory-bank/`.
- Data, facts, and conclusions must come from the project first.
- External sources must include source name, link or file name, and citation date.
- Missing information goes to `docs/questions.md`; do not fabricate.

## Office Skill Routing

- Use `minimax-docx` for Word / DOCX.
- Use `minimax-xlsx` for Excel / XLSX.
- Use `ppt-master` for PPT / PPTX.
- Use `minimax-pdf` for formal PDF reports.

## Validation

Before claiming changes are complete:

```bash
python -m py_compile scripts/init_ken_project.py
```

If the Skill validation tool is available, also run:

```bash
python <skill-creator>/scripts/quick_validate.py .
```

Test initialization in a temporary directory when changing `scripts/init_ken_project.py`.
