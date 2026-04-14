# 📸 VISUAL GUIDE - SPA LOGIN/REGISTER

## 🖼️ Cấu Trúc Dự Án

```
┌─────────────────────────────────────────┐
│         DjangoProject1 (Root)           │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        │             │
    LAPTRINHWEB   manage.py (khác)
        │
      SPA (👈 Dự án chính)
        │
    ┌───┴─────────────────────────────┐
    │                                 │
  SPA/               templates/     static/
    │                 │              │
    ├─ views.py      ├─ login.html  ├─ css/
    ├─ forms.py      ├─ register    ├─ js/
    ├─ urls.py       ├─ dashboard   └─ images/
    ├─ settings.py   └─ ...
    ├─ wsgi.py
    └─ manage.py
```

---

## 🚀 FLOW CHẠY SERVER

```
┌─────────────────────────────────┐
│   Mở PowerShell / Command Line   │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  cd SPA project directory       │
│  C:\...\DjangoProject1\...\SPA  │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│  python manage.py runserver     │
│  OR                             │
│  Double-click START_SERVER.bat  │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   Server Started ✅             │
│  http://127.0.0.1:8000/         │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│   Mở Trình Duyệt & Truy Cập     │
└────────────┬────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
 Login             Register
 /login/           /register/
```

---

## 🔐 LOGIN PAGE FLOW

```
User Access: /login/
        │
        ▼
   Django View
   (views.py)
        │
        ├─ Is authenticated? 
        │   ├─ YES → Redirect to Dashboard
        │   └─ NO  → Continue
        │
        ├─ Method is POST?
        │   ├─ YES → Validate Form
        │   │         │
        │   │         ├─ Valid?
        │   │         │   ├─ YES → Authenticate User
        │   │         │   │         │
        │   │         │   │         ├─ User Found?
        │   │         │   │         │   ├─ YES → Password Match?
        │   │         │   │         │   │         ├─ YES → Login ✅ → Dashboard
        │   │         │   │         │   │         └─ NO  → Error Message
        │   │         │   │         │   └─ NO  → Email Not Found
        │   │         │   │
        │   │         └─ NO  → Show Form Errors
        │   │
        │   └─ NO (GET) → Show Empty Form
        │
        ▼
    Render Template
    (login.html)
        │
        ▼
   Show to User
```

---

## 📝 REGISTER PAGE FLOW

```
User Access: /register/
        │
        ▼
   Django View
   (views.py)
        │
        ├─ Is authenticated?
        │   ├─ YES → Redirect to Dashboard
        │   └─ NO  → Continue
        │
        ├─ Method is POST?
        │   ├─ YES → Validate Form
        │   │         │
        │   │         ├─ Valid?
        │   │         │   ├─ YES → Create User
        │   │         │   │         │
        │   │         │   │         ├─ Email already exists?
        │   │         │   │         │   ├─ YES → Error Message
        │   │         │   │         │   └─ NO  → Create ✅
        │   │         │   │         │           Set username = email
        │   │         │   │         │           Hash password
        │   │         │   │         │           Redirect to Login
        │   │         │   │
        │   │         └─ NO  → Show Form Errors
        │   │
        │   └─ NO (GET) → Show Empty Form
        │
        ▼
    Render Template
    (register.html)
        │
        ▼
   Show to User
```

---

## 🎨 GIAO DIỆN THIẾT KẾ

### Login Page
```
┌──────────────────────────────────────┐
│                                      │
│    ┌────────────────────────────┐    │
│    │     SPA Gradient Header     │    │
│    │  (#FF2F6D → #FF69B4)        │    │
│    │                             │    │
│    │  🧖 SPA Icon                │    │
│    │  Đăng Nhập                  │    │
│    │  Chào mừng quay lại         │    │
│    └────────────────────────────┘    │
│                                      │
│    ┌────────────────────────────┐    │
│    │    Form (White Background)  │    │
│    │                             │    │
│    │  📧 Email                   │    │
│    │  [____________]             │    │
│    │                             │    │
│    │  🔒 Password                │    │
│    │  [____________]             │    │
│    │                             │    │
│    │  ☐ Ghi nhớ tôi             │    │
│    │  [Quên mật khẩu?]          │    │
│    │                             │    │
│    │  [ĐĂNG NHẬP BUTTON]         │    │
│    │  (#FF2F6D, Full Width)      │    │
│    │                             │    │
│    │  ─────────────────────────  │    │
│    │   Hoặc tiếp tục với        │    │
│    │  ─────────────────────────  │    │
│    │                             │    │
│    │  [Google] [Facebook]        │    │
│    └────────────────────────────┘    │
│                                      │
│    ┌────────────────────────────┐    │
│    │   Footer (Light Gray Bg)    │    │
│    │ Chưa có tài khoản?          │    │
│    │ [Đăng ký ngay]              │    │
│    └────────────────────────────┘    │
│                                      │
└──────────────────────────────────────┘
```

### Register Page
```
┌──────────────────────────────────────┐
│                                      │
│    ┌────────────────────────────┐    │
│    │     SPA Gradient Header     │    │
│    │  (#FF2F6D → #FF69B4)        │    │
│    │                             │    │
│    │  🧖 SPA Icon                │    │
│    │  Đăng Ký                    │    │
│    │  Tạo tài khoản mới          │    │
│    └────────────────────────────┘    │
│                                      │
│    ┌────────────────────────────┐    │
│    │    Form (White Background)  │    │
│    │    (Scrollable if long)     │    │
│    │                             │    │
│    │  [Tên]        [Họ]         │    │
│    │  [____]       [____]       │    │
│    │                             │    │
│    │  📧 Email                   │    │
│    │  [____________]             │    │
│    │                             │    │
│    │  ⚠️ Yêu cầu mật khẩu:      │    │
│    │  ✓ Ít nhất 8 ký tự         │    │
│    │  ✓ Không toàn số            │    │
│    │  ✓ Không trùng tên          │    │
│    │                             │    │
│    │  🔒 Mật khẩu                │    │
│    │  [____________]             │    │
│    │                             │    │
│    │  🔒 Xác nhận mật khẩu       │    │
│    │  [____________]             │    │
│    │                             │    │
│    │  ☐ Tôi đồng ý Điều khoản    │    │
│    │                             │    │
│    │  [TẠO TÀI KHOẢN BUTTON]     │    │
│    │  (#FF2F6D, Full Width)      │    │
│    └────────────────────────────┘    │
│                                      │
│    ┌────────────────────────────┐    │
│    │   Footer (Light Gray Bg)    │    │
│    │ Đã có tài khoản?            │    │
│    │ [Đăng nhập ngay]            │    │
│    └────────────────────────────┘    │
│                                      │
└──────────────────────────────────────┘
```

---

## 🔄 REQUEST/RESPONSE CYCLE

### Login Request
```
User enters credentials and clicks "Đăng Nhập"
        │
        ▼
POST /login/
├─ email: user@example.com
├─ password: mypassword123
└─ csrfmiddlewaretoken: xxxxx
        │
        ▼
Django Process
├─ Validate CSRF token ✅
├─ Validate form data ✅
├─ Find user by email ✅
├─ Authenticate password ✅
└─ Create session ✅
        │
        ▼
Response
├─ If Success: Redirect to /
├─ If Error: Render form with errors
└─ Set session cookie 🍪
```

### Register Request
```
User fills form and clicks "Tạo Tài Khoản"
        │
        ▼
POST /register/
├─ first_name: John
├─ last_name: Doe
├─ email: john@example.com
├─ password1: SecurePass123
├─ password2: SecurePass123
└─ csrfmiddlewaretoken: xxxxx
        │
        ▼
Django Process
├─ Validate CSRF token ✅
├─ Validate form data ✅
├─ Check email not duplicate ✅
├─ Validate passwords match ✅
├─ Hash password ✅
├─ Create User object ✅
└─ Save to database ✅
        │
        ▼
Response
├─ If Success: 
│   ├─ Show success message
│   └─ Redirect to /login/
├─ If Error: Render form with errors
└─ Don't create session (user needs to login)
```

---

## 🛡️ SECURITY LAYERS

```
┌─────────────────────────────────┐
│    User Input                   │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    CSRF Token Validation        │ ← Django CSRF Protection
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    Form Validation              │ ← Django Forms
├─ Email format check            │
├─ Password strength check       │
└─ Password match check          │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    Database Query Protection    │ ← ORM (SQL Injection)
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    Password Hashing             │ ← PBKDF2 + Salt
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    Session Management           │ ← Django Sessions
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│    Secure Database              │
│    (SQLite + Encryption)        │
└─────────────────────────────────┘
```

---

## 📊 DATABASE SCHEMA

```
┌──────────────────────┐
│   User Table         │
├──────────────────────┤
│ id (PK)              │
│ username *           │
│ email *              │
│ first_name           │
│ last_name            │
│ password (hashed)    │
│ is_active            │
│ is_staff             │
│ date_joined          │
│ last_login           │
└──────────────────────┘
    │
    ├─ * Unique
    └─ password = PBKDF2-SHA256
```

---

## 🎯 URL MAPPING

```
URL                          View Function           Template
────────────────────────────────────────────────────────────
/login/                    → user_login()          → login.html
/register/                 → user_register()       → register.html
/logout/                   → user_logout()         → (redirect)
/                          → service_dashboard()   → service_dashboard.html
/lich-hen/                 → appointment_dash()    → appointment_dashboard.html
/phan-hoi/                 → feedback_dash()       → feedback_dashboard.html
/phan-hoi/tu-van/          → consultation_dash()   → consultation_dashboard.html
/phan-hoi/tu-van/<id>/     → consultation_detail() → consultation_detail.html
/phan-hoi/<id>/            → feedback_detail()     → feedback_detail.html
/khach-hang/               → customer_dash()       → customer_dashboard.html
/khach-hang/<id>/          → customer_detail()     → customer_detail.html
/admin/                    → admin site            → Django Admin
```

---

## 📱 RESPONSIVE BREAKDOWN

### Desktop (>768px)
```
Full-width card with max-width: 450px
Side-by-side form fields
Full icons display
```

### Tablet (768px)
```
Adjusted padding
Responsive grid
Optimized spacing
```

### Mobile (<576px)
```
Single column layout
Smaller padding
Touch-friendly buttons
Stacked social buttons
```

---

## ⚙️ CONFIGURATION OVERVIEW

```
Django Settings (settings.py)
├─ DEBUG = True
├─ ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
├─ INSTALLED_APPS = [auth, sessions, messages, ...]
├─ DATABASES = SQLite3
├─ AUTH_PASSWORD_VALIDATORS = [strength checks]
├─ TEMPLATES = [DIRS: BASE_DIR/'templates']
├─ STATIC_URL = 'static/'
└─ LOGIN_URL = 'user_login'
```

---

**Created:** 2026-04-14
**Status:** ✅ Complete Visual Guide
**Last Updated:** Latest


