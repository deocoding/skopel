from django.contrib import admin

from .models import *

admin.site.register(Kelas)
admin.site.register(Siswa)
admin.site.register(Pasal)
admin.site.register(Pelanggaran)

@admin.register(Pengajar)
class PengajarAdmin(admin.ModelAdmin):
    list_display = ("nama", "nip", "jabatan")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nip"].label = "NIP"
        return form