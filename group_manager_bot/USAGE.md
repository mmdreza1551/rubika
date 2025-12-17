# دستورالعمل استفاده 📖

راهنمای کامل استفاده از ربات مدیریت گروه روبیکا

## فهرست محتوا
1. [راه‌اندازی](#راه‌اندازی)
2. [دستورات](#دستورات)
3. [تنظیمات](#تنظیمات)
4. [نکات ایمنی](#نکات-ایمنی)
5. [خطاهای رایج](#خطاهای-رایج)

## راه‌اندازی

### مرحله 1: تهیه Token
1. به صفحه [مدیریت Bot Rubika](https://rubika.ir) بروید
2. یک Bot جدید ایجاد کنید
3. Token را کپی کنید

### مرحله 2: تنظیم فایل .env
```bash
# کپی کردن فایل نمونه
cp .env.example .env

# ویرایش فایل
nano .env
```

### مرحله 3: یافتن Group Chat IDs
برای یافتن Chat ID گروه‌های خود:

**روش 1: از داخل گروه**
- پیام: `@GroupGuide get_my_id`
- ID شما نمایش داده خواهد شد

**روش 2: استفاده از API**
```python
from rubpy import Client
import asyncio

async def get_group_id():
    client = Client()
    # دریافت لیست گروه‌ها
    # ...
    
asyncio.run(get_group_id())
```

### مرحله 4: اجرا
```bash
python main.py
```

## دستورات

### دستورات Admin

#### /kick
اخراج کاربر از گروه (می‌تواند دوباره بپیوندد)

```
/kick 123456789
```

**شرایط:**
- فرستنده باید Admin یا Moderator باشد
- نمی‌تواند Admins دیگر را kick کند

**نتیجه:**
```
✅ کاربر User 123456789 از گروه اخراج شد.
```

#### /ban
مسدود کردن دائمی کاربر

```
/ban 123456789
```

**شرایط:**
- فرستنده باید Admin یا Moderator باشد
- نمی‌تواند Admins را ban کند

**نتیجه:**
```
🚫 کاربر User 123456789 مسدود شد.
```

#### /promote
ترفیع کاربر به سطح مدیر (فقط Admin)

```
/promote 123456789
```

**شرایط:**
- فرستنده **باید** Admin باشد
- کاربر مدیر نباشد

**نتیجه:**
```
⬆️ کاربر User 123456789 به سطح مدیر ارتقا یافت.
```

**دسترسی‌های مدیر:**
- BanMember
- ChangeInfo
- DeleteGlobalAllMessages

#### /demote
تنزل مدیر (فقط Admin)

```
/demote 123456789
```

**شرایط:**
- فرستنده **باید** Admin باشد
- کاربر مدیر باشد

**نتیجه:**
```
⬇️ کاربر User 123456789 از سطح مدیر تنزل یافت.
```

#### /mute
سکوت دادن کاربر (در حال توسعه)

```
/mute 123456789
```

> **نکته:** این ویژگی در نسخه فعلی فقط پیام الطمیننه می‌فرستد.

## تنظیمات

### تنظیمات اساسی

#### GROUP_CHAT_IDS
```env
GROUP_CHAT_IDS=group1_id,group2_id,group3_id
```
گروه‌های زیر نظارت ربات (جداشده با کاما)

#### ADMIN_USERS
```env
ADMIN_USERS=admin1_id,admin2_id
```
آیدی ادمین‌ها (دسترسی کامل)

#### MODERATOR_USERS
```env
MODERATOR_USERS=mod1_id,mod2_id
```
آیدی مدیران (دسترسی محدود)

### تنظیمات Content Filtering

#### BANNED_WORDS
```env
BANNED_WORDS=کلمه1,کلمه2,کلمه3,bad_english_word
```
کلمات ممنوعه (حساس به بزرگ/کوچک حروف نیست)

#### WARNING_LIMIT
```env
WARNING_LIMIT=3
```
تعداد هشدارها قبل از ban خودکار

#### AUTO_DELETE_BANNED_CONTENT
```env
AUTO_DELETE_BANNED_CONTENT=True
```
حذف خودکار پیام‌های حاوی کلمات ممنوعه

#### WARN_ON_BANNED_WORD
```env
WARN_ON_BANNED_WORD=True
```
ارسال پیام هشدار برای کلمات ممنوعه

### تنظیمات Logging

#### ENABLE_LOGGING
```env
ENABLE_LOGGING=True
```
فعال/غیرفعال کردن لاگ‌های فعالیت

#### LOG_FILE
```env
LOG_FILE=group_manager.log
```
نام فایل لاگ

### پیام‌های سفارشی

```env
WELCOME_MESSAGE=خوش آمدید!
BAN_MESSAGE=کاربر مسدود شد
KICK_MESSAGE=کاربر اخراج شد
WARN_MESSAGE=⚠️ هشدار: {count}/{limit}
```

## نکات ایمنی

### ایمنی Token
- **هرگز** token را عمومی کنید
- فایل `.env` را در `.gitignore` قرار دهید
- از environment variables محیطی استفاده کنید

### ایمنی User IDs
- هیچ User ID را در کد hard-code نکنید
- از `.env` برای تمام IDs استفاده کنید

### Permissions
- دسترسی‌های کاربران را منطقی تنظیم کنید
- Admin count را کم نگه دارید
- Moderator list را هر ماه بررسی کنید

### Data Protection
- لاگ‌ها حاوی اطلاعات شخصی هستند
- لاگ‌ها را محفوظ نگه دارید
- Backup منظم بگیرید

## خطاهای رایج

### خطا: "BOT_TOKEN not set in .env file"

**علت:** Token تنظیم نشده‌است

**حل:**
```bash
# بررسی فایل .env
cat .env

# اگر خالی بود:
BOT_TOKEN=your_token_here
```

### خطا: "Unknown method"

**علت:** API Rubika دستور را پشتیبانی نمی‌کند

**حل:**
- دستور را بررسی کنید
- نسخه rubpy را آپدیت کنید

### خطا: "User not found"

**علت:** User ID غلط است

**حل:**
```python
# بررسی User ID
user_id = "123456789"
if not user_id.isdigit():
    print("User ID باید عددی باشد")
```

### خطا: "Permission denied"

**علت:** کاربر دسترسی لازم ندارد

**حل:**
- User را به ADMIN_USERS اضافه کنید
- یا MODERATOR_USERS

### خطا: "Message deleted by sender"

**علت:** کاربر پیام را حذف کرده‌است

**حل:** این خطا قابل جلوگیری نیست

## بهینه‌سازی

### بهتری عملکرد

```python
# از async/await استفاده کنید
async def my_handler():
    await client.send_message(...)

# از batch operations استفاده کنید
await client.delete_messages(
    message_ids=[id1, id2, id3]
)
```

### مصرف رم

```python
# پاک کردن تاریخچه
from handlers.moderation_handlers import clear_all_warnings
clear_all_warnings()
```

### سرعت

```python
# Middleware برای بهتری سرعت
@bot.middleware()
async def fast_middleware(bot, update, call_next):
    # کدهای سریع
    await call_next()
```

## مثال‌های عملی

### مثال 1: Setup کامل

```bash
# 1. نصب
git clone ...
cd group_manager_bot

# 2. Environment
cp .env.example .env
nano .env
# ویرایش:
# BOT_TOKEN=your_token
# GROUP_CHAT_IDS=your_group_id
# ADMIN_USERS=your_user_id

# 3. نصب وابستگی‌ها
pip install python-dotenv

# 4. اجرا
python main.py
```

### مثال 2: اضافه کردن Admin

```env
# قبل
ADMIN_USERS=user1_id

# بعد
ADMIN_USERS=user1_id,user2_id,user3_id
```

### مثال 3: تغییر کلمات ممنوعه

```env
# فقط انگلیسی
BANNED_WORDS=spam,abuse,harassment

# فقط فارسی  
BANNED_WORDS=کلمه‌نامناسب,فحش,توهین

# مخلوط
BANNED_WORDS=spam,کلمه‌نامناسب,abuse,توهین
```

---

**نسخه:** 1.0.0  
**آخر بروزرسانی:** 2024
