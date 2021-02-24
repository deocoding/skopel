import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class PelanggaranFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    keterangan = CharFilter(field_name='keterangan', lookup_expr='icontains')
    class Meta:
        model = Pelanggaran
        fields = '__all__'
        exclude = ['pengajar', 'date_created']