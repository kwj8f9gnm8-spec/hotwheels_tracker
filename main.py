import requests
import time
import hashlib
import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = "8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4"
CHAT_ID = "5097274608"

STORES = {
"FirstCry": "https://www.firstcry.com/Hot%20Wheels/0/0/113?q=as_hot+whee&asid=48299"
}

HEADERS = {
"User-Agent": "Mozilla/5.0"
}

last_hashes = {}

def send_message(text):
try:
r = requests.post(
f"https://api.telegram.org/bot8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4/sendMessage",
data={
"chat_id": CHAT_ID,
"text": text
},
timeout=30
)
print(r.text)
except Exception as e:
print("Telegram Error:", e)

def get_hash(url):
try:
r = requests.get(url, headers=HEADERS, timeout=30)
return hashlib.md5(r.text.encode()).hexdigest()
except Exception as e:
print("Request Error:", e)
return None

def tracker():
print("Tracker Started")
send_message("🚗 Hot Wheels Tracker Started")

```
for name, url in STORES.items():
    last_hashes[name] = get_hash(url)

while True:
    try:
        print(f"Checking stores at {time.ctime()}")

        for name, url in STORES.items():
            current_hash = get_hash(url)

            if current_hash is None:
                continue

            if current_hash != last_hashes[name]:
                send_message(
                    f"🚨 Change detected on {name}\n{url}"
                )

                print(f"Change detected on {name}")

                last_hashes[name] = current_hash

        time.sleep(60)

    except Exception as e:
        print("Loop Error:", e)
        time.sleep(60)
```

@app.route("/")
def home():
return "Hot Wheels Tracker Running"

if __name__ == "__main__":
Thread(target=tracker, daemon=True).start()

```
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
```
