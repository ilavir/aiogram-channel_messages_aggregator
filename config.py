import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DESTINATION_CHANNEL = int(os.getenv("DESTINATION_CHANNEL"))
    SOURCE_CHANNELS = [int(ch.strip()) for ch in os.getenv("SOURCE_CHANNELS").split(",")]


config = Config()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
