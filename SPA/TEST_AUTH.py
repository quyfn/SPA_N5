"""
Test script để kiểm tra login/register functionality
Chạy: python manage.py shell < TEST_AUTH.py
"""

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

# Tạo test client
client = Client()

print("\n" + "="*50)
print("🧪 TEST AUTH SYSTEM")
print("="*50)

# Test 1: Kiểm tra URL routes
print("\n✓ Test 1: Kiểm tra URL routes")
try:
    login_url = reverse('user_login')
    register_url = reverse('user_register')
    print(f"  ✅ Login URL: {login_url}")
    print(f"  ✅ Register URL: {register_url}")
except Exception as e:
    print(f"  ❌ Lỗi: {e}")

# Test 2: Truy cập trang login
print("\n✓ Test 2: Truy cập trang login")
try:
    response = client.get('/login/')
    if response.status_code == 200:
        print(f"  ✅ Status: {response.status_code} - OK")
    else:
        print(f"  ❌ Status: {response.status_code}")
except Exception as e:
    print(f"  ❌ Lỗi: {e}")

# Test 3: Truy cập trang register
print("\n✓ Test 3: Truy cập trang register")
try:
    response = client.get('/register/')
    if response.status_code == 200:
        print(f"  ✅ Status: {response.status_code} - OK")
    else:
        print(f"  ❌ Status: {response.status_code}")
except Exception as e:
    print(f"  ❌ Lỗi: {e}")

# Test 4: Thử đăng ký người dùng
print("\n✓ Test 4: Thử đăng ký người dùng")
try:
    # Xóa user test nếu tồn tại
    User.objects.filter(email='test@example.com').delete()

    response = client.post('/register/', {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'test@example.com',
        'password1': 'Test@Password123',
        'password2': 'Test@Password123',
    })

    if User.objects.filter(email='test@example.com').exists():
        print(f"  ✅ Đăng ký thành công!")
    else:
        print(f"  ⚠️  Đăng ký chưa thành công")
except Exception as e:
    print(f"  ❌ Lỗi: {e}")

# Test 5: Thử đăng nhập
print("\n✓ Test 5: Thử đăng nhập")
try:
    response = client.post('/login/', {
        'email': 'test@example.com',
        'password': 'Test@Password123',
    })

    if response.wsgi_request.user.is_authenticated:
        print(f"  ✅ Đăng nhập thành công!")
    else:
        print(f"  ⚠️  Đăng nhập chưa thành công - Check form validation")
except Exception as e:
    print(f"  ❌ Lỗi: {e}")

print("\n" + "="*50)
print("🎉 Kiểm tra hoàn thành!")
print("="*50 + "\n")

