import django_filters

from .models import *

class PelanggaranFilter(django_filters.FilterSet):
    class Meta:
        model = Pelanggaran
        fields = '__all__'