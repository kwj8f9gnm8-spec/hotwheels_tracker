import requests
import time
import hashlib
BOT_TOKEN = "8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4"
CHAT_ID = "5097274608"
STORES = {
    "FirstCry": "https://www.firstcry.com/Hot%20Wheels/0/0/113?q=as_hot+whee&asid=48299",
    "Blinkit": "https://blinkit.com/s/?q=hot%20wheels",
    "Instamart": "https://www.swiggy.com/stores/instamart/search?custom_back=true&query=Hot+Wheels",
    "Zepto": "https://www.zepto.com/search?query=Hot+wheels",
    "BigBasket": "https://www.bigbasket.com/ps/?q=hotwheels&nc=as"
}
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
last_hashes = {}
def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4/sendMessage",
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
