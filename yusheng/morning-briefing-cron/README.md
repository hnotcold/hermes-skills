# 🌅 晨间简报 (Daily Morning Briefing)

每日自动推送的晨间简报 Skill，聚合新闻、天气和股票数据。

## 功能

- 🇨🇳 **国内热点** — 聚合百度新闻、新浪国内新闻等来源
- 🌍 **国际热点** — 新浪国际新闻、Google News
- 📈 **科技股行情** — 中美 Top 11 科技股实时数据
- 🌤️ **天气查询** — 南京、北京天气（可自定义城市）
- 💡 **出行建议**

## 前置条件

- Hermes Agent 已配置
- 飞书 / Telegram 等消息平台已连接（用于接收简报）
- **（可选）** Bocha API Key（用于深度搜索——非必需，新闻通过浏览器抓取）

## 安装

### 1. 复制 Skill 文件

```bash
cp -r path/to/morning-briefing-cron ~/.hermes/skills/productivity/
```

### 2. 配置节假日文件

创建节假日数据文件（格式参考 `china-holidays-2026.json`）：

```bash
mkdir -p ~/.hermes/workspace/memory/milestones/
```

节假日 JSON 格式示例：

```json
{
  "2026": {
    "new_year": {
      "name": "元旦",
      "holidays": ["2026-01-01", "2026-01-02", "2026-01-03"],
      "workdays": []
    }
  }
}
```

### 3. （可选）配置 Bocha API

如需使用 Bocha 搜索，在 `.env` 中添加：

```
BOCHA_API_KEY=your_key_here
```

### 4. 创建 Cron Job

```bash
cronjob action=create \
  name="晨间简报" \
  schedule="55 8 * * *" \
  deliver="<你的平台:feishu/telegram等>" \
  prompt="🌅 执行晨间简报任务\n\n## 📋 任务流程\n\n### 1. 读取节假日配置\n读取 holidays JSON 判断今日是否为工作日\n\n### 2. 聚合新闻\n- 国内：browser_navigate → news.baidu.com\n- 国际：browser_navigate → news.sina.com.cn/world/\n\n### 3. 获取天气\n- 通过 wttr.in 或 weather.com.cn\n\n### 4. 获取股票\n- 使用 Sina Finance API 获取中美科技股行情\n\n### 5. 格式化输出\n按照模板格式输出完整简报"
```

## 配置说明

### 自定义城市

修改 SKILL.md 中的天气城市 ID：

| 城市 | 代码 |
|------|------|
| 南京 | 101190101 |
| 北京 | 101010100 |
| 上海 | 101020100 |
| 深圳 | 101280601 |

### 自定义股票池

编辑 SKILL.md 中的 `# Tracked tickers` 部分。

## 输出格式

```
🌅 晨间简报 | YYYY-MM-DD 周X [工作日/休息日]

🇨🇳 国内热点 Top 10（8-10 条带摘要）
🌍 国际热点 Top 10（8-10 条带摘要）
📈 科技股 Top 10（中国 + 美国）
🌤️ 天气（南京/北京）
💡 出行建议
```

## 数据来源

| 类型 | 来源 | 备注 |
|------|------|------|
| 国内新闻 | news.baidu.com | 热点要闻 + 热搜词 |
| 国际新闻 | news.sina.com.cn/world/ | 分钟级更新 |
| 天气 | wttr.in / weather.com.cn | 二选一 |
| 美股行情 | Sina Finance API (`hq.sinajs.cn`) | 需 `Referer` 头 |
| 港股行情 | Sina Finance API (`hq.sinajs.cn`) | 需 `Referer` 头 |

## 许可证

MIT
