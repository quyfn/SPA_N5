from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from services.models import CustomerProfile


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập email của bạn",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập mật khẩu",
                "required": True,
            }
        ),
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập email của bạn",
                "required": True,
            }
        ),
    )
    first_name = forms.CharField(
        label="Tên",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập tên của bạn",
                "required": True,
            }
        ),
    )
    last_name = forms.CharField(
        label="Họ",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập họ của bạn",
                "required": False,
            }
        ),
    )
    password1 = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập mật khẩu (ít nhất 8 ký tự)",
                "required": True,
            }
        ),
    )
    password2 = forms.CharField(
        label="Xác nhận mật khẩu",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Nhập lại mật khẩu",
                "required": True,
            }
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email này đã được đăng ký. Vui lòng sử dụng email khác.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Mật khẩu không khớp.")
        return password2


class CustomerProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Họ và tên",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "account-input",
                "placeholder": "Nhập họ và tên",
            }
        ),
    )

    class Meta:
        model = CustomerProfile
        fields = ("full_name", "phone", "birth_date", "address", "notes")
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "class": "account-input",
                    "placeholder": "Nhập số điện thoại",
                }
            ),
            "birth_date": forms.DateInput(
                attrs={
                    "class": "account-input",
                    "type": "date",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "account-input",
                    "placeholder": "Nhập địa chỉ",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "account-input account-textarea",
                    "rows": 3,
                    "placeholder": "Thông tin sức khỏe, sở thích điều trị, lưu ý đặc biệt...",
                }
            ),
        }
