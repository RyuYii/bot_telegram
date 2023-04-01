import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#config
TOKEN = os.environ.get('TOKEN', '')
# Reemplaza 'TOKEN' por el token que te dio @BotFather
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

# Manejador de comandos "/start"
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="¡Hola! Soy un bot de Telegram.")

# Manejador de eventos "new_chat_members"
def new_chat_members(update, context):
    for member in update.message.new_chat_members:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"¡Bienvenido al grupo, {member.first_name}!")


def echo(update, context):
    text = update.message.text
    if 'otaku' in text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Has mencionado la palabra clave.")

# Crea un manejador para el evento "new_chat_members"
new_chat_members_handler = MessageHandler(Filters.status_update.new_chat_members, new_chat_members)
updater.dispatcher.add_handler(new_chat_members_handler)
# Crea un comando llamado "/start"
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)
updater.start_polling()