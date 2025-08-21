import json
import random
import requests
from datetime import datetime
import os

# Load config
with open("config.json") as f:
    data = json.load(f)

links = data["links"]

# Template caption
templates = [
    "🔥 Check this out: {link} {emoji} {hashtag}",
    "💥 Don't miss out: {link} {emoji} {hashtag}",
    "🌟 Today only: {link} {emoji} {hashtag}",
    "⚡ Special deal: {link} {emoji} {hashtag}"
]

# Emoji list
emojis = ["🥓","🥗","🍳","🔥","💪","🌟","🍀"]

# Hashtag list
hashtags = ["#KetoLife","#KetoDiet","#LowCarb","#HealthyEating","#FatLoss"]

# --- Generate multiple captions ---
num_captions = 5
captions = []

for _ in range(num_captions):
    link = random.choice(links)
    caption = random.choice(templates).format(
        link=link,
        emoji=random.choice(emojis),
        hashtag=random.choice(hashtags)
    )
    captions.append((link, caption))

# --- Telegram BOT ---
TOKEN = os.getenv( "8095758972:AAF4nFCSYh9iT5DqyoeWb4kcpwo52cswUwU" )
CHAT_ID = os.getenv("5912438442")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Kirim SEMUA caption ke Telegram
for _, caption in captions:
    payload = {"chat_id": CHAT_ID, "text": caption}
    requests.post(url, data=payload)

# --- Save all captions to file ---
output_folder = "daily_posts"
os.makedirs(output_folder, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(output_folder, f"{today}.txt")

with open(file_path, "w", encoding="utf-8") as f:
    for link, caption in captions:
        f.write(caption + "\n" + link + "\n\n")

print(f"{num_captions} captions generated, sent to Telegram, and saved in: {file_path}")
