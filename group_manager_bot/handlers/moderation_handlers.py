"""
Moderation handlers for Rubika Group Manager Bot.
Handles content filtering, banned words, and user warnings.
"""

from rubpy.bot import filters
from rubpy.bot.models import Update
from utils.permission import PermissionManager
from utils.filters_custom import is_banned_word
from utils.helpers import format_user_mention, format_warning_message
import config
from typing import Dict, Optional


# In-memory storage for warnings (in production, use a database)
user_warnings: Dict[str, int] = {}


def setup_moderation_handlers(bot):
    """Setup moderation handlers."""
    permission_manager = PermissionManager()
    
    @bot.on_update(filters.text & filters.chat(config.GROUP_CHAT_IDS))
    async def content_filter_handler(client, update: Update):
        """Filter banned words and content."""
        try:
            message = update.new_message
            if not message or not message.text:
                return
            
            sender_id = message.sender_id
            chat_id = update.chat_id
            text = message.text.strip()
            
            # Skip if sender is admin
            if permission_manager.is_admin(sender_id):
                return
            
            # Check for banned words
            if config.BANNED_WORDS:
                banned_word = is_banned_word(text)
                if banned_word:
                    await handle_banned_word(
                        client, 
                        update, 
                        permission_manager,
                        banned_word
                    )
        
        except Exception as e:
            print(f"Error in content_filter_handler: {e}")


async def handle_banned_word(client, update: Update, permission_manager: PermissionManager, banned_word: str):
    """Handle banned word detection."""
    try:
        message = update.new_message
        sender_id = message.sender_id
        chat_id = update.chat_id
        
        # Increment warning count
        current_count = user_warnings.get(sender_id, 0) + 1
        user_warnings[sender_id] = current_count
        
        # Delete the message if auto-delete is enabled
        if config.AUTO_DELETE_BANNED_CONTENT:
            try:
                await client.delete_messages(
                    object_guid=chat_id,
                    message_ids=message.message_id,
                    type='Global'
                )
            except Exception as e:
                print(f"Error deleting message: {e}")
        
        # Send warning message
        if config.WARN_ON_BANNED_WORD:
            warning_msg = format_warning_message(current_count, config.WARNING_LIMIT)
            await client.send_message(
                chat_id=chat_id,
                text=f"{format_user_mention(sender_id)}\n⚠️ کلمه ممنوع '{banned_word}' استفاده نشود!\n{warning_msg}"
            )
        
        # Check if warning limit reached
        if current_count >= config.WARNING_LIMIT:
            await handle_warning_limit_exceeded(client, update, permission_manager)
    
    except Exception as e:
        print(f"Error in handle_banned_word: {e}")


async def handle_warning_limit_exceeded(client, update: Update, permission_manager: PermissionManager):
    """Handle when a user exceeds warning limit."""
    try:
        message = update.new_message
        sender_id = message.sender_id
        chat_id = update.chat_id
        
        # Ban the user
        try:
            await client.ban_group_member(chat_id, sender_id, action='Set')
            await client.send_message(
                chat_id=chat_id,
                text=f"🚫 کاربر {format_user_mention(sender_id)} به دلیل تکرار نقض قوانین مسدود شد."
            )
            # Reset warnings
            user_warnings[sender_id] = 0
        except Exception as e:
            print(f"Error banning user: {e}")
    
    except Exception as e:
        print(f"Error in handle_warning_limit_exceeded: {e}")


def get_user_warnings(user_id: str) -> int:
    """Get current warning count for a user."""
    return user_warnings.get(user_id, 0)


def reset_user_warnings(user_id: str):
    """Reset warnings for a user."""
    user_warnings[user_id] = 0


def clear_all_warnings():
    """Clear all warnings (useful for bot restart)."""
    global user_warnings
    user_warnings.clear()
