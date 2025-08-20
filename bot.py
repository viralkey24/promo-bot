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
    "🔥 Cek ini bro: {link} {emoji} {hashtag}",
    "💥 Jangan sampai ketinggalan: {link} {emoji} {hashtag}",
    "🌟 Hanya hari ini: {link} {emoji} {hashtag}",
    "⚡ Promo spesial: {link} {emoji} {hashtag}"
]

emojis = ["🚀","✨","🎯","😎","🔥","💎","🌈"]
hashtags = ["#PromoMantap","#CuanTerus","#AutoCash","#DealHariIni","#HotSale"]

caption = random.choice(templates).format(
    link=promo,
    emoji=random.choice(emojis),
    hashtag=random.choice(hashtags)
)

# --- Kirim ke Telegram ---
TOKEN = "8095758972:AAF4nFCSYh9iT5DqyoeWb4kcpwo52cswUwU"
CHAT_ID = "5912438442"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={caption}"
requests.get(url)

print("Link promo:", promo)
print("Caption siap posting:", caption)
