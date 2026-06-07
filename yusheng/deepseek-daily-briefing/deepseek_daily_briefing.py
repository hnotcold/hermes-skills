#!/usr/bin/env python3
"""DeepSeek daily briefing script - fetches balance, monthly cost, yesterday cost.

Usage: Place this script at ~/.hermes/scripts/deepseek_daily_briefing.py
and configure a cron job with:
  cronjob action=create name="DeepSeek Daily Briefing" schedule="0 9 * * *" 
    no_agent=true script="deepseek_daily_briefing.py" workdir="$HOME/.hermes" deliver="feishu"

Prerequisites:
  - DEEPSEEK_API_KEY in ~/.hermes/.env (for balance query)
  - DeepSeek platform token in ~/.hermes/deepseek_platform_token (for usage queries)
"""
import json, os
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen

# ---- Configuration ----
# Change these paths to match your setup
HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))


# ---- Credential Loading ----
def load_platform_token():
    """Read platform token from deepseek_platform_token file (skips comment lines)."""
    token_path = HERMES_HOME / "deepseek_platform_token"
    try:
        for line in token_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    except (FileNotFoundError, IOError):
        return None
    return None


def load_api_key():
    """Read DeepSeek API key from .env file."""
    env_path = HERMES_HOME / ".env"
    try:
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip("\"'")
    except (FileNotFoundError, IOError):
        return None
    return None


# ---- HTTP Helper ----
def fetch_json(url, token=None):
    """Fetch JSON from URL with optional Bearer auth."""
    req = Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", "Hermes/1.0")
    with urlopen(req, timeout=15) as r:
        return json.loads(r.read())


# ---- Formatting Helpers ----
def fmt_yuan(v):
    """Format yuan with ¥ prefix."""
    return f"¥{float(v):.2f}"


def fmt_tokens(v):
    """Format token count in human-readable form (Chinese units)."""
    n = int(float(v))
    if n >= 1_0000_0000:
        return f"{n/1_0000_0000:.1f}亿"
    elif n >= 1_0000:
        return f"{n/1_0000:.1f}万"
    else:
        return str(n)


# ---- Main ----
def main():
    platform_token = load_platform_token()
    api_key = load_api_key()

    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    yesterday_year = yesterday.strftime("%Y")
    yesterday_month = yesterday.strftime("%m")
    today_year = today.strftime("%Y")
    today_month = today.strftime("%m")

    lines = []
    yesterday_cost = 0.0
    yesterday_details = []
    todays_cost = 0.0
    todays_details = []

    # === 1. Balance ===
    balance_data = fetch_json("https://api.deepseek.com/user/balance", token=api_key) if api_key else {}
    balance = "N/A"
    if "balance_infos" in balance_data and balance_data["balance_infos"]:
        balance = fmt_yuan(balance_data["balance_infos"][0]["total_balance"])

    # === 2. User Summary (monthly overview) ===
    summary = fetch_json(
        "https://platform.deepseek.com/api/v0/users/get_user_summary",
        token=platform_token,
    ) if platform_token else {}
    monthly_cost = "N/A"
    monthly_tokens = "N/A"
    token_estimation = "N/A"
    try:
        biz = summary["data"]["biz_data"]
        monthly_cost = fmt_yuan(biz["monthly_costs"][0]["amount"])
        monthly_tokens = fmt_tokens(biz["monthly_token_usage"])
        token_estimation = biz.get("total_available_token_estimation", "N/A")
    except (KeyError, IndexError, TypeError):
        pass

    # === 3. Yesterday's cost breakdown ===
    if platform_token:
        try:
            cost_data = fetch_json(
                f"https://platform.deepseek.com/api/v0/usage/cost?year={yesterday_year}&month={yesterday_month}",
                token=platform_token,
            )
            biz_data = cost_data.get("data", {}).get("biz_data", [])
            if isinstance(biz_data, list):
                biz_data = biz_data[0] if biz_data else {}
            for day in biz_data.get("days", []):
                if day.get("date") == yesterday_str:
                    for me in day.get("data", []):
                        model = me.get("model", "unknown")
                        total = sum(float(u.get("amount", "0")) for u in me.get("usage", []))
                        if total > 0:
                            yesterday_details.append(f"  • {model}: {fmt_yuan(str(total))}")
                        yesterday_cost += total
        except Exception:
            pass

    # === 4. Today's cost breakdown ===
    if platform_token:
        try:
            cost_today = fetch_json(
                f"https://platform.deepseek.com/api/v0/usage/cost?year={today_year}&month={today_month}",
                token=platform_token,
            )
            biz_today = cost_today.get("data", {}).get("biz_data", [])
            if isinstance(biz_today, list):
                biz_today = biz_today[0] if biz_today else {}
            for day in biz_today.get("days", []):
                if day.get("date") == today.strftime("%Y-%m-%d"):
                    for me in day.get("data", []):
                        model = me.get("model", "unknown")
                        total = sum(float(u.get("amount", "0")) for u in me.get("usage", []))
                        if total > 0:
                            todays_details.append(f"  • {model}: {fmt_yuan(str(total))}")
                        todays_cost += total
        except Exception:
            pass

    # === Build Report ===
    lines.append(f"🐙 **DeepSeek 每日简报**  |  `{today.strftime('%Y-%m-%d %H:%M')}`")
    lines.append("")
    lines.append(f"💰 **余额** — {balance}")
    if token_estimation != "N/A":
        lines[-1] += f"（可用约 {fmt_tokens(token_estimation)} tokens）"
    lines.append("")
    lines.append(f"📊 **本月累计（{today_year}年{today_month}月）**")
    lines.append(f"  花费: {monthly_cost}  |  Tokens: {monthly_tokens}")
    lines.append("")
    lines.append(f"📅 **昨日花费（{yesterday_str}）** — {fmt_yuan(str(yesterday_cost))}")
    if yesterday_details:
        for d in yesterday_details:
            lines.append(d)
    lines.append("")
    lines.append(f"⚡ **今日已用（{today.strftime('%Y-%m-%d')}）** — {fmt_yuan(str(todays_cost))}")
    if todays_details:
        for d in todays_details:
            lines.append(d)
    lines.append("")
    lines.append("---")
    lines.append("🐙 DeepSeek 监控")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
