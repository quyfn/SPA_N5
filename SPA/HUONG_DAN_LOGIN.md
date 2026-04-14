# Hướng Dẫn Sử Dụng Trang Login & Register

## 🚀 Cách Khởi Chạy

### 1. Mở Terminal/CMD
Cd vào thư mục dự án SPA:
```bash
cd C:\Users\LENOVO\PycharmProjects\DjangoProject1\LAPTRINHWEB\SPA
```

### 2. Khởi Chạy Django Server
```bash
python manage.py runserver
```

Bạn sẽ thấy output:
```
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 3. Truy Cập Trang

**Trang Đăng Nhập:**
```
http://127.0.0.1:8000/login/
```

**Trang Đăng Ký:**
```
http://127.0.0.1:8000/register/
```

**Trang Dịch Vụ (Trang Chính - Cần Đăng Nhập):**
```
http://127.0.0.1:8000/
```

## ⚠️ Lưu Ý Quan Trọng

- **Không** truy cập: `http://127.0.0.1:8000/SPA/login/` ❌
- **Đúng** là: `http://127.0.0.1:8000/login/` ✅

## 📝 Để Đăng Ký Tài Khoản

1. Vào trang: `http://127.0.0.1:8000/register/`
2. Điền đầy đủ thông tin:
   - Tên
   - Họ
   - Email
   - Mật khẩu (ít nhất 8 ký tự)
   - Xác nhận mật khẩu
3. Tick vào "Tôi đồng ý với Điều khoản dịch vụ"
4. Nhấn "Tạo Tài Khoản"

## 🔐 Để Đăng Nhập

1. Vào trang: `http://127.0.0.1:8000/login/`
2. Nhập Email và Mật khẩu
3. Nhấn "Đăng Nhập"
4. Sẽ được chuyển hướng đến trang dịch vụ

## 🎨 Giao Diện

- **Màu nổi bật:** #FF2F6D (Hồng)
- **Gradient:** #FF2F6D → #FF69B4
- **Responsive:** Hoạt động tốt trên mọi thiết bị

## 🔴 Nếu Gặp Lỗi

### Lỗi: "ModuleNotFoundError"
→ Cài đặt requirements: `pip install django`

### Lỗi: "Table doesn't exist"
→ Chạy: `python manage.py migrate`

### Lỗi: "Port 8000 already in use"
→ Dùng port khác: `python manage.py runserver 8001`

## ✅ Cấu Hình Hoàn Chỉnh

- ✅ URL routes: Đã cấu hình
- ✅ Views: Đã tạo
- ✅ Forms: Đã tạo (LoginForm, RegisterForm)
- ✅ Templates: login.html, register.html
- ✅ CSS: Màu #FF2F6D đã áp dụng
- ✅ Authentication: Django auth đã tích hợp


