from django.contrib import admin

from .models import *

# admin.site.register(Kelas)
admin.site.register(Siswa)
admin.site.register(Pasal)
admin.site.register(Pelanggaran)

@admin.register(Pengajar)
class PengajarAdmin(admin.ModelAdmin):
    list_display = ("nama", "nip", "jabatan")
    search_fields = ("nama__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nip"].label = "NIP"
        return form

@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ("nama", "wali", "bk")
    search_fields = ("nama__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nama"].label = "Kelas"
        form.base_fields["wali"].label = "Wali Kelas"
        form.base_fields["bk"].label = "Guru BK"
        return form