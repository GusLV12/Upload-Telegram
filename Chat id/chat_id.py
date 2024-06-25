import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
BOT_TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Tu chat ID es: {chat_id}")
    print(f"Tu chat ID es: {chat_id}")

async def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"El chat ID es: {chat_id}")
    print(f"El chat ID es: {chat_id}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_chat_id))

    application.run_polling()

if __name__ == '__main__':
    main()
