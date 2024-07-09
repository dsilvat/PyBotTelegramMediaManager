PYBOTTELEGRAMMEDIAMANAGER

O PyBotTelegramMediaManager é um bot Telegram desenvolvido em Python que permite enviar mensagens para um grupo no Telegram, incluindo textos, imagens e vídeos. O projeto segue uma estrutura MVC básica para organizar o código de forma modular.

FUNCIONALIDADES

Envio de Mensagens: Permite enviar mensagens de texto para um grupo no Telegram.
Envio de Imagens e Vídeos: Suporta o envio de arquivos de mídia, como imagens e vídeos, para o grupo.
Comandos Definidos: Implementa comandos como /start, /help e /echo para interagir com os usuários do grupo.
CONFIGURAÇÃO

Token do Bot: Configure o token do seu bot Telegram no arquivo config.py.

bot_token = 'seu_token_aqui'

ID do Grupo: Defina o ID do grupo Telegram para onde as mensagens serão enviadas.

group_id = 'seu_group_id_aqui'

Diretório de Mídia: Configure o diretório onde os arquivos de mídia serão armazenados no arquivo config.py.

media_directory = '/caminho/para/seu/diretorio_de_midia/'

COMO USAR

Clone o repositório:

https://github.com/dsilvat/PyBotTelegramMediaManager.git
cd py-bot-telegram-media-manager

Instale as dependências:

pip install -r requirements.txt

Configure o token do bot, o ID do grupo e o diretório de mídia no arquivo config.py.

Execute o bot:

python telegram_bot.py

Interaja com o bot no Telegram usando os comandos disponíveis (/start, /help, /echo).



---------------------------------------------------------------------------------------


Exemplo de Uso em Outro Script Python
Suponha que você tenha um script meu_script.py no mesmo diretório onde está o diretório do projeto py-bot-telegram-media-manager. Você pode importar e usar as funcionalidades do bot Telegram da seguinte maneira:


# Importe as classes e funções necessárias do seu projeto
from telegram_bot_controller import TelegramBotController

# Função para enviar uma mensagem para o grupo no Telegram
def enviar_mensagem_no_telegram(mensagem):
    # Crie uma instância do controlador do bot Telegram
    bot_controller = TelegramBotController()

    # Envie a mensagem para o grupo definido no projeto
    bot_controller.enviar_mensagem(mensagem)

# Exemplo de uso
if __name__ == "__main__":
    # Mensagem a ser enviada para o grupo no Telegram
    mensagem_para_enviar = "Olá! Esta é uma mensagem de teste."

    # Chame a função para enviar a mensagem
    enviar_mensagem_no_telegram(mensagem_para_enviar)