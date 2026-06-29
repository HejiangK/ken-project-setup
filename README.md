# ken-project-setup

一个用于初始化基础办公 AI 项目的 Codex Skill。

它会创建一套适合 Word、Excel、PPT、PDF 办公交付的项目结构，并写好 `AGENTS.md` 规则，帮助 Codex 明确原始材料、过程文档、最终输出和项目记忆应该放在哪里。

## 适合什么场景

- 第一次用 Codex 做办公项目。
- 想让 Codex 生成 Word、Excel、PPT、PDF 等文件。
- 想给项目加上 `raw / docs / output / memory-bank / AGENTS.md` 基础结构。
- 想在项目规则里加入数据来源、防幻觉、外部引用说明等要求。

## 创建的项目结构

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

## 核心规则

初始化后的 `AGENTS.md` 会包含：

- `raw/` 放原始材料，只读，不乱改。
- `docs/` 放过程文档、数据来源、问题清单。
- `output/` 放最终 Word、Excel、PPT、PDF。
- `memory-bank/` 放长期有效的项目背景和偏好。
- 数据、事实、结论优先来自本项目。
- 外部引用必须写清来源名称、链接或文件名、引用日期。
- 信息不足时写入 `docs/questions.md`，不要硬编。
- Word 使用 `minimax-docx`。
- Excel 使用 `minimax-xlsx`。
- PPT 使用 `ppt-master`。
- PDF 使用 `minimax-pdf`。

## 在 Codex 中使用

安装或导入这个 Skill 后，可以这样说：

```text
用 $ken-project-setup 初始化一个办公项目，名字叫 codex-office-demo。
```

也可以在当前目录初始化：

```text
用 $ken-project-setup 在当前目录创建 raw、docs、output、memory-bank 和 AGENTS.md。
```

## 直接运行脚本

如果你只想使用脚本，也可以运行：

```bash
python scripts/init_ken_project.py codex-office-demo
```

在当前目录初始化：

```bash
python scripts/init_ken_project.py .
```

如需覆盖已有模板文件：

```bash
python scripts/init_ken_project.py codex-office-demo --force
```

## 推荐下一步

初始化完成后，把原始材料放进 `raw/`，然后对 Codex 说：

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

## 注意事项

- 不要把真实密钥、账号、客户隐私放进 `memory-bank/`。
- 不要把最终交付文件散落在项目根目录。
- 不要改动 `raw/` 里的原始材料，除非你明确要求 Codex 这么做。
