# scripts/telegram_ping.py
import os, requests, json
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT  = os.getenv("DAMIAN_BOT_CHAT")
MSG   = os.getenv("MESSAGE") or datetime.now().strftime("Ping desde script: %d/%m/%Y %H:%M:%S")

if not TOKEN or not CHAT:
    raise SystemExit("Faltan TELEGRAM_TOKEN o DAMIAN_BOT_CHAT")

resp = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT, "text": MSG, "disable_web_page_preview": True},
    timeout=20
)
resp.raise_for_status()
data = resp.json()
print("Enviado ✅", json.dumps(data, ensure_ascii=False))
