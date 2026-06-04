import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "5097274608"

URL = "https://www.firstcry.com/Hot%20Wheels/0/0/113?q=as_hot+whee&asid=48299"

last_found = False

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

while True:
    try:
        page = requests.get(URL, timeout=20).text.lower()

        found = (
            "die cast toy car" in page or
            "hot wheels" in page
        )

        if found and not last_found:
            send_message("🚗 Hot Wheels found on FirstCry!")

        last_found = found

    except Exception as e:
        print(e)

    time.sleep(300)
