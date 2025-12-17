"""
Permission system for Rubika Group Manager Bot.
Manages user roles and access levels.
"""

from enum import Enum
from typing import Optional
import config


class PermissionLevel(Enum):
    """Permission levels for group members."""
    USER = 1
    MODERATOR = 2
    ADMIN = 3
    BOT_OWNER = 4


class PermissionManager:
    """Manages permissions for group members."""
    
    def __init__(self):
        self.admin_users = set(config.ADMIN_USERS)
        self.moderator_users = set(config.MODERATOR_USERS)
    
    def get_permission_level(self, user_id: str) -> PermissionLevel:
        """
        Get the permission level of a user.
        
        Args:
            user_id: The ID of the user.
        
        Returns:
            PermissionLevel: The permission level of the user.
        """
        if user_id in self.admin_users:
            return PermissionLevel.ADMIN
        elif user_id in self.moderator_users:
            return PermissionLevel.MODERATOR
        else:
            return PermissionLevel.USER
    
    def is_admin(self, user_id: str) -> bool:
        """Check if user is admin."""
        return user_id in self.admin_users
    
    def is_moderator(self, user_id: str) -> bool:
        """Check if user is moderator."""
        return user_id in self.moderator_users
    
    def is_admin_or_above(self, user_id: str) -> bool:
        """Check if user has admin privileges or above."""
        return self.get_permission_level(user_id).value >= PermissionLevel.ADMIN.value
    
    def is_moderator_or_above(self, user_id: str) -> bool:
        """Check if user has moderator privileges or above."""
        return self.get_permission_level(user_id).value >= PermissionLevel.MODERATOR.value
    
    def add_admin(self, user_id: str) -> bool:
        """Add a user as admin."""
        if user_id not in self.admin_users:
            self.admin_users.add(user_id)
            return True
        return False
    
    def remove_admin(self, user_id: str) -> bool:
        """Remove admin status from a user."""
        if user_id in self.admin_users:
            self.admin_users.discard(user_id)
            return True
        return False
    
    def add_moderator(self, user_id: str) -> bool:
        """Add a user as moderator."""
        if user_id not in self.moderator_users:
            self.moderator_users.add(user_id)
            return True
        return False
    
    def remove_moderator(self, user_id: str) -> bool:
        """Remove moderator status from a user."""
        if user_id in self.moderator_users:
            self.moderator_users.discard(user_id)
            return True
        return False
