"""
Rubika Group Manager Bot
A comprehensive group management bot for Rubika messenger.

Features:
- Permission system (Admin, Moderator, User)
- Admin commands: /kick, /ban, /mute, /promote, /demote
- Content filtering (banned words)
- Activity logging and monitoring
- Auto-responses and moderation
- Warning system with automatic banning
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from rubpy.bot import BotClient, filters
from rubpy.bot.models import Update
import config
from handlers import setup_all_handlers


def create_bot() -> BotClient:
    """Create and configure the bot instance."""
    if not config.BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set in .env file")
    
    bot = BotClient(token=config.BOT_TOKEN)
    return bot


async def main():
    """Main entry point for the bot."""
    print("🚀 Starting Rubika Group Manager Bot...")
    
    try:
        # Create bot instance
        bot = create_bot()
        
        # Setup all handlers
        setup_all_handlers(bot)
        
        # Run the bot
        await bot.run()
    
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️  Bot stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
