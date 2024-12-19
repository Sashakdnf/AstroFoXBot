import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Установи токен Telegram
TELEGRAM_TOKEN = "7690113291:AAHlZ_ge2f8_pJdEiKUajvzii7LbYXnC7-Y"

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Генерация ответа
def generate_answer():
    return random.choice(["Да", "Нет"])

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Задай мне любой вопрос, и я отвечу 'Да' или 'Нет'."
    )

# Ответ на текстовые сообщения
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = generate_answer()
    await update.message.reply_text(answer)

# Основной блок
def main():
    try:
        application = Application.builder().token(TELEGRAM_TOKEN).build()

        # Обработчики
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

        # Запуск бота
        logger.info("Бот запущен и готов отвечать на вопросы.")
        application.run_polling()
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    main()
