"""Handlers package for Rubika Group Manager Bot."""

from .admin_handlers import setup_admin_handlers
from .moderation_handlers import setup_moderation_handlers
from .logging_handlers import setup_logging_handlers

__all__ = [
    "setup_admin_handlers",
    "setup_moderation_handlers",
    "setup_logging_handlers",
]


def setup_all_handlers(bot):
    """Setup all handlers for the bot."""
    setup_admin_handlers(bot)
    setup_moderation_handlers(bot)
    setup_logging_handlers(bot)
