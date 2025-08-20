import json
import random
import requests
from datetime import datetime
import os

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

# --- Save ke file txt/CSV ---
output_folder = "daily_posts"
os.makedirs(output_folder, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(output_folder, f"{today}.txt")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(caption + "\n" + promo)

print("Link promo:", promo)
print("Caption siap posting:", caption)
print(f"Disimpan di: {file_path}")
