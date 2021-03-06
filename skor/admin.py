from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import *

# admin.site.register(Pengajar)
# admin.site.register(Siswa)
# admin.site.register(Pasal)
# admin.site.register(Pelanggaran)

@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    # list_display = ("nama")
    search_fields = ("nama",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nama"].label = "Jabatan"
        return form

@admin.register(Pengajar)
class PengajarAdmin(admin.ModelAdmin):
    # list_display = ("nama", "nip", "jabatan")
    list_display = ("nama", "nip")
    search_fields = ("nama", "nip", )

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

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ("nama", "nisn", "kelas")
    search_fields = ("nama__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nama"].label = "Nama Siswa"
        form.base_fields["nisn"].label = "NISN"
        form.base_fields["kelas"].label = "Kelas"
        return form

@admin.register(Pasal)
class PasalAdmin(admin.ModelAdmin):
    list_display = ("nama", "jenis", "skor")
    search_fields = ("jenis__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["nama"].label = "Pasal"
        form.base_fields["jenis"].label = "Jenis Pelanggaran"
        form.base_fields["skor"].label = "Skor"
        return form

@admin.register(Pelanggaran)
class PelanggaranAdmin(admin.ModelAdmin):
    list_display = ("siswa", "pasal", "status")
    search_fields = ("jenis__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["siswa"].label = "Nama Siswa"
        form.base_fields["pasal"].label = "Pasal Pelanggaran"
        form.base_fields["status"].label = "Status"
        return form