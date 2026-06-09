# Grok Image to Video

通过 Hermes Web UI 将本地图片转换为短视频（MP4），使用 xAI Grok Imagine 的图像动画能力。

## 功能

- 将静态图片转为 3-6 秒的短视频
- 支持多种动画风格（电影级、动漫、3D 等）
- 自动添加运镜和动态效果

## 前置条件

- Hermes Agent 已安装并运行
- Hermes Web UI 已启动
- xAI API Key 已配置（通过 Hermes Web UI 的 provider 管理）

## 使用方式

1. 准备一张图片（本地路径或 URL）
2. 对 Hermes 说：

```
把这张图片变成视频：/path/to/image.png
```

或者指定风格：

```
用电影级风格把这张图动画化：/path/to/image.png
```

## 输出

- MP4 文件，保存到 `~/.hermes/` 下的临时目录
- 完成后自动发送到对话渠道

## License

MIT
