# 道具资产出图提示词 Skill

为短剧、美术设定和分镜整理可直接粘贴的中文出图提示词。支持道具三视图、单视角、正反两面、载具、手机界面和屏幕配图。实体资产默认使用 `#767676` 灰底，并附视图名、尺寸标注和尺寸依据表。

## 在 Hermes 使用

把仓库克隆到 Hermes 的技能目录，新会话即可发现该 Skill。

```sh
mkdir -p ~/.hermes/skills/storyboard
git clone https://github.com/BaoZhengchen/prop-asset-image-prompts.git ~/.hermes/skills/storyboard/prop-asset-image-prompts
```

已经装有同名 Skill 时，先保留原副本，再替换目录。也可以直接把 [SKILL.md](SKILL.md) 和它引用的文件交给支持本地文件的助手。

> 请用 prop-asset-image-prompts，把第 1 集第 2 场里的空骨瓷茶杯写成即梦三视图提示词，给出尺寸依据，再做成一张可复制名称和提示词的 HTML 资产卡。

## 示例与检查

[茶杯提示词](examples/tea-cup.txt) 和 [道具全案 HTML](examples/prop-sheet.html) 展示同一张资产卡。保存 HTML 后可用浏览器打开。提示词和 HTML 检查只使用 Python 3 标准库。

```sh
python3 scripts/lint_prop_prompt.py examples/tea-cup.txt
python3 scripts/verify_prop_html.py examples/prop-sheet.html
```

提示词脚本检查长度、句式和否定字预算。HTML 脚本检查卡号、提示词、资产表和按钮等结构锚点。尺寸取值、出图后的文字准确性和跨格一致性仍由人工核对。

## 许可证

[MIT](LICENSE)
