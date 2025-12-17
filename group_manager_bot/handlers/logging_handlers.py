"""
Logging and monitoring handlers for Rubika Group Manager Bot.
Tracks group activities and changes.
"""

from rubpy.bot import filters
from rubpy.bot.models import Update
import config
from utils.helpers import format_timestamp, format_user_mention
import logging
from pathlib import Path
from typing import Optional


# Setup logging
def setup_logger():
    """Setup logging configuration."""
    if not config.ENABLE_LOGGING:
        return None
    
    logger = logging.getLogger("group_manager_bot")
    logger.setLevel(logging.INFO)
    
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # File handler
    file_handler = logging.FileHandler(log_dir / config.LOG_FILE)
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


logger = setup_logger()


def setup_logging_handlers(bot):
    """Setup logging and monitoring handlers."""
    
    @bot.on_update(filters.chat(config.GROUP_CHAT_IDS))
    async def activity_logger(client, update: Update):
        """Log all group activities."""
        try:
            if not logger:
                return
            
            message = update.new_message
            if not message:
                return
            
            sender_id = message.sender_id
            chat_id = update.chat_id
            text = message.text if message.text else "[Non-text content]"
            
            # Log message
            log_message = f"Chat: {chat_id} | Sender: {sender_id} | Text: {text[:100]}"
            logger.info(log_message)
        
        except Exception as e:
            if logger:
                logger.error(f"Error in activity_logger: {e}")
    
    @bot.on_start()
    async def startup_log(client):
        """Log bot startup."""
        try:
            if logger:
                logger.info("=" * 50)
                logger.info("Group Manager Bot Started")
                logger.info(f"Timestamp: {format_timestamp()}")
                logger.info(f"Configured Groups: {config.GROUP_CHAT_IDS}")
                logger.info(f"Banned Words Count: {len(config.BANNED_WORDS)}")
                logger.info("=" * 50)
            
            print("✅ Bot started successfully!")
            print(f"📍 Monitoring {len(config.GROUP_CHAT_IDS)} group(s)")
        
        except Exception as e:
            if logger:
                logger.error(f"Error in startup_log: {e}")
            print(f"❌ Error during startup: {e}")


def log_command_execution(command: str, user_id: str, details: str = ""):
    """Log command execution."""
    if not logger:
        return
    
    log_msg = f"Command: {command} | User: {user_id}"
    if details:
        log_msg += f" | Details: {details}"
    
    logger.info(log_msg)


def log_moderation_action(action: str, target_user: str, reason: str = ""):
    """Log moderation action."""
    if not logger:
        return
    
    log_msg = f"Moderation Action: {action} | Target User: {target_user}"
    if reason:
        log_msg += f" | Reason: {reason}"
    
    logger.warning(log_msg)


def log_warning_issued(user_id: str, current_count: int, limit: int):
    """Log warning issued to user."""
    if not logger:
        return
    
    logger.warning(
        f"Warning issued to {user_id}: {current_count}/{limit}"
    )


def log_error(error_type: str, error_msg: str, context: str = ""):
    """Log error message."""
    if not logger:
        return
    
    log_msg = f"Error Type: {error_type} | Message: {error_msg}"
    if context:
        log_msg += f" | Context: {context}"
    
    logger.error(log_msg)
