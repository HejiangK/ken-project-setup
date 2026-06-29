---
name: ken-project-setup
description: Initialize a Ken-style AI project workspace for Chinese office/document tasks. Use when the user asks to create or initialize a Codex project, office AI workspace, project scaffold, raw/docs/output/memory-bank structure, AGENTS.md rules, anti-hallucination data-source rules, or a reusable setup for Word, Excel, PPT, and PDF deliverables.
---

# Ken Project Setup

Initialize a clean AI office project workspace that Codex can use as a real work site, not just a chat thread.

The default structure is:

```text
<project>/
├─ AGENTS.md
├─ CLAUDE.md
├─ .cursor/
│  └─ rules/
│     └─ ken-project-setup.mdc
├─ raw/
├─ docs/
│  ├─ source-notes.md
│  └─ questions.md
├─ output/
└─ memory-bank/
   └─ PROJECT-MEMORY.md
```

## Workflow

1. Determine the target directory.
   - If the user gives a project name or path, use it.
   - If they do not, ask for the project name unless the current directory is clearly the intended project.
   - Do not initialize in a sensitive existing project root unless the user explicitly asks.
2. Run the initializer script when possible:

   ```bash
   python <skill-dir>/scripts/init_ken_project.py <target-directory>
   ```

   Use `--force` only when the user explicitly asks to overwrite existing template files.
3. If script execution is not available, manually create the same directories and files with the templates in this skill.
4. After initialization, tell the user:
   - where the project was created,
   - which files were created or skipped,
   - where to put raw materials,
   - that final Word/Excel/PPT/PDF deliverables should go to `output/`.

## Generated Rules

`AGENTS.md` must be written in Chinese and include these required sections:

- `目录规则`
- `数据与事实规则`
- `Skill 使用规则`
- `工作规则`

`CLAUDE.md` must mirror the same project rules for Claude Code compatibility.

`.cursor/rules/ken-project-setup.mdc` must mirror the same project rules for Cursor compatibility and use `alwaysApply: true`.

The data rules are mandatory:

- Prefer facts and data from `raw/`, `docs/`, and `memory-bank/`.
- External sources must include source name, link or file name, and citation date.
- Do not fabricate customers, amounts, growth rates, market data, citations, or conclusions.
- If information is missing, write questions to `docs/questions.md` instead of guessing.
- Key data in Word, Excel, PPT, and PDF outputs must cite its source.

The Skill routing rules are mandatory:

- Use `minimax-docx` for Word / DOCX.
- Use `minimax-xlsx` for Excel / XLSX.
- Use `ppt-master` for PPT / PPTX.
- Use `minimax-pdf` for formal PDF reports.

## Default Next Prompt

After setup, suggest this next prompt only if the user wants to generate office deliverables:

```text
请按 AGENTS.md 的规则处理这个项目：

1. 阅读 raw/ 中的原始材料；
2. 先在 docs/source-notes.md 记录关键数据来源；
3. 使用 minimax-docx 生成 Word 文档到 output/；
4. 使用 minimax-xlsx 生成 Excel 表格到 output/；
5. 使用 ppt-master 生成 PPT 演示文稿到 output/；
6. 使用 minimax-pdf 生成正式 PDF 报告到 output/；
7. 所有关键数据必须标注来源；
8. 信息不足时写入 docs/questions.md，不要编造；
9. 生成后检查文件是否存在，并说明每个文件的用途。
```

## Safety

- Preserve existing user files.
- Skip existing template files unless the user explicitly requests overwrite.
- Never place generated deliverables in the project root.
- Never move or edit original files in `raw/` unless the user explicitly asks.
- Do not store secrets, API keys, passwords, private customer data, or credentials in `memory-bank/`.

## Examples

User:

```text
用 ken-project-setup 帮我初始化一个办公项目，名字叫 codex-office-demo。
```

Action:

```bash
python <skill-dir>/scripts/init_ken_project.py codex-office-demo
```

User:

```text
在当前目录创建 raw/docs/output/memory-bank 和 AGENTS.md，适合生成 Word、Excel、PPT、PDF。
```

Action:

```bash
python <skill-dir>/scripts/init_ken_project.py .
```
