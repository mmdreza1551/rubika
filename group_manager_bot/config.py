"""
Configuration module for Rubika Group Manager Bot.
Handles environment variables and bot settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Group configurations
GROUP_CHAT_IDS = [
    chat_id.strip()
    for chat_id in os.getenv("GROUP_CHAT_IDS", "").split(",")
    if chat_id.strip()
]

# Admin and moderator settings
ADMIN_USERS = [
    user_id.strip()
    for user_id in os.getenv("ADMIN_USERS", "").split(",")
    if user_id.strip()
]

MODERATOR_USERS = [
    user_id.strip()
    for user_id in os.getenv("MODERATOR_USERS", "").split(",")
    if user_id.strip()
]

# Banned words list
BANNED_WORDS = [
    word.strip()
    for word in os.getenv("BANNED_WORDS", "").split(",")
    if word.strip()
]

# Warning limit before action
WARNING_LIMIT = int(os.getenv("WARNING_LIMIT", "3"))

# Logging settings
LOG_FILE = os.getenv("LOG_FILE", "group_manager.log")
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() == "true"

# Message settings
AUTO_DELETE_BANNED_CONTENT = os.getenv("AUTO_DELETE_BANNED_CONTENT", "True").lower() == "true"
WARN_ON_BANNED_WORD = os.getenv("WARN_ON_BANNED_WORD", "True").lower() == "true"

# Response messages
WELCOME_MESSAGE = os.getenv(
    "WELCOME_MESSAGE",
    "خوش آمدید به گروه! لطفا قوانین را رعایت کنید."
)

BAN_MESSAGE = os.getenv(
    "BAN_MESSAGE",
    "این کاربر از گروه اخراج شد."
)

KICK_MESSAGE = os.getenv(
    "KICK_MESSAGE",
    "این کاربر از گروه حذف شد."
)

WARN_MESSAGE = os.getenv(
    "WARN_MESSAGE",
    "هشدار: {count}/{limit} هشدارهای شما استفاده شده است."
)
