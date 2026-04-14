#!/usr/bin/env python
"""
Quick Check Script - Kiểm tra tất cả các thành phần của hệ thống Auth
Chạy: python check_system.py
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SPA.settings')
django.setup()

from django.urls import reverse
from django.template.loader import get_template
from SPA.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

print("\n" + "="*60)
print("  🔍 SYSTEM CHECK - SPA LOGIN/REGISTER")
print("="*60)

# 1. Check URLs
print("\n✓ CHECKING URLS...")
url_patterns = {
    'Login': 'user_login',
    'Register': 'user_register',
    'Logout': 'user_logout',
    'Dashboard': 'service_dashboard'
}

all_urls_ok = True
for name, pattern in url_patterns.items():
    try:
        url = reverse(pattern)
        print(f"  ✅ {name:15} → {url}")
    except Exception as e:
        print(f"  ❌ {name:15} → ERROR")
        all_urls_ok = False

# 2. Check Templates
print("\n✓ CHECKING TEMPLATES...")
templates = ['login.html', 'register.html']
all_templates_ok = True

for template in templates:
    try:
        get_template(template)
        print(f"  ✅ {template}")
    except Exception as e:
        print(f"  ❌ {template} - {str(e)[:50]}")
        all_templates_ok = False

# 3. Check Forms
print("\n✓ CHECKING FORMS...")
try:
    login_form = LoginForm()
    print(f"  ✅ LoginForm fields: {list(login_form.fields.keys())}")
except Exception as e:
    print(f"  ❌ LoginForm - {e}")

try:
    register_form = RegisterForm()
    print(f"  ✅ RegisterForm fields: {list(register_form.fields.keys())}")
except Exception as e:
    print(f"  ❌ RegisterForm - {e}")

# 4. Check Database
print("\n✓ CHECKING DATABASE...")
try:
    user_count = User.objects.count()
    print(f"  ✅ Database connected (Users: {user_count})")
except Exception as e:
    print(f"  ❌ Database error - {e}")

# 5. Check Views
print("\n✓ CHECKING VIEWS...")
try:
    from SPA.views import user_login, user_register, user_logout
    print(f"  ✅ user_login function found")
    print(f"  ✅ user_register function found")
    print(f"  ✅ user_logout function found")
except Exception as e:
    print(f"  ❌ Views error - {e}")

# 6. Summary
print("\n" + "="*60)
if all_urls_ok and all_templates_ok:
    print("  ✅ ALL SYSTEMS GO! 🚀")
    print("  → Start server: python manage.py runserver")
    print("  → Login page: http://127.0.0.1:8000/login/")
else:
    print("  ⚠️  SOME ISSUES DETECTED")
    print("  → Check errors above")

print("="*60 + "\n")

