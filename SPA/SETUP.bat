@echo off
REM Script cài đặt và khởi động hệ thống
REM Hệ thống Đăng Nhập & Đăng Ký Spa

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║     SETUP: Hệ Thống Đăng Nhập & Đăng Ký - SPA            ║
echo ║         Chạy script này lần đầu tiên                      ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Kiểm tra xem có ở đúng thư mục không
if not exist "manage.py" (
    echo ❌ ERROR: Không tìm thấy manage.py
    echo    Vui lòng chạy script này từ thư mục: SPA
    echo.
    echo Cách làm:
    echo   1. Mở Command Prompt
    echo   2. cd C:\Users\LENOVO\PycharmProjects\DjangoProject1\LAPTRINHWEB\SPA
    echo   3. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✓ Đã tìm thấy manage.py
echo.

REM Chạy migrations
echo 📋 Đang chạy migrations...
python manage.py migrate
if errorlevel 1 (
    echo ❌ ERROR: Migrations thất bại
    pause
    exit /b 1
)
echo ✓ Migrations hoàn thành
echo.

REM Tạo superuser (nếu cần)
echo 👤 Tạo tài khoản admin (nếu chưa có)
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@spa.com', 'admin123')
    print("✓ Tài khoản admin tạo thành công: admin/admin123")
else:
    print("✓ Tài khoản admin đã tồn tại")
EOF
echo.

echo ╔════════════════════════════════════════════════════════════╗
echo ║              ✨ SETUP HOÀN THÀNH ✨                       ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo 📋 BƯỚC TIẾP THEO:
echo.
echo 1️⃣  Chạy Django Server:
echo    python manage.py runserver
echo.
echo 2️⃣  Mở trình duyệt và truy cập:
echo    http://localhost:8000/register/    # Đăng ký
echo    http://localhost:8000/login/       # Đăng nhập
echo.
echo 3️⃣  Hoặc truy cập Admin:
echo    http://localhost:8000/admin/
echo    Username: admin
echo    Password: admin123
echo.
echo 📚 Xem tài liệu thêm:
echo    - README_AUTH.md         (Hướng dẫn chi tiết)
echo    - QUICK_START.md         (Bắt đầu nhanh)
echo    - PREVIEW.html           (Xem trước giao diện)
echo    - HUONG_DAN_TEST.py      (Hướng dẫn test)
echo.

pause

