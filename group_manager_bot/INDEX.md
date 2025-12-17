# مفهرس و راهنمای فایل‌ها 📑

## فایل‌های اصلی

### 🚀 شروع سریع
- **[QUICKSTART.md](QUICKSTART.md)** - شروع در 5 دقیقه

### 📖 مستندات اصلی
- **[README.md](README.md)** - راهنمای کامل و ویژگی‌ها
- **[USAGE.md](USAGE.md)** - دستورالعمل دستورات و استفاده
- **[INSTALLATION.md](INSTALLATION.md)** - نصب و تنظیم دقیق
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - راهنمای توسعه و گسترش

### ⚙️ فایل‌های تنظیم
- **[.env.example](.env.example)** - نمونه متغیرهای محیطی
- **[example.env](example.env)** - نمونه کامل‌تر با توضیح
- **[.gitignore](.gitignore)** - Git ignore patterns

## فایل‌های پروژه

### اصلی
| فایل | توضیح |
|------|-------|
| `main.py` | نقطه شروع برنامه |
| `config.py` | تنظیمات و متغیرهای محیطی |
| `requirements.txt` | پکیج‌های مورد نیاز |

### Handlers (دستورات و رویدادها)
| فایل | توضیح |
|------|-------|
| `handlers/__init__.py` | صادرات handlers |
| `handlers/admin_handlers.py` | دستورات Admin: /kick, /ban, /promote |
| `handlers/moderation_handlers.py` | فیلتر محتوا، هشدار، ban خودکار |
| `handlers/logging_handlers.py` | ثبت فعالیت‌ها و رویدادها |

### Utils (توابع کمکی)
| فایل | توضیح |
|------|-------|
| `utils/__init__.py` | صادرات utils |
| `utils/permission.py` | مدیریت سطح دسترسی کاربران |
| `utils/filters_custom.py` | فیلترهای سفارشی |
| `utils/helpers.py` | توابع کمکی و فرمت‌کنندگی |

## چه کجا چه بدنبال کنم؟

### 🔰 برای شروع
1. **[QUICKSTART.md](QUICKSTART.md)** را بخوانید
2. فایل `.env` را تنظیم کنید
3. `python main.py` را اجرا کنید

### 📚 برای یادگیری
1. **[README.md](README.md)** - تمام ویژگی‌ها
2. **[USAGE.md](USAGE.md)** - تمام دستورات
3. **[INSTALLATION.md](INSTALLATION.md)** - جزئیات نصب

### 🛠️ برای توسعه
1. **[DEVELOPMENT.md](DEVELOPMENT.md)** - اضافه کردن feature
2. `handlers/` فولدر - برای اضافه کردن دستور
3. `utils/` فولدر - برای توابع کمکی

### 🐛 برای حل مشکل
1. **[INSTALLATION.md](INSTALLATION.md)** - مشکلات نصب
2. **[README.md](README.md)** - مشکلات رایج
3. **[USAGE.md](USAGE.md)** - مشکلات استفاده

## ساختار مجدد

```
group_manager_bot/
│
├── 📖 مستندات
│   ├── INDEX.md              ← شما اینجا هستید
│   ├── QUICKSTART.md         ← شروع سریع
│   ├── README.md             ← مستندات اصلی
│   ├── USAGE.md              ← دستورالعمل‌ها
│   ├── INSTALLATION.md       ← نصب و راه‌اندازی
│   └── DEVELOPMENT.md        ← توسعه و گسترش
│
├── ⚙️ تنظیمات
│   ├── .env.example          ← نمونه ساده
│   ├── example.env           ← نمونه کامل
│   ├── .gitignore            ← Git ignore
│   └── requirements.txt      ← پکیج‌ها
│
├── 🔧 کد اصلی
│   ├── main.py               ← نقطه شروع
│   ├── config.py             ← تنظیمات
│   │
│   ├── handlers/             ← دستورات و رویدادها
│   │   ├── __init__.py
│   │   ├── admin_handlers.py
│   │   ├── moderation_handlers.py
│   │   └── logging_handlers.py
│   │
│   └── utils/                ← توابع کمکی
│       ├── __init__.py
│       ├── permission.py
│       ├── filters_custom.py
│       └── helpers.py
│
└── 📁 فولدرهای خودکار
    └── logs/                 ← فایل‌های لاگ (خودکار)
```

## خط‌مشی نام‌گذاری

| نوع | قرارداد |
|------|---------|
| فایل | `snake_case.py` |
| Function | `snake_case()` |
| Class | `PascalCase` |
| Constant | `UPPER_CASE` |

## ترجمه‌ی شرایط فنی

| انگلیسی | فارسی |
|--------|--------|
| Admin | مدیر |
| Moderator | ناظر |
| User | کاربر |
| Handler | رابط‌الگو |
| Filter | فیلتر |
| Log | لاگ/ثبت |
| Command | دستور |
| Permission | دسترسی |
| Ban | مسدود کردن |
| Kick | اخراج |
| Warn | هشدار |

## تماس و پشتیبانی

### منابع
- 📚 [Rubpy Documentation](https://github.com/RubikaPyX/RubikaPy)
- 🔗 [Rubika Official](https://rubika.ir)

### مشکلات
- اگر مشکلی دارید، ابتدا INSTALLATION.md را چک کنید
- سپس USAGE.md و README.md را بخوانید
- اگر هنوز حل نشد، DEVELOPMENT.md را ببینید

---

## نسخه و تاریخ

| نسخه | تاریخ | توضیح |
|------|-------|--------|
| 1.0.0 | 2024 | نسخه اول و نهایی |

---

**آخر بروزرسانی:** 2024

✨ **پیشنهاد:** با QUICKSTART.md شروع کنید!
