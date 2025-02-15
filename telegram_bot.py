import logging
from telegram import Bot


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "7422699194:AAH44omoiKdhXiKfyDbOqDNH9ZoSi9tBX-k"  
CHAT_ID = "688676895"  

async def send_telegram_notification(message):
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)
        logger.info("Telegram notification sent successfully!")
    except Exception as e:
        logger.error(f"Failed to send Telegram notification: {e}")
