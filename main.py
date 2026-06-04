import requests
import time
import hashlib
import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "5097274608"

STORES = {
    "FirstCry": "https://www.firstcry.com/Hot%20Wheels/0/0/113?q=as_hot+whee&asid=48299",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

last_hashes = {}

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

def get_hash(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        return hashlib.md5(r.text.encode()).hexdigest()
    except Exception:
        return None

def tracker():
    send_message("🚗 Hot Wheels Tracker Started")

    for name, url in STORES.items():
        last_hashes[name] = get_hash(url)

    while True:
        try:
            for name, url in STORES.items():
                current_hash = get_hash(url)

                if current_hash is None:
                    continue

                if current_hash != last_hashes[name]:
                    send_message(
                        f"🚨 Change detected on {name}\n{url}"
                    )
                    last_hashes[name] = current_hash

            time.sleep(300)

        except Exception as e:
            print(e)
            time.sleep(60)

@app.route("/")
def home():
    return "Hot Wheels Tracker Running"

if __name__ == "__main__":
    Thread(target=tracker, daemon=True).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
