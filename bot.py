import json
import random

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

print("Link promo:", promo)
print("Caption siap posting:", caption)
