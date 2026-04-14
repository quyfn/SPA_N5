#!/usr/bin/env python
"""
Script hướng dẫn test hệ thống đăng nhập/đăng ký
"""

print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                  🎯 HỆ THỐNG ĐĂNG NHẬP & ĐĂNG KÝ SPA                     ║
║                         Hướng Dẫn Test Nhanh                              ║
╚════════════════════════════════════════════════════════════════════════════╝

📋 BƯỚC 1: Khởi Động Django Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   cd C:\\Users\\LENOVO\\PycharmProjects\\DjangoProject1\\LAPTRINHWEB\\SPA
   python manage.py runserver

   ✓ Server chạy tại: http://localhost:8000/


📋 BƯỚC 2: Truy Cập Trang Đăng Ký
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   URL: http://localhost:8000/register/

   Điền thông tin:
   ├─ Tên: Nguyễn
   ├─ Họ: Văn A
   ├─ Email: nguyenvana@example.com
   ├─ Mật khẩu: Password123
   ├─ Xác nhận: Password123
   └─ ✓ Đồng ý điều khoản

   Nhấn "Tạo Tài Khoản"


📋 BƯỚC 3: Đăng Nhập
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   URL: http://localhost:8000/login/

   Điền thông tin:
   ├─ Email: nguyenvana@example.com
   ├─ Mật khẩu: Password123
   └─ ✓ Ghi nhớ tôi (tùy chọn)

   Nhấn "Đăng Nhập"


📋 BƯỚC 4: Các URL Chính
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   🔐 /login/              → Trang đăng nhập
   📝 /register/           → Trang đăng ký
   🚪 /logout/             → Đăng xuất
   🏠 /                    → Trang chủ dịch vụ
   📅 /lich-hen/           → Lịch hẹn
   💬 /phan-hoi/           → Phản hồi
   👥 /khach-hang/         → Khách hàng
   

✅ CÁC TÍNH NĂNG ĐÃ CÓ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ✓ Form đăng nhập với email + mật khẩu
   ✓ Form đăng ký với xác thực mật khẩu
   ✓ Email phải duy nhất
   ✓ Mật khẩu ít nhất 8 ký tự
   ✓ Giao diện responsive (mobile/desktop)
   ✓ Flash messages cho feedback
   ✓ CSS hiện đại với gradient
   ✓ Icons Font Awesome
   ✓ Hỗ trợ tiếng Việt
   ✓ CSRF protection


🧪 TEST CÁC TÌNH HUỐNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   1️⃣ Đăng ký với email hợp lệ ✓
   2️⃣ Cố gắng đăng ký email trùng → Lỗi ✓
   3️⃣ Mật khẩu không khớp → Lỗi ✓
   4️⃣ Mật khẩu < 8 ký tự → Lỗi ✓
   5️⃣ Đăng nhập với email + mật khẩu đúng ✓
   6️⃣ Đăng nhập email sai → Lỗi ✓
   7️⃣ Đăng nhập mật khẩu sai → Lỗi ✓
   8️⃣ Nhấn "Ghi nhớ tôi" → Session tồn tại ✓
   9️⃣ Đăng xuất → Chuyển về trang đăng nhập ✓
   🔟 Test responsive trên mobile ✓


🎨 TỰY CHỈNH THÊM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Thay đổi file: SPA/static/css/auth.css

   Màu sắc:
   - --primary-color: #667eea → Thay bằng màu khác
   - --secondary-color: #764ba2 → Thay bằng màu khác

   Font:
   - Thay đổi trong login.html & register.html


📞 LIÊN HỆ HỖ TRỢ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ❓ Không chạy được?
   → Kiểm tra: python manage.py migrate
   → Kiểm tra: cd vào thư mục SPA
   → Kiểm tra: port 8000 có bị chiếm không?

   ❓ 404 Not Found?
   → URL có chính xác không?
   → Templates có ở thư mục templates không?

   ❓ Form không hiển thị?
   → Templates có CSS chưa?
   → Static files có load chưa?


╔════════════════════════════════════════════════════════════════════════════╗
║                    ✨ Chúc bạn sử dụng vui vẻ! ✨                        ║
║                 Tạo bởi: GitHub Copilot - 14/04/2026                     ║
╚════════════════════════════════════════════════════════════════════════════╝
""")

# Liệt kê các file đã tạo
print("\n📁 CÁC FILE ĐÃ TẠO/CẬP NHẬT:\n")

files = [
    ("SPA/forms.py", "TẠOMỚI", "Form đăng nhập & đăng ký"),
    ("SPA/views.py", "CẬP NHẬT", "Views cho auth (login/register/logout)"),
    ("SPA/urls.py", "CẬP NHẬT", "URLs cho auth endpoints"),
    ("templates/login.html", "TẠOMỚI", "Template trang đăng nhập"),
    ("templates/register.html", "TẠOMỚI", "Template trang đăng ký"),
    ("static/css/auth.css", "TẠOMỚI", "Stylesheet bổ sung"),
    ("SPA/settings.py", "CẬP NHẬT", "Messages & i18n config"),
    ("README_AUTH.md", "TẠOMỚI", "Tài liệu hướng dẫn"),
]

for file, status, desc in files:
    status_icon = "🟢" if status == "TẠOMỚI" else "🔵"
    print(f"  {status_icon} [{status:6}] {file:30} - {desc}")

print("\n")

