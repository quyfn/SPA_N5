# 🎬 STEP-BY-STEP GUIDE - CÁC BƯỚC CHI TIẾT

## PHẦN 1️⃣: KHỞI CHẠY SERVER

### Bước 1: Mở PowerShell hoặc Command Prompt
```
Windows Search → Gõ "PowerShell" → Enter
hoặc
Windows Search → Gõ "cmd" → Enter
```

### Bước 2: Điều hướng đến thư mục dự án
```powershell
cd C:\Users\LENOVO\PycharmProjects\DjangoProject1\LAPTRINHWEB\SPA
```

📌 **Copy & Paste đầy đủ:**
```
C:\Users\LENOVO\PycharmProjects\DjangoProject1\LAPTRINHWEB\SPA
```

### Bước 3: Khởi chạy Django server
```powershell
python manage.py runserver
```

### Bước 4: Xác nhận server đã chạy
```
Terminal sẽ hiển thị:

Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

✅ **Server đã chạy thành công!**

---

## PHẦN 2️⃣: TRUY CẬP TRANG LOGIN

### Bước 1: Mở Trình Duyệt Web
```
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari (Mac)
Bất kỳ trình duyệt nào cũng được
```

### Bước 2: Nhập URL vào thanh địa chỉ
```
http://127.0.0.1:8000/login/
```

⚠️ **QUAN TRỌNG:**
- ❌ KHÔNG: `http://127.0.0.1:8000/SPA/login/`
- ✅ ĐÚNG: `http://127.0.0.1:8000/login/`
- ✅ ĐÚNG: `localhost:8000/login/`

### Bước 3: Nhấn Enter
```
Trang login sẽ hiển thị
```

---

## PHẦN 3️⃣: ĐĂNG KÝ TÀI KHOẢN

### Bước 1: Vào trang đăng ký
```
Nhấn "Đăng ký ngay" từ trang login
hoặc
Nhập URL: http://127.0.0.1:8000/register/
```

### Bước 2: Điền thông tin
```
Tên *           : Nhập tên của bạn
                  Ví dụ: "Thanh"

Họ *            : Nhập họ của bạn
                  Ví dụ: "Nguyễn"

Email *         : Nhập email hợp lệ
                  Ví dụ: "thanh123@gmail.com"

Mật khẩu *      : Tối thiểu 8 ký tự
                  Không toàn số
                  Không trùng tên
                  Ví dụ: "MyPass@2024"

Xác nhận MK *   : Nhập lại mật khẩu
                  Phải giống phần trên
                  Ví dụ: "MyPass@2024"

Tick checkbox   : ☑ Tôi đồng ý với...
```

### Bước 3: Kiểm tra yêu cầu mật khẩu
```
Ghi chú sẽ hiển thị:
✓ Ít nhất 8 ký tự
✓ Không toàn số
✓ Không trùng với tên người dùng
```

### Bước 4: Nhấn "Tạo Tài Khoản"
```
Nếu thành công:
→ Thấy tin nhắn "Đăng ký thành công!"
→ Tự động chuyển sang trang login
```

### Bước 5: Test
```
Sau khi đăng ký, hãy thử đăng nhập ngay
Email: thanh123@gmail.com
Mật khẩu: MyPass@2024
```

---

## PHẦN 4️⃣: ĐĂNG NHẬP

### Bước 1: Vào trang đăng nhập
```
URL: http://127.0.0.1:8000/login/
```

### Bước 2: Nhập thông tin đăng nhập
```
Email      : thanh123@gmail.com
Mật khẩu   : MyPass@2024
```

### Bước 3: Tùy chọn
```
☐ Ghi nhớ tôi    (Optional)
[Quên mật khẩu?] (Để sau)
```

### Bước 4: Nhấn "Đăng Nhập"
```
Nếu thành công:
→ Thấy tin nhắn "Chào mừng..."
→ Chuyển đến trang Dashboard
→ URL: http://127.0.0.1:8000/
```

### Bước 5: Kiểm tra Dashboard
```
Trang sẽ hiển thị:
- Menu dịch vụ
- Các tính năng khác
- Nút Đăng xuất
```

---

## PHẦN 5️⃣: CÁC TRANG KHÁC

### Trang Lịch Hẹn
```
URL: http://127.0.0.1:8000/lich-hen/
Chức năng: Xem danh sách lịch hẹn
```

### Trang Phản Hồi
```
URL: http://127.0.0.1:8000/phan-hoi/
Chức năng: Xem feedback từ khách hàng
```

### Trang Tư Vấn
```
URL: http://127.0.0.1:8000/phan-hoi/tu-van/
Chức năng: Tư vấn trực tuyến
```

### Trang Khách Hàng
```
URL: http://127.0.0.1:8000/khach-hang/
Chức năng: Quản lý khách hàng
```

### Trang Admin
```
URL: http://127.0.0.1:8000/admin/
Username: (Cần tạo superuser)
Password: (Cần tạo superuser)
```

---

## PHẦN 6️⃣: TẠO SUPERUSER (Admin)

### Bước 1: Dừng server (Ctrl+C)
```
Nhấn Ctrl+C trong terminal
```

### Bước 2: Chạy lệnh tạo superuser
```powershell
python manage.py createsuperuser
```

### Bước 3: Điền thông tin
```
Username: admin
Email: admin@example.com
Password: admin123456
Password (again): admin123456
Superuser created successfully ✅
```

### Bước 4: Khởi chạy lại server
```powershell
python manage.py runserver
```

### Bước 5: Truy cập admin panel
```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: admin123456
```

---

## PHẦN 7️⃣: TROUBLESHOOTING

### ❌ "Trang không tìm thấy"
```
Kiểm tra:
1. Server đã chạy? (Terminal có thông báo?)
2. URL đúng? (http://127.0.0.1:8000/login/)
3. Port 8000? (Không phải port khác?)
```

### ❌ "Server không chạy"
```
Giải pháp:
cd C:\Users\LENOVO\PycharmProjects\DjangoProject1\LAPTRINHWEB\SPA
python manage.py runserver
```

### ❌ "Port 8000 bị dùng"
```
Chạy trên port khác:
python manage.py runserver 8001

Sau đó truy cập:
http://127.0.0.1:8001/login/
```

### ❌ "Lỗi Module"
```
Cài đặt dependencies:
pip install django
pip install pillow
```

### ❌ "Database error"
```
Chạy migration:
python manage.py migrate
```

### ❌ "Static files không load"
```
Xóa cache browser:
Ctrl+Shift+Delete
hoặc
Ctrl+F5 (Hard refresh)
```

### ❌ "Form không submit"
```
Kiểm tra:
1. Có CSRF token không?
2. Điền đầy đủ thông tin?
3. Mật khẩu hợp lệ?
4. Check browser console (F12)
```

---

## PHẦN 8️⃣: NÂNG CAO

### Thay đổi Server Port
```powershell
# Port 8000 (mặc định)
python manage.py runserver

# Port tùy chỉnh (ví dụ 3000)
python manage.py runserver 3000

# Địa chỉ tùy chỉnh
python manage.py runserver 127.0.0.1:8000
python manage.py runserver 0.0.0.0:8000
```

### Chế độ Development vs Production
```
Development (hiện tại):
- DEBUG = True
- Static files tự động
- Error messages chi tiết

Production (sau này):
- DEBUG = False
- Collectstatic cần chạy
- Error messages ẩn
```

### Tạo Dummy Data
```python
# Mở Django shell
python manage.py shell

# Tạo user test
from django.contrib.auth.models import User
User.objects.create_user(
    username='test123',
    email='test@example.com',
    password='testpass123'
)
```

---

## PHẦN 9️⃣: BEST PRACTICES

### ✅ DO (Nên làm)
```
✓ Khởi chạy server trước
✓ Truy cập đúng URL
✓ Làm mới page (F5)
✓ Xóa cache khi cần
✓ Check terminal logs
✓ Dùng mật khẩu mạnh
✓ Test tất cả chức năng
```

### ❌ DON'T (Không nên)
```
✗ Quên khởi chạy server
✗ Truy cập URL sai (/SPA/login/)
✗ Không làm mới page
✗ Dùng mật khẩu yếu
✗ Bỏ qua error messages
✗ Chỉnh settings.py khi đang debug
```

---

## 📋 CHECKLIST

- [ ] Server chạy thành công
- [ ] Truy cập /login/ được
- [ ] Tạo tài khoản thành công
- [ ] Đăng nhập thành công
- [ ] Vào Dashboard được
- [ ] Xem trang khác được
- [ ] Đăng xuất được
- [ ] Cache browser được clear
- [ ] Kiểm tra admin panel
- [ ] Test tất cả error cases

---

## 🎯 NEXT STEPS

1. **Test tính năng:**
   - ✅ Đăng ký
   - ✅ Đăng nhập
   - ✅ Đăng xuất
   - ✅ Quên mật khẩu (UI)
   - ✅ Social login (UI)

2. **Tùy chỉnh:**
   - Thay đổi màu sắc
   - Thêm logo
   - Thay đổi text
   - Tùy chỉnh CSS

3. **Mở rộng:**
   - Email verification
   - Two-factor auth
   - User profiles
   - Settings page

---

**Created:** 2026-04-14
**Status:** ✅ Complete Step-by-Step Guide
**Tested:** Yes


