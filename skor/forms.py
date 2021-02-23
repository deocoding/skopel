from django.forms import ModelForm, fields
from .models import Pelanggaran


class PelanggaranForm(ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'