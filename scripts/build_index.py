#!/usr/bin/env python3
"""Rebuild the small generated index between explicit markers in README.md."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- generated-index:start -->"
END = "<!-- generated-index:end -->"


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def entries(folder: str) -> list[str]:
    paths = sorted((ROOT / folder).rglob("*.md"), reverse=True)
    return [f"- [{title(path)}]({path.relative_to(ROOT).as_posix()})" for path in paths]


def main() -> None:
    sections = [
        "## 自动索引",
        "",
        "### 阵容原型分级",
        *entries("composition-tiers"),
        "",
        "### 每日复盘",
        *entries("daily"),
        "",
        "### 五位置逐路检验",
        *entries("tier-lists/roles"),
        "",
        "### 层级历史",
        *entries("tier-lists/history"),
        "",
        "### 逆风阵容候选",
        *entries("comeback-comps/candidates"),
    ]
    generated = f"{START}\n" + "\n".join(sections) + f"\n{END}"
    text = README.read_text(encoding="utf-8")
    if START in text and END in text:
        prefix, rest = text.split(START, 1)
        _, suffix = rest.split(END, 1)
        text = prefix.rstrip() + "\n\n" + generated + suffix
    else:
        text = text.rstrip() + "\n\n" + generated + "\n"
    README.write_text(text, encoding="utf-8")
    print("INDEX OK")


if __name__ == "__main__":
    main()
