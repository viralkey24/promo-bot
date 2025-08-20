import json
import random
import requests

# Load config
with open("config.json") as f:
    data = json.load(f)

links = data["links"]
promo = random.choice(links)

# Template caption
templates = [
    "🔥 Cek ini bro: {link} 🚀",
    "💥 Jangan sampai ketinggalan: {link} ✨",
    "🌟 Hanya hari ini: {link} 😎",
    "⚡ Promo spesial: {link} 🎯"
]

caption = random.choice(templates).format(link=promo)

# --- Kirim ke Telegram ---
TOKEN = "8095758972:AAF4nFCSYh9iT5DqyoeWb4kcpwo52cswUwU"
CHAT_ID = "5912438442"

msg = f"{caption}"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
requests.get(url)

print("Link promo:", promo)
print("Caption siap posting:", caption)
