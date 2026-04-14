# 📱 Hướng Dẫn Hệ Thống Đăng Nhập & Đăng Ký Spa

## 🎯 Tính Năng

✅ Giao diện đăng nhập hiện đại và đẹp mắt  
✅ Giao diện đăng ký với xác thực dữ liệu  
✅ Xác thực email duy nhất  
✅ Kiểm tra mật khẩu mạnh  
✅ Flash messages cho phản hồi người dùng  
✅ Responsive design (di động/desktop)  
✅ Hỗ trợ tiếng Việt đầy đủ  

---

## 📁 Các File Được Tạo/Sửa

### 1. **forms.py** (Tạo mới)
- Form đăng nhập: `LoginForm`
- Form đăng ký: `RegisterForm`

### 2. **views.py** (Cập nhật)
- `user_login()` - Xử lý đăng nhập
- `user_register()` - Xử lý đăng ký
- `user_logout()` - Xử lý đăng xuất

### 3. **urls.py** (Cập nhật)
- `path('login/', ...)` - Trang đăng nhập
- `path('register/', ...)` - Trang đăng ký
- `path('logout/', ...)` - Xử lý đăng xuất

### 4. **login.html** (Tạo mới)
- Template đăng nhập với thiết kế gradient
- Form validation client-side
- Icons từ Font Awesome

### 5. **register.html** (Tạo mới)
- Template đăng ký với thiết kế đẹp
- Yêu cầu mật khẩu hiển thị
- Kiểm tra điều khoản sử dụng

### 6. **auth.css** (Tạo mới)
- Stylesheet bổ sung cho giao diện

### 7. **settings.py** (Cập nhật)
- Cấu hình messages framework
- Đặt language code thành tiếng Việt

---

## 🚀 Cách Sử Dụng

### 1. **Đăng Ký Tài Khoản Mới**
```
URL: http://localhost:8000/register/
- Nhập họ (bắt buộc)
- Nhập tên (bắt buộc)
- Nhập email (bắt buộc, phải duy nhất)
- Nhập mật khẩu (ít nhất 8 ký tự)
- Xác nhận mật khẩu
- Tick xác nhận điều khoản
- Nhấn "Tạo Tài Khoản"
```

### 2. **Đăng Nhập**
```
URL: http://localhost:8000/login/
- Nhập email đã đăng ký
- Nhập mật khẩu
- (Tùy chọn: Tick "Ghi nhớ tôi")
- Nhấn "Đăng Nhập"
```

### 3. **Đăng Xuất**
```
URL: http://localhost:8000/logout/
- Tự động chuyển hướng về trang đăng nhập
```

---

## 🔐 Bảo Mật

### Kiểm Tra Mật Khẩu:
- ✅ Ít nhất 8 ký tự
- ✅ Không toàn số
- ✅ Không trùng với tên người dùng
- ✅ Phải khớp khi xác nhận

### Kiểm Tra Email:
- ✅ Email phải hợp lệ
- ✅ Email phải duy nhất (không được đăng ký lại)
- ✅ Email không được để trống

### CSRF Protection:
- ✅ Django tự động bảo vệ CSRF tokens

---

## 🎨 Giao Diện

### Màu Sắc:
- **Primary**: #667eea (Tím xanh)
- **Secondary**: #764ba2 (Tím)
- **Success**: #28a745 (Xanh lá)
- **Error**: #f5222d (Đỏ)

### Font:
- Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- Font Awesome Icons 6.4.0

### Hiệu Ứng:
- Gradient backgrounds
- Smooth transitions
- Hover effects
- Loading animations

---

## 📱 Responsive Design

| Thiết Bị | Kích Thước | Hỗ Trợ |
|----------|-----------|---------|
| Mobile | < 576px | ✅ |
| Tablet | 576px - 992px | ✅ |
| Desktop | > 992px | ✅ |

---

## ⚙️ Cấu Hình Thêm (Nếu Cần)

### Bật Xác Thực Email (settings.py):
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### Giữ Người Dùng Đăng Nhập Lâu Hơn:
```python
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30 ngày
```

---

## 🐛 Xử Lý Lỗi Thường Gặp

### Lỗi: "Email này đã được đăng ký"
→ Sử dụng email khác hoặc nhấn "Quên mật khẩu?"

### Lỗi: "Mật khẩu không chính xác"
→ Kiểm tra lại email và mật khẩu

### Lỗi: "Mật khẩu không khớp"
→ Kiểm tra lại mật khẩu xác nhận

### Lỗi: "Yêu cầu bắt buộc"
→ Điền đầy đủ tất cả các trường bắt buộc

---

## 📞 Liên Hệ Hỗ Trợ

Nếu gặp vấn đề, vui lòng kiểm tra:
1. Django server có chạy không?
2. URL có chính xác không?
3. Templates có ở đúng thư mục không?
4. Migrations đã chạy chưa?

---

## 📚 Tài Liệu Tham Khảo

- [Django Authentication](https://docs.djangoproject.com/en/6.0/topics/auth/)
- [Django Forms](https://docs.djangoproject.com/en/6.0/topics/forms/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/)
- [Font Awesome Icons](https://fontawesome.com/docs)

---

**Tạo bởi: GitHub Copilot**  
**Ngày tạo: 14/04/2026**

