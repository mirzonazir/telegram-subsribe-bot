import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ApplicationBuilder, ContextTypes

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Ваш токен бота
TOKEN = '7470545997:AAHGtVEE_zLlR_4kP-ukhX5DPpsKJPOoeIg'
CHANNEL_INVITE_LINK = 'https://t.me/+5vht0SB6tl43YTMy'  # Ссылка-приглашение к вашему приватному каналу

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    logger.info(f"User {user.username} ({user.id}) started the bot.")
    
    keyboard = [
        [InlineKeyboardButton("Подписаться", url=CHANNEL_INVITE_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Пожалуйста, подпишитесь на наш канал, чтобы получить доступ к контенту.',
        reply_markup=reply_markup
    )

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Настраиваем обработчики команд
    start_handler = CommandHandler("start", start)

    application.add_handler(start_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
