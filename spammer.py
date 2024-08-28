import os

try:
    import art
except ImportError:
    os.system('pip install art')
    import art

nan = "FREAKXD7"
lo = art.text2art(nan)
print(lo)

import requests

print("Lütfen dilinizi seçin / Please select your language:")
print("Türkçe İçin 1")
print("For English 2")
language_choice = input("Seçiminiz / Your choice: ")

if language_choice == "1":
    username_prompt = "Webhook Botu Adınız: "
    message_prompt = "Mesajınız: "
    webhook_prompt = "Webhook URL: "
    times_prompt = "Kaç Mesaj Atacaksınız: "
elif language_choice == "2":
    username_prompt = "Your Webhook Bot Name: "
    message_prompt = "Your Message: "
    webhook_prompt = "Webhook URL: "
    times_prompt = "How Many Messages to Send: "
else:
    print("Geçersiz seçim / Invalid choice!")
    exit()

def send_discord_message(webhook_url, message, username, times):
    data = {
        "content": message,
        "username": username
    }

    for _ in range(times):
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"Mesaj başarıyla gönderildi! / Message sent successfully!")
        else:
            print(f"Mesaj gönderilirken hata oluştu: {response.status_code} / Error occurred: {response.status_code}")

username = input(username_prompt)
message = input(message_prompt)
webhook_url = input(webhook_prompt)
times = int(input(times_prompt))

send_discord_message(webhook_url, message, username, times)
