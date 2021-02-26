from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Pelanggaran, Pengajar


class PengajarForm(ModelForm):
    class Meta:
        model = Pengajar
        fields = '__all__'
        exclude = ['user']


class PelanggaranForm(ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'


class BuatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
