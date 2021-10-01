from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDB

class userForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'ชื่อจริง', 'class': 'input'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'นามสกุล', 'class': 'input'})
        self.fields['username'].widget.attrs.update({'placeholder': 'ชื่อบัญชี', 'class': 'input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'อีเมล', 'class': 'input'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'รหัสผ่าน', 'class': 'input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'ยืนยันรหัสผ่าน', 'class': 'input'})

    class Meta:
        model = UserDB
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
