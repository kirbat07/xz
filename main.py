import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, полученный у @BotFather
TOKEN = '6521929197:AAGdCGV8vyKdMnfxoLeGyxdbvyrHJUB-m5Y'

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Создание экземпляра Updater и передача токена
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Функция для удаления сообщений с ссылками
def delete_messages_with_links(update: Update, context: CallbackContext):
    message = update.message

    # Проверяем, является ли отправитель ботом
    if message.from_user.is_bot:
        # Проверяем, содержит ли сообщение ссылки
        if any(entity.type == 'url' for entity in message.entities):
            # Удаляем сообщение с ссылками
            message.delete()

# Создаем обработчик сообщений
message_handler = MessageHandler(Filters.text & (~Filters.command), delete_messages_with_links)
dispatcher.add_handler(message_handler)

# Функция для старта бота
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Бот начал работу.")

# Создаем обработчик команды /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Запускаем бота
updater.start_polling()
updater.idle()
