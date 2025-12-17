"""
Admin command handlers for Rubika Group Manager Bot.
Handles commands like /kick, /ban, /mute, /promote, /demote.
"""

from rubpy.bot import filters
from rubpy.bot.models import Update
from utils.permission import PermissionManager
from utils.filters_custom import is_command, parse_user_mention, extract_command_args
from utils.helpers import format_user_mention, parse_command_args
import config


def setup_admin_handlers(bot):
    """Setup admin command handlers."""
    permission_manager = PermissionManager()
    
    @bot.on_update(filters.text & filters.chat(config.GROUP_CHAT_IDS))
    async def admin_commands_handler(client, update: Update):
        """Handle admin commands."""
        try:
            message = update.new_message
            if not message or not message.text:
                return
            
            sender_id = message.sender_id
            chat_id = update.chat_id
            text = message.text.strip()
            
            # Check if user is admin or moderator
            if not permission_manager.is_moderator_or_above(sender_id):
                return
            
            # Handle /kick command
            if is_command(text, "kick"):
                await handle_kick_command(client, update, permission_manager)
            
            # Handle /ban command
            elif is_command(text, "ban"):
                await handle_ban_command(client, update, permission_manager)
            
            # Handle /promote command
            elif is_command(text, "promote"):
                await handle_promote_command(client, update, permission_manager)
            
            # Handle /demote command
            elif is_command(text, "demote"):
                await handle_demote_command(client, update, permission_manager)
            
            # Handle /mute command
            elif is_command(text, "mute"):
                await handle_mute_command(client, update, permission_manager)
            
        except Exception as e:
            print(f"Error in admin_commands_handler: {e}")


async def handle_kick_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /kick command."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        if not args:
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ لطفا یک کاربر را مشخص کنید.\nنحوه استفاده: /kick <user_id>"
            )
            return
        
        target_user_id = args[0]
        chat_guid = update.chat_id
        
        # Note: Rubika API uses ban/unban for removal
        # We'll use ban with temporary measure
        try:
            await client.ban_group_member(chat_guid, target_user_id, action='Set')
            await client.send_message(
                chat_id=update.chat_id,
                text=f"✅ کاربر {format_user_mention(target_user_id)} از گروه اخراج شد."
            )
        except Exception as e:
            await client.send_message(
                chat_id=update.chat_id,
                text=f"❌ خطا در اخراج کاربر: {str(e)}"
            )
    
    except Exception as e:
        print(f"Error in handle_kick_command: {e}")


async def handle_ban_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /ban command."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        if not args:
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ لطفا یک کاربر را مشخص کنید.\nنحوه استفاده: /ban <user_id>"
            )
            return
        
        target_user_id = args[0]
        chat_guid = update.chat_id
        
        # Check if user is trying to ban an admin
        if permission_manager.is_admin(target_user_id):
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ نمی‌تواند یک مدیر را مسدود کنید."
            )
            return
        
        try:
            await client.ban_group_member(chat_guid, target_user_id, action='Set')
            await client.send_message(
                chat_id=update.chat_id,
                text=f"🚫 کاربر {format_user_mention(target_user_id)} مسدود شد."
            )
        except Exception as e:
            await client.send_message(
                chat_id=update.chat_id,
                text=f"❌ خطا در مسدود کردن کاربر: {str(e)}"
            )
    
    except Exception as e:
        print(f"Error in handle_ban_command: {e}")


async def handle_promote_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /promote command."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        if not args:
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ لطفا یک کاربر را مشخص کنید.\nنحوه استفاده: /promote <user_id>"
            )
            return
        
        target_user_id = args[0]
        chat_guid = update.chat_id
        
        # Check if sender is admin
        if not permission_manager.is_admin(message.sender_id):
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ فقط مدیران می‌توانند کاربران را ترفیع دهند."
            )
            return
        
        try:
            await client.set_group_admin(
                chat_guid, 
                target_user_id, 
                action='SetAdmin',
                access_list=["BanMember", "ChangeInfo", "DeleteGlobalAllMessages"]
            )
            await client.send_message(
                chat_id=update.chat_id,
                text=f"⬆️ کاربر {format_user_mention(target_user_id)} به سطح مدیر ارتقا یافت."
            )
            permission_manager.add_admin(target_user_id)
        except Exception as e:
            await client.send_message(
                chat_id=update.chat_id,
                text=f"❌ خطا در ترفیع کاربر: {str(e)}"
            )
    
    except Exception as e:
        print(f"Error in handle_promote_command: {e}")


async def handle_demote_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /demote command."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        if not args:
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ لطفا یک کاربر را مشخص کنید.\nنحوه استفاده: /demote <user_id>"
            )
            return
        
        target_user_id = args[0]
        chat_guid = update.chat_id
        
        # Check if sender is admin
        if not permission_manager.is_admin(message.sender_id):
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ فقط مدیران می‌توانند کاربران را تنزل دهند."
            )
            return
        
        try:
            await client.set_group_admin(
                chat_guid,
                target_user_id,
                action='UnsetAdmin'
            )
            await client.send_message(
                chat_id=update.chat_id,
                text=f"⬇️ کاربر {format_user_mention(target_user_id)} از سطح مدیر تنزل یافت."
            )
            permission_manager.remove_admin(target_user_id)
        except Exception as e:
            await client.send_message(
                chat_id=update.chat_id,
                text=f"❌ خطا در تنزل کاربر: {str(e)}"
            )
    
    except Exception as e:
        print(f"Error in handle_demote_command: {e}")


async def handle_mute_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /mute command."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        if not args:
            await client.send_message(
                chat_id=update.chat_id,
                text="❌ لطفا یک کاربر را مشخص کنید.\nنحوه استفاده: /mute <user_id>"
            )
            return
        
        target_user_id = args[0]
        
        await client.send_message(
            chat_id=update.chat_id,
            text=f"🔇 کاربر {format_user_mention(target_user_id)} سکوت داده شد.\n(ویژگی کامل در نسخه‌های بعدی)"
        )
    
    except Exception as e:
        print(f"Error in handle_mute_command: {e}")
