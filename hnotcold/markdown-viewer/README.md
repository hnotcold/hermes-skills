# Markdown Viewer

在 Markdown 中直接创建丰富的图表、数据可视化、技术架构图和内容卡片。支持 Mermaid、PlantUML、Vega-Lite、Excalidraw JSON Canvas 等多种图表格式。

## 功能

- **Mermaid 图表**：流程图、时序图、甘特图、类图等
- **PlantUML 架构图**：UML、云架构、网络拓扑、安全架构
- **Vega-Lite 图表**：数据可视化（柱状图、折线图、散点图等）
- **JSON Canvas**：Excalidraw 风格的手绘图
- **信息图**：排版精美的内容卡片

## 前置条件

- Hermes Agent 已安装
- （可选）PlantUML 服务用于渲染 UML 图

## 使用方式

直接描述你需要的图表：

- "画一个微服务架构图"
- "用 Mermaid 画一个用户登录的流程图"
- "做一个展示月度销售数据的柱状图"
- "创建一个系统设计的架构图，包含 API Gateway、数据库和缓存层"

## 支持的图表类型

| 格式 | 适用场景 |
|------|---------|
| Mermaid | 流程图、时序图、甘特图、ER 图 |
| PlantUML | UML 类图、部署图、组件图 |
| Vega-Lite | 数据图表（柱/线/散点/饼） |
| JSON Canvas | 手绘风格图、思维导图 |

## 输出

生成 SVG 或 PNG 图片，嵌入对话回复中。

## License

MIT
