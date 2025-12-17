# راهنمای نصب و تنظیم 🛠️

## پیش‌نیازها

- Python 3.7 یا بالاتر
- pip (Package Installer for Python)
- دسترسی به اینترنت

## مراحل نصب

### 1️⃣ دانلود و استخراج

```bash
# دانلود پروژه
git clone <repository_url>
cd group_manager_bot

# یا استخراج فایل ZIP
unzip group_manager_bot.zip
cd group_manager_bot
```

### 2️⃣ نصب وابستگی‌ها

```bash
# نصب Python packages
pip install -r requirements.txt

# یا دستی:
pip install python-dotenv
```

### 3️⃣ تنظیم متغیرهای محیطی

```bash
# کپی کردن فایل نمونه
cp .env.example .env

# ویرایش فایل (به دنبال نمونه زیر)
nano .env      # برای Linux/Mac
# یا
notepad .env   # برای Windows
```

### 4️⃣ تنظیم فایل .env

```env
# BOT TOKEN - از ربات @BotFather یا صفحه مدیریت روبیکا دریافت کنید
BOT_TOKEN=your_actual_bot_token_here

# GROUP CHAT IDs - آیدی گروه‌ها را جداشده با کاما وارد کنید
GROUP_CHAT_IDS=123456789,987654321

# ADMIN USERS - آیدی ادمین‌ها
ADMIN_USERS=your_admin_id

# MODERATOR USERS - آیدی مدیران
MODERATOR_USERS=moderator_id1,moderator_id2

# BANNED WORDS - کلمات ممنوعه
BANNED_WORDS=spam,abuse,inappropriate

# تنظیمات دیگر
WARNING_LIMIT=3
ENABLE_LOGGING=True
AUTO_DELETE_BANNED_CONTENT=True
WARN_ON_BANNED_WORD=True
```

### 5️⃣ بدست آوردن Chat IDs

#### روش 1: از داخل Rubika
1. یک گروه نمونه ایجاد کنید
2. پیام ارسال کنید: `@GroupGuide get_my_id` (اگر موجود باشد)
3. ID نمایش داده خواهد شد

#### روش 2: از Rubika Bot Manager
1. به <https://rubika.ir> بروید
2. در بخش Bot Manager، گروه‌های خود را ببینید
3. Chat ID را از اطلاعات گروه کپی کنید

### 6️⃣ اجرای ربات

```bash
# اجرا کردن ربات
python main.py

# یا برای Linux/Mac:
python3 main.py

# اجرا در background:
nohup python main.py > bot.log 2>&1 &
```

### 7️⃣ بررسی عملکرد

```bash
# بررسی لاگ‌ها
tail -f logs/group_manager.log
```

## حل مشکلات نصب

### خطا: "ModuleNotFoundError: No module named 'dotenv'"

```bash
pip install python-dotenv
```

### خطا: Permission denied

```bash
chmod +x main.py
```

## نکات ایمنی مهم

⚠️ **هرگز نکنید:**
- BOT_TOKEN را در کد درج کنید
- فایل .env را آپلود کنید

✅ **بهتر است:**
- فایل .env را در .gitignore قرار دهید
- Token را محفوظ نگه دارید
