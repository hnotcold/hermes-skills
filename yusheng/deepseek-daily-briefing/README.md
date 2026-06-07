# 🐙 DeepSeek 每日用量简报

每日自动推送 DeepSeek API 余额和用量监控简报。

## 功能

- 💰 **余额查询** — 当前账户余额
- 📊 **本月用量** — 累计花费和 Token 用量
- 📅 **昨日花费** — 按模型细分的日花费
- ⚡ **今日已用** — 当天实时用量
- 🔔 **自动推送** — 通过飞书 / Telegram 定时推送

## 前置条件

- Hermes Agent 已配置
- DeepSeek API Key（用于余额查询）
- DeepSeek Platform Token（用于用量明细查询，需从 DeepSeek Web 控制台获取）
- 消息平台已连接

## 安装

### 1. 复制文件

```bash
cp -r deepseek-daily-briefing/ ~/.hermes/skills/productivity/
cp deepseek_daily_briefing.py ~/.hermes/scripts/
```

### 2. 配置凭据

在 `~/.hermes/.env` 中添加：

```
DEEPSEEK_API_KEY=sk-your_api_key_here
```

创建 `~/.hermes/deepseek_platform_token`：

```
# DeepSeek Platform API Token
your_platform_token_here
```

### 3. 创建 Cron Job

```bash
cronjob action=create \
  name="DeepSeek 每日用量简报" \
  schedule="0 9 * * *" \
  no_agent=true \
  script="deepseek_daily_briefing.py" \
  workdir="$HOME/.hermes" \
  deliver="feishu"
```

> ⚠️ `script` 参数只传文件名（不加 `scripts/` 前缀），系统会自动补全路径。

## 输出示例

```
🐙 **DeepSeek 每日简报**  |  `2026-06-07 09:00`

💰 **余额** — ¥87.60（可用约 29.2万 tokens）

📊 **本月累计（2026年06月）**
  花费: ¥0.32  |  Tokens: 2.288M

📅 **昨日花费（2026-06-06）** — ¥0.12
  • deepseek-v4-pro: ¥0.08
  • deepseek-v4-flash: ¥0.04

⚡ **今日已用（2026-06-07）** — ¥0.00
```

## 认证说明

DeepSeek 有两个不同的凭据：

| 凭据 | 用途 | 获取方式 |
|------|------|---------|
| `DEEPSEEK_API_KEY` | 模型推理 + 余额查询 | API Key 页面 |
| Platform Token | 管理 API（用量、账单） | Web 控制台 → 开发者工具 |

## 技术细节

- 使用 Python 标准库（无需额外依赖）
- 调用的 DeepSeek 内部 API：
  - `/v1/user/balance` — 余额（API Key 认证）
  - `/api/v0/users/get_user_summary` — 月总览（Platform Token）
  - `/api/v0/usage/cost` — 日明细（Platform Token）
- 支持跨月边界处理

## 许可证

MIT
