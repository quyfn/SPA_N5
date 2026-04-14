## ✅ CHECKLIST - HỆ THỐNG ĐĂNG NHẬP & ĐĂNG KÝ

### 🎯 Giai Đoạn 1: Chuẩn Bị

- [ ] Python 3.8+ đã cài đặt
- [ ] Django 6.0+ đã cài đặt
- [ ] Thư mục `/templates` tồn tại
- [ ] Thư mục `/static/css` tồn tại
- [ ] File `manage.py` tồn tại

### 🎯 Giai Đoạn 2: Kiểm Tra Files

**Backend:**
- [ ] `SPA/forms.py` tồn tại
- [ ] `SPA/views.py` được cập nhật (có `user_login`, `user_register`, `user_logout`)
- [ ] `SPA/urls.py` được cập nhật (có routes `/login/`, `/register/`, `/logout/`)
- [ ] `SPA/settings.py` được cập nhật (có MESSAGE_TAGS)

**Frontend:**
- [ ] `templates/login.html` tồn tại
- [ ] `templates/register.html` tồn tại
- [ ] `static/css/auth.css` tồn tại

**Documentation:**
- [ ] `README_AUTH.md` tồn tại
- [ ] `QUICK_START.md` tồn tại
- [ ] `PREVIEW.html` tồn tại
- [ ] `HUONG_DAN_TEST.py` tồn tại

### 🎯 Giai Đoạn 3: Thiết Lập Database

- [ ] Chạy: `python manage.py migrate`
- [ ] Không có lỗi trong output
- [ ] File `db.sqlite3` được tạo/cập nhật

### 🎯 Giai Đoạn 4: Tạo Admin User (Tùy Chọn)

```bash
python manage.py createsuperuser
```

- [ ] Tài khoản admin tạo thành công
- [ ] Ghi nhớ username/password

### 🎯 Giai Đoạn 5: Test Backend

Chạy Django shell:
```bash
python manage.py shell
```

Test từng phần:

```python
# Test 1: Kiểm tra LoginForm
from SPA.forms import LoginForm
form = LoginForm()
print("✓ LoginForm import OK")

# Test 2: Kiểm tra RegisterForm
from SPA.forms import RegisterForm
form = RegisterForm()
print("✓ RegisterForm import OK")

# Test 3: Kiểm tra User model
from django.contrib.auth.models import User
users = User.objects.all()
print(f"✓ {len(users)} users trong database")

# Thoát
exit()
```

- [ ] Tất cả imports OK
- [ ] Không có lỗi

### 🎯 Giai Đoạn 6: Chạy Server

```bash
python manage.py runserver
```

- [ ] Server chạy thành công (hiển thị "Starting development server...")
- [ ] Port 8000 có sẵn (không có "Address already in use")
- [ ] Không có lỗi Python

### 🎯 Giai Đoạn 7: Test Giao Diện

#### Trang Đăng Ký:

```
URL: http://localhost:8000/register/
```

Kiểm tra:
- [ ] Trang load thành công (không 404)
- [ ] Tiêu đề: "Đăng Ký"
- [ ] Có các trường: Tên, Họ, Email, Mật khẩu, Xác nhận
- [ ] Có nút "Tạo Tài Khoản"
- [ ] Link "Đăng nhập" có ở dưới
- [ ] CSS load đúng (có gradient, icons)

#### Test Đăng Ký:

```
Tên: Nguyễn
Họ: Văn
Email: test@example.com
Mật khẩu: Password123
Xác nhận: Password123
```

- [ ] Form submit thành công
- [ ] Thấy message: "Đăng ký thành công! Vui lòng đăng nhập."
- [ ] Redirect sang trang đăng nhập

#### Test Đăng Ký Thất Bại:

```
Thử đăng ký lại với email trên
```

- [ ] Thấy lỗi: "Email này đã được đăng ký"

#### Trang Đăng Nhập:

```
URL: http://localhost:8000/login/
```

Kiểm tra:
- [ ] Trang load thành công
- [ ] Tiêu đề: "Đăng Nhập"
- [ ] Có các trường: Email, Mật khẩu
- [ ] Có checkbox "Ghi nhớ tôi"
- [ ] Có link "Quên mật khẩu?"
- [ ] Có nút "Đăng Nhập"
- [ ] Link "Đăng ký" có ở dưới
- [ ] CSS load đúng

#### Test Đăng Nhập:

```
Email: test@example.com
Mật khẩu: Password123
```

- [ ] Form submit thành công
- [ ] Thấy message: "Chào mừng Nguyễn!"
- [ ] Redirect sang trang chủ (`/`)
- [ ] User đã được bảo mật (Session)

#### Test Đăng Nhập Thất Bại:

**Test 1: Email sai**
```
Email: wrong@example.com
Mật khẩu: Password123
```
- [ ] Thấy lỗi: "Email này không tồn tại."

**Test 2: Mật khẩu sai**
```
Email: test@example.com
Mật khẩu: WrongPassword
```
- [ ] Thấy lỗi: "Mật khẩu không chính xác."

#### Test Đăng Xuất:

```
URL: http://localhost:8000/logout/
```

- [ ] Redirect sang trang đăng nhập
- [ ] Thấy message: "Bạn đã đăng xuất thành công!"

### 🎯 Giai Đoạn 8: Test Validation

#### Email Validation:

- [ ] Email trống → Lỗi "Bắt buộc"
- [ ] Email sai định dạng → Lỗi "Email không hợp lệ"
- [ ] Email trùng → Lỗi "Email đã được đăng ký"

#### Mật Khẩu Validation:

- [ ] < 8 ký tự → Lỗi "Ít nhất 8 ký tự"
- [ ] Toàn số → Lỗi "Không thể toàn số"
- [ ] Không khớp → Lỗi "Mật khẩu không khớp"
- [ ] Trùng email → Lỗi "Không được trùng email"

#### Tên/Họ Validation:

- [ ] Tên trống → Lỗi "Bắt buộc"
- [ ] Họ để trống OK (không bắt buộc)

### 🎯 Giai Đoạn 9: Test Responsive

#### Desktop (1200px+):
- [ ] Form hiển thị đúng
- [ ] Gradient background OK
- [ ] Icons hiển thị đúng

#### Tablet (768px):
- [ ] Form vẫn nhìn thấy được
- [ ] Input fields vẫn sử dụng được
- [ ] Font size phù hợp

#### Mobile (360px):
- [ ] Form không bị cut off
- [ ] Input fields vẫn dùng được
- [ ] Button dễ nhấn
- [ ] Scrollable nếu cần

**Test trên browser DevTools:**
- [ ] F12 → Toggle device toolbar
- [ ] Thử kích thước: 320px, 768px, 1200px

### 🎯 Giai Đoạn 10: Test Bảo Mật

- [ ] CSRF token có trong form ({% csrf_token %})
- [ ] Mật khẩu không hiển thị khi gõ
- [ ] Không thấy mật khẩu trong URL
- [ ] Password được hash trong database

Kiểm tra database:
```python
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.get(email='test@example.com')
print(user.password)  # Phải là hash, không phải plain text
```

- [ ] Mật khẩu là hash (bắt đầu với "pbkdf2_sha256$")

### 🎯 Giai Đoạn 11: Test Trực Quan

- [ ] Gradient màu có đẹp không?
- [ ] Icons load đúng không (Font Awesome)?
- [ ] Text tiếng Việt hiển thị đúng không?
- [ ] Animation (fade-in) có hoạt động không?
- [ ] Hover effects có hoạt động không?

### 🎯 Giai Đoạn 12: Kiểm Tra Final

**Tổng Quát:**
- [ ] Mọi file đã tạo
- [ ] Server chạy không lỗi
- [ ] Trang load không 404
- [ ] Form validation hoạt động
- [ ] Đăng ký thành công
- [ ] Đăng nhập thành công
- [ ] Đăng xuất thành công

**Documentation:**
- [ ] README_AUTH.md dễ hiểu
- [ ] QUICK_START.md đủ hướng dẫn
- [ ] PREVIEW.html xem được
- [ ] HUONG_DAN_TEST.py chạy được

**Performance:**
- [ ] Trang load nhanh (< 1s)
- [ ] Không có console errors
- [ ] Không có lỗi network
- [ ] Database queries efficient

---

## 🎉 HOÀN THÀNH!

Nếu tất cả checkbox được tick ✅, bạn đã:
- ✅ Cài đặt thành công
- ✅ Test toàn bộ tính năng
- ✅ Xác minh bảo mật
- ✅ Kiểm tra responsive
- ✅ Sẵn sàng deploy!

---

## 📝 GHI CHÚ

Nơi ghi chú các vấn đề gặp phải:

```
Vấn đề:
Giải pháp:
Ngày fix:
```

---

**Tạo bởi:** GitHub Copilot  
**Ngày:** 14/04/2026

