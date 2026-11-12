#!/usr/bin/env python3
"""检查道具提示词的长度、句式与否定字预算。"""

import argparse
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", type=Path, help="UTF-8 提示词文件")
    args = parser.parse_args()
    try:
        text = args.prompt.read_text(encoding="utf-8-sig").strip()
    except (OSError, UnicodeError) as error:
        parser.error(f"读取提示词失败：{error}")

    sentences = [
        fragment.strip()
        for fragment in re.split(r"[。！？；!?;\n]+", text)
        if fragment.strip()
    ]
    longest = max((len(sentence) for sentence in sentences), default=0)
    most_commas = max(
        (sentence.count("，") + sentence.count(",") for sentence in sentences),
        default=0,
    )
    negatives = len(re.findall(r"[不无没勿禁]", text))
    checks = (
        ("全文 100–3000 字符", 100 <= len(text) <= 3000, len(text)),
        ("单句最多 80 字符", longest <= 80, longest),
        ("单句最多 6 个逗号", most_commas <= 6, most_commas),
        ("全文最多 3 个否定字", negatives <= 3, negatives),
    )
    for name, passed, count in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}（{count}）")
    return 0 if all(passed for _, passed, _ in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
