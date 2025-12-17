# شروع سریع ⚡

سریع‌ترین راه برای راه‌اندازی ربات در 5 دقیقه!

## مرحله 1: نصب (1 دقیقه)

```bash
pip install python-dotenv
```

## مرحله 2: تنظیم (2 دقیقه)

```bash
cp .env.example .env
```

سپس .env را ویرایش کنید و این ۳ مورد را پر کنید:

```env
BOT_TOKEN=your_token_here
GROUP_CHAT_IDS=your_group_id
ADMIN_USERS=your_user_id
```

## مرحله 3: اجرا (فوری)

```bash
python main.py
```

بس! ربات شروع به کار کرد! 🚀

## دستورات سریع

### Admin Commands
```
/kick 123456789      - اخراج کاربر
/ban 123456789       - مسدود کردن دائمی
/promote 123456789   - ترفیع به مدیر
/demote 123456789    - تنزل از مدیری
/mute 123456789      - سکوت دادن
```

### مثال‌های بیشتر

#### بدست آوردن Group ID

1. پیامی در گروه ارسال کنید
2. لاگ‌ها را چک کنید: `tail logs/group_manager.log`
3. Chat ID را کپی کنید

#### اضافه کردن چند گروه

```env
GROUP_CHAT_IDS=123,456,789
```

#### اضافه کردن چند Admin

```env
ADMIN_USERS=111,222,333
```

#### تنظیم کلمات ممنوعه

```env
BANNED_WORDS=spam,bad,inappropriate
```

## خطاهای رایج

### "BOT_TOKEN not set"
→ BOT_TOKEN را در .env پر کنید

### دستورات کار نمی‌کنند
→ مطمئن شوید:
- کاربر Admin است
- GROUP_CHAT_IDS درست است

### لاگ‌ها ذخیره نمی‌شوند
→ `ENABLE_LOGGING=True` را بررسی کنید

## بعد

- 📖 [README.md](README.md) برای جزئیات بیشتر
- 📚 [USAGE.md](USAGE.md) برای دستورات کامل
- 🛠️ [DEVELOPMENT.md](DEVELOPMENT.md) برای توسعه

---

**تبریک! ربات شما آماده است** ✅
