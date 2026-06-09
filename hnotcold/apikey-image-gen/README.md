# APIKEY Image Generation

通过 Hermes Web UI 生成或编辑图片，底层使用 [api.apikey.fun](https://api.apikey.fun) 的图像生成 API。

## 功能

- **文生图**：根据文字描述生成图片
- **图生图**：基于参考图片生成新图
- **图片编辑**：局部修改已有图片

## 前置条件

- Hermes Agent 已安装并运行
- Hermes Web UI 已启动（默认端口 8648）
- `config.yaml` 中已配置 `custom_providers` 的 `fun-codex` 条目

## 使用方式

直接对 Hermes 说：

- "生成一张赛博朋克风格的城市夜景"
- "把这张图改成油画风格"
- "在这张图片的左上角加一个月亮"

Hermes 会自动调用 Web UI 的 media endpoint 完成生成，无需手动提供 API Key。

## 技术细节

- 不直接调用外部 API，而是通过 Hermes Web UI 的 media endpoint 中转
- Web UI 读取 `config.yaml` 中的 `fun-codex` provider 配置
- 支持自定义模型和参数

## License

MIT
