import json
import random

with open("config.json") as f:
    data = json.load(f)

links = data["links"]
promo = random.choice(links)

print("🔥 Promo hari ini:", promo)
