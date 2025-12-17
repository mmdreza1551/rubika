"""
Custom filters for Rubika Group Manager Bot.
Provides specialized filtering functions.
"""

import re
from typing import Optional
import config


def is_command(text: str, command: str) -> bool:
    """
    Check if text is a command.
    
    Args:
        text: The message text.
        command: The command to check (without slash).
    
    Returns:
        bool: True if text is the command, False otherwise.
    """
    if not text:
        return False
    
    words = text.split()
    if not words:
        return False
    
    first_word = words[0].lower()
    return first_word == f"/{command}" or first_word == f"!{command}"


def is_banned_word(text: str) -> Optional[str]:
    """
    Check if text contains banned words.
    
    Args:
        text: The message text.
    
    Returns:
        Optional[str]: The banned word found, or None if no banned word found.
    """
    if not text:
        return None
    
    text_lower = text.lower()
    for banned_word in config.BANNED_WORDS:
        if banned_word.lower() in text_lower:
            return banned_word
    
    return None


def extract_command_args(text: str) -> list:
    """
    Extract arguments from a command string.
    
    Args:
        text: The command text.
    
    Returns:
        list: List of arguments.
    """
    if not text:
        return []
    
    parts = text.split()
    if len(parts) > 1:
        return parts[1:]
    return []


def parse_user_mention(text: str) -> Optional[str]:
    """
    Parse user mention or ID from text.
    
    Args:
        text: The text containing user mention/ID.
    
    Returns:
        Optional[str]: The user ID, or None if not found.
    """
    if not text:
        return None
    
    text = text.strip()
    
    if text.isdigit():
        return text
    
    return None


def is_admin_command(text: str) -> bool:
    """Check if text is an admin command."""
    admin_commands = ["kick", "ban", "mute", "promote", "demote", "warn"]
    for cmd in admin_commands:
        if is_command(text, cmd):
            return True
    return False
