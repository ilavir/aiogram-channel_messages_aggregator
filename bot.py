import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import config

logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.channel_post()
async def forward_channel_post(message: Message):
    if message.chat.id in config.SOURCE_CHANNELS:
        channel_name = message.chat.title or f"Channel {message.chat.id}"
        try:
            await bot.send_message(
                config.DESTINATION_CHANNEL,
                f"📢 From: {channel_name}\n\n{message.text or '[Media/File]'}"
            )
            logger.info(f"Forwarded message from {channel_name} to destination channel")
        except Exception as e:
            logger.error(f"Failed to forward message from {channel_name}: {e}")


@dp.message()
async def forward_message(message: Message):
    if message.chat.id in config.SOURCE_CHANNELS:
        channel_name = message.chat.title or f"Channel {message.chat.id}"
        try:
            await bot.send_message(
                config.DESTINATION_CHANNEL,
                f"📢 From: {channel_name}\n\n{message.text or '[Media/File]'}"
            )
            logger.info(f"Forwarded message from {channel_name} to destination channel")
        except Exception as e:
            logger.error(f"Failed to forward message from {channel_name}: {e}")


async def main():
    logger.info("Starting bot...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot stopped with error: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
