import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "5097274608"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot8728455127:AAGH3v79KQQGIurSHkVzgDr9szr88PzD-W4/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

send_message("🚗 Hot Wheels Tracker Started!")
