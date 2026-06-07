# 🐙 Hermes Skills 共享仓库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

朋友之间分享好用的 [Hermes Agent](https://hermes-agent.nousresearch.com) Skills 的公开仓库。

> **Hermes Agent** 是一个可组合的 AI 智能体系统，Skill 是其核心扩展机制——通过 YAML + Markdown 定义的技能模块，让 AI 助手掌握特定领域的工作流、API 调用和最佳实践。

## 目录结构

```
hermes-skills/
├── README.md              # 本文件
├── LICENSE                # MIT 许可证
├── .gitignore
└── <username>/            # 每个贡献者自己的目录
    ├── <skill-name>/
    │   ├── README.md      # 技能说明和使用方法
    │   ├── SKILL.md       # Hermes Skill 定义文件
    │   └── ...            # 脚本、参考文档等附属文件
    └── ...
```

## 贡献指南

### 添加你的技能

1. **Fork 本仓库** 并 clone 到本地
2. 在根目录下创建你的 **用户名目录**（如 `zhangsan/`）
3. 在用户名目录下创建技能子目录（如 `zhangsan/my-awesome-skill/`）
4. 添加 `SKILL.md`（Hermes 技能定义文件）及附属文件
5. 提交 Pull Request

### 命名规范

- 用户名目录：使用你的 GitHub 用户名或习惯的英文代号
- 技能目录：`kebab-case` 命名（如 `daily-briefing-cron`）
- 主文件：统一使用 `SKILL.md`

### 脱敏要求

**推送前请检查并移除以下内容：**
- ❌ API Key、Token、密码等敏感凭据
- ❌ 个人文件路径（如 `/Users/yourname/` → `~/` 或 `$HOME/`）
- ❌ 个人隐私信息（地址、电话等）
- ❌ 内部业务数据

## 技能列表

| 贡献者 | 技能 | 说明 |
|--------|------|------|
| [yusheng](yusheng/) | [晨间简报](yusheng/morning-briefing-cron/) | 每日自动推送新闻、天气、股票简报 |
| [yusheng](yusheng/) | [DeepSeek 每日用量简报](yusheng/deepseek-daily-briefing/) | 每日监控 DeepSeek API 余额和用量 |

---

**灵感来源:** [Hermes Agent Skills](https://hermes-agent.nousresearch.com/docs/category/skills)
