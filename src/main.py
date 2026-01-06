import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# from vkbottle import Keyboard, Text
from vkbottle.bot import Bot, Message

from src.config import settings
from src.logconfig import configurate_logging, get_logger
from src.middlewares import LoggingMiddleware

bot = Bot(token=settings.vk_api_key)
bot.labeler.message_view.register_middleware(LoggingMiddleware)

configurate_logging()
logger = get_logger("main")


@bot.on.message(text="/start")
async def start_handler(message: Message):
    await message.answer("Привет! Я эхо-бот. Напиши мне что-нибудь!")


@bot.on.message()
async def echo_handler(message: Message):
    await message.answer(f"Эхо: {message.text}")


if __name__ == "__main__":
    logger.info("Bot has been started...")
    bot.run_forever()
