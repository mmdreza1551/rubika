# Rubika Group Manager Bot 🤖

یک ربات مدیریت گروه جامع و کامل برای تلگرام روبیکا با ویژگی‌های قدرتمند مدیریتی.

## ویژگی‌ها ✨

### 1. سیستم سطح دسترسی
- **Admin**: دسترسی کامل به تمام فعالیت‌های مدیریتی
- **Moderator**: دسترسی به دستورات kick, ban, warn
- **User**: کاربر عادی با محدودیت‌های سیستم

### 2. دستورات مدیریتی
- `/kick <user_id>`: اخراج کاربر از گروه
- `/ban <user_id>`: مسدود کردن کاربر (اخراج دائمی)
- `/promote <user_id>`: ترفیع کاربر به سطح مدیر (فقط Admin)
- `/demote <user_id>`: تنزل کاربر از سطح مدیر (فقط Admin)
- `/mute <user_id>`: سکوت دادن کاربر

### 3. فیلتر کلمات ممنوعه
- حذف خودکار پیام‌های حاوی کلمات ممنوعه
- هشدار کاربر با شمارش تجمعی
- مسدود کردن خودکار پس از تجاوز حد هشدار

### 4. سیستم هشدار
- هشدار تجمعی برای تخلفات
- حد قابل تنظیم برای مسدود کردن خودکار
- نمایش تعداد هشدارهای باقیمانده

### 5. لاگ و نظارت
- ثبت تمام فعالیت‌های گروه
- ثبت دستورات مدیریتی
- ثبت اقدامات مدیریتی
- ذخیره در فایل و نمایش در کنسول

## ساختار پروژه 📁

```
group_manager_bot/
├── main.py                      # نقطه شروع برنامه
├── config.py                    # تنظیمات و متغیرهای محیطی
├── requirements.txt             # پکیج‌های مورد نیاز
├── .env.example                 # نمونه فایل محیطی
├── README.md                    # این فایل
├── handlers/
│   ├── __init__.py             # بسته handlers
│   ├── admin_handlers.py        # دستورات مدیریتی
│   ├── moderation_handlers.py   # مدیریت محتوا و هشدارها
│   └── logging_handlers.py      # ثبت و نظارت فعالیت‌ها
├── utils/
│   ├── __init__.py             # بسته utils
│   ├── permission.py           # سیستم سطح دسترسی
│   ├── filters_custom.py       # فیلترهای سفارشی
│   └── helpers.py              # توابع کمکی
└── logs/                        # فایل‌های لاگ (ایجاد خودکار)
```

## نصب و راه‌اندازی 🚀

### الزامات
- Python 3.7+
- rubpy library
- python-dotenv

### مراحل نصب

1. **نصب وابستگی‌ها:**
```bash
pip install python-dotenv
```

2. **تنظیم فایل محیطی:**
```bash
cp .env.example .env
```

3. **پر کردن فایل .env:**
```bash
# تغییر دهید:
BOT_TOKEN=your_bot_token_here
GROUP_CHAT_IDS=your_group_id_1,your_group_id_2
ADMIN_USERS=your_admin_id_1,your_admin_id_2
MODERATOR_USERS=your_mod_id_1,your_mod_id_2
BANNED_WORDS=bad_word_1,bad_word_2
```

4. **اجرای ربات:**
```bash
python main.py
```

## فایل .env 🔐

```
# توکن ربات (از صفحه مدیریت ربات Rubika)
BOT_TOKEN=your_bot_token_here

# آیدی‌های گروه (از @GroupGuide یا درون‌یابی)
GROUP_CHAT_IDS=group_id_1,group_id_2

# آیدی‌های ادمین (دسترسی کامل)
ADMIN_USERS=admin_id_1,admin_id_2

# آیدی‌های مدیر (دسترسی محدود)
MODERATOR_USERS=mod_id_1,mod_id_2

# کلمات ممنوعه
BANNED_WORDS=کلمه1,کلمه2,کلمه3

# حد هشدارها
WARNING_LIMIT=3

# تنظیمات لاگ
LOG_FILE=group_manager.log
ENABLE_LOGGING=True

# تنظیمات مدیریت محتوا
AUTO_DELETE_BANNED_CONTENT=True
WARN_ON_BANNED_WORD=True

# پیام‌های سفارشی
WELCOME_MESSAGE=خوش آمدید!
BAN_MESSAGE=این کاربر اخراج شد.
```

## استفاده 💻

### دستورات برای ادمین/مدیر

#### اخراج کاربر
```
/kick 123456789
```
نتیجه: کاربر مسدود می‌شود (تا بتواند دوباره بپیوندد)

#### مسدود کردن کاربر
```
/ban 123456789
```
نتیجه: کاربر به طور دائمی مسدود می‌شود

#### ترفیع به مدیر (فقط ادمین)
```
/promote 123456789
```
نتیجه: کاربر مدیر گروه می‌شود

#### تنزل از مدیریت (فقط ادمین)
```
/demote 123456789
```
نتیجه: حذف دسترسی‌های مدیری

#### سکوت دادن (در حال توسعه)
```
/mute 123456789
```

## مدیریت خودکار ⚙️

### فیلتر کلمات ممنوعه
- وقتی کاربری پیام‌ی با کلمات ممنوعه ارسال کند:
  1. پیام حذف می‌شود
  2. یک هشدار ارسال می‌شود
  3. تعداد هشدارها افزایش می‌یابد

### سیستم هشدار
- بعد از رسیدن به حد هشدارها (`WARNING_LIMIT`):
  - کاربر مسدود می‌شود
  - هشدارهای کاربر ریست می‌شوند

## لاگ‌ها 📊

لاگ‌های فعالیت در پوشه `logs/` ذخیره می‌شوند:
- نام فایل: `group_manager.log`
- فرمت: `datetime - source - level - message`
- سطح: INFO, WARNING, ERROR

## کلاس‌ها و توابع 🔧

### Permission Manager
```python
from utils.permission import PermissionManager

pm = PermissionManager()
pm.is_admin(user_id)          # بررسی ادمین
pm.is_moderator(user_id)      # بررسی مدیر
pm.add_admin(user_id)         # اضافه کردن ادمین
pm.remove_admin(user_id)      # حذف ادمین
```

### Custom Filters
```python
from utils.filters_custom import is_command, is_banned_word

is_command(text, "kick")      # بررسی دستور
is_banned_word(text)          # بررسی کلمات ممنوعه
```

### Helpers
```python
from utils.helpers import format_user_mention, parse_command_args

format_user_mention(user_id)  # فرمت کردن نام کاربر
parse_command_args(text)      # پارس آرگومان‌های دستور
```

## مثال‌های پیشرفته 🎓

### استفاده سفارشی
```python
from main import create_bot
import asyncio

async def custom_bot():
    bot = create_bot()
    
    # دستورات سفارشی خود را اضافه کنید
    @bot.on_update(filters.text)
    async def my_handler(client, update):
        # کدهای سفارشی شما
        pass
    
    await bot.run()

asyncio.run(custom_bot())
```

### تغییر تنظیمات در زمان اجرا
```python
import config

# تغییر حد هشدار
config.WARNING_LIMIT = 5

# اضافه کردن کلمات ممنوعه
config.BANNED_WORDS.append("new_bad_word")
```

## مشکلات و حل‌های احتمالی 🐛

### مشکل: "BOT_TOKEN not set"
**حل**: مطمئن شوید فایل `.env` موجود است و حاوی `BOT_TOKEN` صحیح است

### مشکل: دستورات کار نمی‌کنند
**حل**: 
- مطمئن شوید کاربر ادمین یا مدیر است
- تنظیمات GROUP_CHAT_IDS را بررسی کنید

### مشکل: لاگ‌ها ذخیره نمی‌شوند
**حل**: 
- `ENABLE_LOGGING=True` را در .env تنظیم کنید
- پوشه `logs/` دسترسی نوشتن دارد

## توسعه و گسترش 🚀

ربات به راحتی قابل توسعه است:

1. **اضافه کردن دستور جدید:**
   - در `admin_handlers.py` تابع جدید اضافه کنید
   - Handler جدید را ثبت کنید

2. **فیلترهای سفارشی:**
   - در `utils/filters_custom.py` تابع جدید بنویسید
   - در handler‌ها استفاده کنید

3. **ذخیره داده‌ها:**
   - تغییر `user_warnings` به دیتابیس (SQLite, MongoDB, etc.)
   - ذخیره تاریخچه اقدامات مدیریتی

## مجوز 📄

این پروژه در قالب نمونه سیستم rubpy ارائه شده است.

## پشتیبانی و تماس 📞

برای مشکلات یا پیشنهادات:
- بررسی مستندات: [rubpy documentation]
- ایجاد Issue در repository

---

**نسخه**: 1.0.0  
**آخرین بروزرسانی**: 2024
