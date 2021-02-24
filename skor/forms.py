from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Pelanggaran


class PelanggaranForm(ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'


class BuatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
