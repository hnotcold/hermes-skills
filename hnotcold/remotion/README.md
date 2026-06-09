# Remotion

使用 Remotion 和 React 创建可编辑的 AI 视频项目，支持预览和渲染为 MP4。适合竖版短视频、产品演示、故事动画、HUD/科技视觉、广告、教程等场景。

## 功能

- 用 React 组件定义视频内容
- 支持关键帧动画、CSS 动画、GSAP 等
- 字幕和语音旁白支持
- 音效和背景音乐
- 可迭代编辑（代码改 → 预览 → 渲染）

## 前置条件

- Hermes Agent 已安装
- Node.js 环境
- Remotion 已安装（Hermes 会自动处理）

## 使用方式

描述你想要的视频：

- "做一个 15 秒的产品介绍视频，竖版，标题从下方滑入"
- "创建一个科技感的数据仪表盘动画"
- "做一个带字幕的教程视频，有代码展示效果"

Hermes 会：
1. 生成 Remotion 项目代码
2. 启动预览服务器供你查看
3. 确认后渲染为 MP4

## 适用场景

- 竖版短视频（抖音/TikTok/Reels）
- 产品演示和宣传片
- 故事驱动的动画
- HUD/科技风格视觉
- 信息流广告
- 教程和演示视频
- 字幕动画
- 语音旁白视频

## 项目结构

```
remotion-project/
├── src/
│   ├── Root.tsx          # 入口组件
│   ├── Composition.tsx   # 视频主组件
│   └── ...               # 其他组件
├── public/               # 静态资源
├── remotion.config.ts    # 配置
└── package.json
```

## License

MIT
