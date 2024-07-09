# telegram_client.py

import requests

class TelegramClient:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}/"
    
    def send_message(self, chat_id, text):
        url = self.base_url + "sendMessage"
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(url, data=data)
        return response.json()
    
    def send_photo(self, chat_id, photo_path):
        url = self.base_url + "sendPhoto"
        files = {"photo": open(photo_path, "rb")}
        data = {"chat_id": chat_id}
        response = requests.post(url, files=files, data=data)
        return response.json()
    
    def send_video(self, chat_id, video_path):
        url = self.base_url + "sendVideo"
        files = {"video": open(video_path, "rb")}
        data = {"chat_id": chat_id}
        response = requests.post(url, files=files, data=data)
        return response.json()
