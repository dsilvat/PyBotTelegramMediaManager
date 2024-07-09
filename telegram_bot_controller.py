# telegram_bot_controller.py

from telegram_client import TelegramClient

class TelegramBotController:
    def __init__(self, bot_token):
        self.telegram_client = TelegramClient(bot_token)
    
    def start(self):
        # Implemente a inicialização do bot aqui, se necessário
        pass
    
    def send_message(self, group_chat_id, text):
        self.telegram_client.send_message(group_chat_id, text)
    
    def send_image(self, group_chat_id, image_path):
        self.telegram_client.send_photo(group_chat_id, image_path)
    
    def send_video(self, group_chat_id, video_path):
        self.telegram_client.send_video(group_chat_id, video_path)
