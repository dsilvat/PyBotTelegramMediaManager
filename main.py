# main.py

from telegram_bot_controller import TelegramBotController
from config import bot_token, group_chat_id, media_directory

def main():
    bot_controller = TelegramBotController(bot_token)
    
    # Exemplo de envio de mensagem
    bot_controller.send_message(group_chat_id, "Olá, grupo! Esta é uma mensagem de teste.")
    
    # Exemplo de envio de imagem
    #image_path = "caminho/para/sua/imagem.jpg"
    #bot_controller.send_image(group_chat_id, image_path)
    
    # Exemplo de envio de vídeo
    #video_path = "caminho/para/seu/video.mp4"
    #bot_controller.send_video(group_chat_id, video_path)

if __name__ == "__main__":
    main()
