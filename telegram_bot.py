# telegram_bot.py

import logging
import os
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import bot_token, script_directory

# Configuração do logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define um comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá! Eu sou o seu bot. Como posso ajudar?')

# Define um comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Aqui está a lista de comandos disponíveis: /start, /help, /echo <mensagem>, /executar_arquivo <nome_do_arquivo>')

# Define um comando /echo que repete a mensagem do usuário
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(' '.join(context.args))

# Define um comando /executar_arquivo para executar um arquivo Python no diretório de mídia
async def run_python_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text('Por favor, forneça o nome do arquivo Python a ser executado.')
        return
    
    file_name = context.args[0]
    file_path = os.path.join(script_directory, file_name)
    
    if not os.path.exists(file_path):
        await update.message.reply_text(f'O arquivo "{file_name}" não existe no diretório de mídia.')
        return
    
    try:
        output = subprocess.check_output(['python', file_path], stderr=subprocess.STDOUT, timeout=30)
        await update.message.reply_text(f'Output da execução de "{file_name}":\n\n{output.decode("utf-8")}')
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f'Erro ao executar "{file_name}":\n\n{e.output.decode("utf-8")}')
    except subprocess.TimeoutExpired:
        await update.message.reply_text(f'Tempo limite expirado ao executar "{file_name}".')
    except Exception as e:
        await update.message.reply_text(f'Erro inesperado ao executar "{file_name}": {str(e)}')


def main() -> None:
    # Cria o Application e passa o token do bot
    application = Application.builder().token(bot_token).build()

    # Define os comandos e os seus manipuladores
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("executar_arquivo", run_python_file))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
