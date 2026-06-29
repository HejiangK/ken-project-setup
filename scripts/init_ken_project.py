#!/usr/bin/env python3
"""Initialize a Ken-style AI office project workspace."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from textwrap import dedent


DIRS = ["raw", "docs", "output", "memory-bank"]


def write_text(path: Path, content: str, force: bool, created: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    created.append(str(path))


def touch(path: Path, created: list[str]) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8", newline="\n")
        created.append(str(path))


def agents_md(project_name: str) -> str:
    return dedent(
        f"""\
        # AGENTS.md

        文档内容请以中文为主。

        ## 项目目标

        本项目是一个基础办公 AI 工作区，用于整理原始材料、沉淀过程文档，并生成 Word、Excel、PPT、PDF 等正式办公交付物。

        项目名称：{project_name}

        ## 目录规则

        - `raw/`：原始材料目录，只读，不要覆盖、改名或移动。公司介绍、销售数据、客户资料、截图、PDF、Word、Excel 都先放这里。
        - `docs/`：过程文档目录。摘要、大纲、分析说明、数据来源、问题清单都放这里。
        - `output/`：最终交付目录。Word、Excel、PPT、PDF、封面图、预览截图都放这里。
        - `memory-bank/`：项目记忆目录。只记录长期有效的背景、决策和偏好，不保存密钥、账号、客户隐私或一次性临时信息。

        ## 数据与事实规则

        - 所有数据、事实、结论，必须优先来自本项目内的 `raw/`、`docs/` 或 `memory-bank/`。
        - 如果使用外部数据、网页、报告或公开资料，必须给出来源说明。
        - 外部引用必须写清楚：来源名称、链接或文件名、引用日期。
        - 不允许编造客户、金额、增长率、市场数据、引用来源或不存在的结论。
        - 如果信息不足，先写入 `docs/questions.md`，不要硬编。
        - 生成 Word、Excel、PPT、PDF 时，关键数据必须标注来源。

        ## Skill 使用规则

        - 生成 Word / DOCX 文档时，优先使用 `minimax-docx`。
        - 生成 Excel / XLSX 表格时，优先使用 `minimax-xlsx`。
        - 生成 PPT / PPTX 演示文稿时，使用 `ppt-master`。
        - 生成正式 PDF 报告时，优先使用 `minimax-pdf`。

        ## 工作规则

        1. 先阅读 `raw/` 的原始材料，不直接生成最终文件。
        2. 先在 `docs/source-notes.md` 记录关键数据来源。
        3. 如果信息不足，写入 `docs/questions.md`，不要编造。
        4. 确认数据来源后，再生成正式交付物。
        5. 最终文件必须放入 `output/`。
        6. 交付前检查文件是否存在、格式是否正确、内容是否符合项目规则。
        """
    )


def source_notes(project_name: str) -> str:
    return dedent(
        f"""\
        # source-notes · {project_name}

        > 记录本项目所有关键事实、数据和结论的来源。生成 Word、Excel、PPT、PDF 前先更新本文件。

        ## 项目内来源

        | 编号 | 文件 | 关键信息 | 用途 |
        |---|---|---|---|
        | S1 | `raw/` |  |  |

        ## 外部来源

        | 编号 | 来源名称 | 链接或文件名 | 引用日期 | 关键信息 | 用途 |
        |---|---|---|---|---|---|
        | E1 |  |  | {date.today().isoformat()} |  |  |

        ## 关键结论

        | 结论 | 来源编号 | 可用于哪些产物 |
        |---|---|---|
        |  |  |  |
        """
    )


def questions_md(project_name: str) -> str:
    return dedent(
        f"""\
        # questions · {project_name}

        > 信息不足时写在这里，不要在正式文件里硬编。

        | 编号 | 问题 | 为什么需要 | 当前处理 |
        |---|---|---|---|
        | Q1 |  |  | 待用户确认 |
        """
    )


def project_memory(project_name: str) -> str:
    return dedent(
        f"""\
        # PROJECT-MEMORY · {project_name}

        > 只记录长期有效的项目背景、固定偏好和已经确认的决策。不要保存密钥、账号、客户隐私或一次性临时信息。

        ## 项目背景

        - 

        ## 常用口吻

        - 中文为主。
        - 表达清楚、稳重、适合基础办公场景。

        ## 固定格式偏好

        - 最终交付物放入 `output/`。
        - 关键数据需要标注来源。

        ## 已确认决策

        | 日期 | 决策 | 说明 |
        |---|---|---|
        | {date.today().isoformat()} | 初始化项目结构 | 使用 `raw/docs/output/memory-bank/AGENTS.md` |
        """
    )


def init_project(target: Path, force: bool) -> tuple[list[str], list[str]]:
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []

    for dirname in DIRS:
        directory = target / dirname
        directory.mkdir(parents=True, exist_ok=True)
        created.append(str(directory))

    project_name = target.name or "ken-office-project"

    write_text(target / "AGENTS.md", agents_md(project_name), force, created, skipped)
    write_text(target / "docs" / "source-notes.md", source_notes(project_name), force, created, skipped)
    write_text(target / "docs" / "questions.md", questions_md(project_name), force, created, skipped)
    write_text(target / "memory-bank" / "PROJECT-MEMORY.md", project_memory(project_name), force, created, skipped)

    touch(target / "raw" / ".gitkeep", created)
    touch(target / "output" / ".gitkeep", created)

    return created, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Ken-style AI office project workspace.")
    parser.add_argument("target", help="Target project directory. Use . for the current directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files.")
    args = parser.parse_args()

    created, skipped = init_project(Path(args.target), args.force)

    print("Ken project setup complete.")
    print()
    print("Created or ensured:")
    for item in created:
        print(f"  + {item}")

    if skipped:
        print()
        print("Skipped existing files (use --force to overwrite):")
        for item in skipped:
            print(f"  - {item}")

    print()
    print("Next steps:")
    print("  1. Put original materials in raw/.")
    print("  2. Record source notes in docs/source-notes.md.")
    print("  3. Generate final Word/Excel/PPT/PDF files into output/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
