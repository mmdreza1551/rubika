# راهنمای توسعه و گسترش 👨‍💻

## ساختار پروژه

```
group_manager_bot/
├── main.py                      # نقطه شروع برنامه
├── config.py                    # تنظیمات و متغیرهای محیطی
├── requirements.txt             # پکیج‌های مورد نیاز
├── .env.example                 # نمونه متغیرهای محیطی
├── README.md                    # راهنمای استفاده
├── USAGE.md                     # دستورالعمل دستورات
├── INSTALLATION.md              # راهنمای نصب
├── DEVELOPMENT.md               # این فایل
├── handlers/                    # دستورات و handlers
│   ├── __init__.py
│   ├── admin_handlers.py        # دستورات مدیریتی
│   ├── moderation_handlers.py   # مدیریت محتوا و هشدارها
│   └── logging_handlers.py      # ثبت و نظارت
├── utils/                       # توابع کمکی
│   ├── __init__.py
│   ├── permission.py            # سیستم سطح دسترسی
│   ├── filters_custom.py        # فیلترهای سفارشی
│   └── helpers.py               # توابع کمکی
└── logs/                        # فایل‌های لاگ (خودکار ایجاد می‌شود)
```

## اضافه کردن دستور جدید

### مثال: دستور /info

```python
# در handlers/admin_handlers.py، اضافه کنید:

async def handle_info_command(client, update: Update, permission_manager: PermissionManager):
    """Handle /info command to get group/user info."""
    try:
        message = update.new_message
        args = extract_command_args(message.text)
        
        await client.send_message(
            chat_id=update.chat_id,
            text="📊 اطلاعات گروه:\n"
                 f"Chat ID: {update.chat_id}\n"
                 f"کل کاربران: (از طریق API)\n"
                 f"مدیران: {len(permission_manager.admin_users)}"
        )
    except Exception as e:
        print(f"Error in handle_info_command: {e}")
```

سپس در تابع `admin_commands_handler`:

```python
elif is_command(text, "info"):
    await handle_info_command(client, update, permission_manager)
```

## اضافه کردن Filter سفارشی

### مثال: فیلتر برای لینک‌های خارجی

```python
# در utils/filters_custom.py:

import re

def has_external_link(text: str) -> bool:
    """Check if text contains external links."""
    url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'
    return bool(re.search(url_pattern, text))
```

سپس در `moderation_handlers.py`:

```python
from utils.filters_custom import has_external_link

# در content_filter_handler:
if has_external_link(text):
    await client.delete_messages(...)
```

## اضافه کردن Handler جدید

### مثال: Handler برای Reply Messages

```python
# یک فایل جدید ایجاد کنید: handlers/reaction_handlers.py

from rubpy.bot import filters
from rubpy.bot.models import Update
import config

def setup_reaction_handlers(bot):
    """Setup handlers for message reactions."""
    
    @bot.on_update(filters.chat(config.GROUP_CHAT_IDS) & filters.text)
    async def auto_react_handler(client, update: Update):
        """Auto-react to certain keywords."""
        try:
            message = update.new_message
            text = message.text.lower() if message.text else ""
            
            # React to "hello"
            if "سلام" in text:
                await client.send_message(
                    chat_id=update.chat_id,
                    text="👋 سلام!",
                    reply_to_message_id=message.message_id
                )
        except Exception as e:
            print(f"Error in auto_react_handler: {e}")
```

سپس در `handlers/__init__.py`:

```python
from .reaction_handlers import setup_reaction_handlers

def setup_all_handlers(bot):
    """Setup all handlers for the bot."""
    setup_admin_handlers(bot)
    setup_moderation_handlers(bot)
    setup_logging_handlers(bot)
    setup_reaction_handlers(bot)  # اضافه کنید
```

## استفاده از دیتابیس

### مثال: ذخیره تاریخچه تغییرات

```python
# نصب sqlite3 (معمولاً داخل Python است)
import sqlite3

class HistoryDB:
    def __init__(self, db_path: str = "history.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_actions (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                chat_id TEXT,
                action TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                details TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def log_action(self, user_id: str, chat_id: str, action: str, details: str = ""):
        """Log a user action."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO user_actions (user_id, chat_id, action, details)
            VALUES (?, ?, ?, ?)
        """, (user_id, chat_id, action, details))
        
        conn.commit()
        conn.close()
    
    def get_user_history(self, user_id: str, limit: int = 10):
        """Get user action history."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT action, details, timestamp FROM user_actions
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        """, (user_id, limit))
        
        results = cursor.fetchall()
        conn.close()
        return results

# استفاده:
db = HistoryDB()
db.log_action("user123", "chat456", "sent_message", "Regular message")
history = db.get_user_history("user123")
```

## Middleware سفارشی

### مثال: Rate Limiting

```python
# در main.py، قبل از setup_all_handlers:

from time import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests: int = 5, window: int = 10):
        self.max_requests = max_requests
        self.window = window  # seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, user_id: str) -> bool:
        """Check if user is allowed to send another request."""
        now = time()
        # Clean old requests
        self.requests[user_id] = [
            t for t in self.requests[user_id]
            if now - t < self.window
        ]
        
        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(now)
            return True
        return False

rate_limiter = RateLimiter()

async def main():
    bot = create_bot()
    
    @bot.middleware()
    async def rate_limit_middleware(client, update, call_next):
        """Middleware to prevent spam."""
        user_id = update.new_message.sender_id if update.new_message else None
        
        if user_id and not rate_limiter.is_allowed(user_id):
            print(f"Rate limit exceeded for {user_id}")
            return
        
        await call_next()
    
    setup_all_handlers(bot)
    await bot.run()
```

## تست کردن

### Unit Test

```python
# ایجاد فایل: test_bot.py

import pytest
from utils.permission import PermissionManager, PermissionLevel
from utils.filters_custom import is_command, is_banned_word

def test_permission_manager():
    pm = PermissionManager()
    
    # Test admin
    assert pm.is_admin("admin_id") == False
    pm.add_admin("admin_id")
    assert pm.is_admin("admin_id") == True

def test_is_command():
    assert is_command("/kick 123", "kick") == True
    assert is_command("!kick 123", "kick") == True
    assert is_command("kick 123", "kick") == False

def test_banned_word():
    from config import BANNED_WORDS
    # اضافه کنید: BANNED_WORDS = ["bad"]
    assert is_banned_word("this is bad") == "bad"
    assert is_banned_word("good message") == None

# اجرا:
# pytest test_bot.py -v
```

## Logging بهتر

### تنظیم Logger سفارشی

```python
# در utils/helpers.py:

import logging
from pathlib import Path

def create_logger(name: str, log_file: str = "logs/bot.log") -> logging.Logger:
    """Create a configured logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Create logs directory
    Path("logs").mkdir(exist_ok=True)
    
    # File handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

# استفاده:
logger = create_logger("admin_commands")
logger.info("Admin command executed")
```

## بهتری عملکرد

### استفاده از Caching

```python
# در utils/helpers.py:

from functools import lru_cache
from datetime import datetime, timedelta

class TTLCache:
    def __init__(self, ttl_seconds: int = 3600):
        self.cache = {}
        self.ttl = ttl_seconds
    
    def get(self, key: str):
        """Get value if not expired."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            if datetime.now() - timestamp < timedelta(seconds=self.ttl):
                return value
            else:
                del self.cache[key]
        return None
    
    def set(self, key: str, value):
        """Set value with timestamp."""
        self.cache[key] = (value, datetime.now())
    
    def clear(self):
        """Clear cache."""
        self.cache.clear()

# استفاده:
user_cache = TTLCache(ttl_seconds=300)
```

## Deployment

### استفاده از Docker Compose

```yaml
# docker-compose.yml

version: '3.8'

services:
  group-manager-bot:
    build: .
    restart: always
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
      - GROUP_CHAT_IDS=${GROUP_CHAT_IDS}
      - ADMIN_USERS=${ADMIN_USERS}
      - MODERATOR_USERS=${MODERATOR_USERS}
      - BANNED_WORDS=${BANNED_WORDS}
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    networks:
      - group_manager_net

networks:
  group_manager_net:
    driver: bridge
```

### استفاده با systemd

```ini
# /etc/systemd/system/group-manager-bot.service

[Unit]
Description=Rubika Group Manager Bot
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/group_manager_bot
ExecStart=/usr/bin/python3 /opt/group_manager_bot/main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

## Best Practices

1. **Error Handling**: همیشه try/except استفاده کنید
2. **Logging**: تمام فعالیت‌های مهم را log کنید
3. **Configuration**: تمام settings را در config.py قرار دهید
4. **Type Hints**: از type hints در توابع استفاده کنید
5. **Documentation**: کد خود را مستند کنید
6. **Testing**: unit tests بنویسید
7. **Security**: هرگز secrets را hardcode نکنید

---

**نسخه:** 1.0.0  
**آخر بروزرسانی:** 2024
