#!/usr/bin/env python3
"""道具全案 HTML 结构自检（prop-asset-image-prompts §4 回读自检的机械版）。

用法: python verify_prop_html.py <全案.html>
检查: 卡号序列 / pre id 序列 / div·table 配平 / 双按钮配对 / 资产表行数 / meta 计数 / 收尾与残留锚点。
退出码: 0=全绿, 1=有 FAIL, 2=用法错误。
"""
import re
import sys


def main(path):
    try:
        with open(path, encoding="utf-8-sig") as file:
            html = file.read()
    except (OSError, UnicodeError) as error:
        print(f"读取全案失败：{error}", file=sys.stderr)
        return 2

    cards = [int(x) for x in re.findall(r'<span class="prop-no">P-(\d+)</span>', html)]
    pres = [int(x) for x in re.findall(r'<pre class="prompt" id="p(\d+)">', html)]
    rows = [int(x) for x in re.findall(r'<tr><td>P-(\d+)</td>', html)]
    copytext = len(re.findall(r"copyText\('", html))
    copypre = len(re.findall(r"copyPre\('", html))
    n = len(cards)

    checks = []

    def chk(name, ok, detail=""):
        checks.append((name, ok, detail))

    chk("卡号序列 P-01..P-%02d 连续" % n, n > 0 and cards == list(range(1, n + 1)), "共 %d 卡" % n)
    chk("pre id 序列 p1..p%d 连续" % n, pres == list(range(1, n + 1)), "%d 个" % len(pres))
    chk("卡片/pre/资产表行数量一致", n == len(pres) == len(rows),
        "cards=%d pres=%d rows=%d" % (n, len(pres), len(rows)))
    chk("双按钮配对（复制名称+一键复制）", copytext == n and copypre == n,
        "copyText=%d copyPre=%d" % (copytext, copypre))
    chk("div 配平", html.count("<div") == html.count("</div>"),
        "%d/%d" % (html.count("<div"), html.count("</div>")))
    chk("table 配平", html.count("<table") == html.count("</table>"),
        "%d/%d" % (html.count("<table"), html.count("</table>")))
    chk("资产表行与卡号同序", rows == cards, "%d 行" % len(rows))
    chk("收尾 </html>", html.rstrip().endswith("</html>"), "")
    chk("无残留锚点", "<!--APPEND-->" not in html, "")
    meta = re.search(r"本版\s*(\d+)\s*卡", html)
    if meta:
        chk("meta 计数=卡数", int(meta.group(1)) == n, "meta=%s vs %d" % (meta.group(1), n))

    fail = 0
    for name, ok, detail in checks:
        print("PASS" if ok else "FAIL", name, ("— " + detail) if detail else "")
        fail += 0 if ok else 1
    print("RESULT: %d/%d PASS" % (len(checks) - fail, len(checks)))
    return 1 if fail else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python verify_prop_html.py <全案.html>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
