# test (temporary file)
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import load_config
from utils.telegram_notifier import send_telegram_message

config = load_config()
send_telegram_message(config['telegram_bot_token'], config['telegram_chat_id'], "Test notification!")