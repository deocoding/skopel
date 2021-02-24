from django.db import models


class Jabatan(models.Model):
    nama = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nama
    
    # Menampilkan Pengajar bukan Pengajars
    class Meta:
        verbose_name_plural = "      Jabatan"


class Pengajar(models.Model):
    # JABATAN = (
    #     ('Kepala Sekolah', 'Kepala Sekolah'),
    #     ('Wakil Kepala Sekolah Bidang Kesiswaan', 'Wakil Kepala Sekolah Bidang Kesiswaan'),
    #     ('Pembina Osis', 'Pembina Osis'),
    #     ('Wali Kelas', 'Wali Kelas'),
    #     ('Guru Mapel', 'Guru Mapel'),
    #     ('Guru BK', 'Guru BK'),
    # )
    STATUS = (
        ('PNS', 'PNS'),
        ('Guru Tidak Tetap', 'Guru Tidak Tetap'),
        ('Guru Honorer', 'Guru Honorer'),
        ('Lainnya', 'Lainnya')
    )

    nama = models.CharField(max_length=200, null=True)
    nip = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    jabatan = models.ManyToManyField(Jabatan)
    # jabatan = models.CharField(max_length=200, null=True, choices=JABATAN)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
    
    # Menampilkan Pengajar bukan Pengajars
    class Meta:
        verbose_name_plural = "    Pengajar"

class Kelas(models.Model):
    nama = models.CharField(max_length=200, null=True)
    wali = models.ForeignKey(Pengajar, null=True, on_delete=models.SET_NULL, related_name='wali')
    bk = models.ForeignKey(Pengajar, null=True, on_delete=models.SET_NULL, related_name='bk')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "   Kelas"

class Siswa(models.Model):
    KELAMIN = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    )

    nama = models.CharField(max_length=200, null=True)
    nisn = models.CharField(max_length=200, null=True)
    kelamin = models.CharField(max_length=200, null=True, choices=KELAMIN)
    kelas = models.ForeignKey(Kelas, null=True, on_delete=models.SET_NULL)
    # ibu = models.CharField(max_length=200, null=True, blank=True)
    # ayah = models.CharField(max_length=200, null=True, blank=True)
    # wali = models.CharField(max_length=200, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "  Siswa"

class Pasal(models.Model):
    nama = models.CharField(max_length=200, null=True, unique=True)
    jenis = models.CharField(max_length=200, null=True, unique=True)
    skor = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = " Pasal"

class Pelanggaran(models.Model):
    STATUS = (
        ('Verifikasi', 'Verifikasi'),
        ('Terbukti', 'Terbukti'),
        ('Tidak Terbukti', 'Tidak Terbukti')
    )

    pengajar = models.ForeignKey(Pengajar, null=True, on_delete=models.SET_NULL)
    siswa = models.ForeignKey(Siswa, null=True, on_delete=models.SET_NULL)
    pasal = models.ForeignKey(Pasal, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    keterangan = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Pelanggaran"

    def __str__(self):
        return self.siswa.nama
