"""
Helper functions for Rubika Group Manager Bot.
Provides utility functions for common operations.
"""

from typing import Any, Optional, Dict


def format_user_mention(user_id: str, first_name: Optional[str] = None) -> str:
    """
    Format a user mention or name.
    
    Args:
        user_id: The user ID.
        first_name: Optional first name of the user.
    
    Returns:
        str: Formatted user mention or name.
    """
    if first_name:
        return f"{first_name} ({user_id})"
    return f"User {user_id}"


def parse_command_args(text: str, skip_command: bool = True) -> list:
    """
    Parse command arguments from text.
    
    Args:
        text: The command text.
        skip_command: Whether to skip the first word (command).
    
    Returns:
        list: List of arguments.
    """
    if not text:
        return []
    
    parts = text.split()
    if skip_command and len(parts) > 1:
        return parts[1:]
    elif not skip_command:
        return parts
    return []


def safe_get_dict_value(
    data: Dict,
    *keys,
    default: Any = None
) -> Any:
    """
    Safely get nested dictionary value.
    
    Args:
        data: The dictionary.
        *keys: The keys to traverse.
        default: Default value if key not found.
    
    Returns:
        Any: The value or default.
    """
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return default
        else:
            return default
    return current


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: The text to truncate.
        max_length: Maximum length.
    
    Returns:
        str: Truncated text with ellipsis if needed.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def format_warning_message(current_count: int, limit: int) -> str:
    """
    Format a warning message with current count and limit.
    
    Args:
        current_count: Current number of warnings.
        limit: Warning limit.
    
    Returns:
        str: Formatted warning message.
    """
    remaining = max(0, limit - current_count)
    return f"⚠️ هشدار ({current_count}/{limit}) - {remaining} هشدار مانده"


def format_timestamp() -> str:
    """
    Get formatted timestamp for logging.
    
    Returns:
        str: Formatted timestamp.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_valid_user_id(user_id: str) -> bool:
    """
    Check if string is a valid user ID format.
    
    Args:
        user_id: The user ID to validate.
    
    Returns:
        bool: True if valid format, False otherwise.
    """
    if not user_id:
        return False
    
    return user_id.isdigit() or (
        len(user_id) > 0 and all(c.isalnum() or c in "-_" for c in user_id)
    )
