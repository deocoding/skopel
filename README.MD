#  PANDUAN PEMBUATAN APLIKASI SKOPEL SMA3
### PANDUAN GIT
* Sebelum cloning dari repo hapus folder proyek dan semua file didalamnya
    ```
    sudo rm -rfv <nama_proyek>
    ```
* Clone dari repo online
    ```
    git clone <link_ssh_git>
    ```
* Lihat status tambah/ubah/hapus data
    ```
    git status
    ```
* Menambahkan status lokal
    ```
    git add .
    ```
* Konfirmasi simpan data lokal
    ```
    git commit -m "<dari:laptop/desktop/online>" -m "<deskripsi>"
    ```
* Upload perubahan ke repo online
    ```
    git push origin <nama_branch>
    ```
---
### UBAH GROUP FOLDER 
* Arahkan ke folder proyek
    ```
    cd /path/to/repo.git
    ```
* Ubah grup folder (root/user) 
    ```
    sudo chgrp -R groupname .
    ```
* Ubah kapabilitas
    ```
    sudo chmod -R g+rwX .
    ```
* Ganti semua folder dan file
    ```
    find . -type d -exec chmod g+s '{}' +
    ```
* Ganti hak akses user pada folder proyek
    ```
    sudo chown -R $(whoami) <nama_proyek>
    ```
---
### BUAT FOLDER PROYEK
* Buat folder proyek
    ```
    mkdir <nama_proyek>
    ```
* Masuk ke folder proyek
    ```
    cd <nama_proyek>
    ```
---
### BUAT KOTAK VIRTUAL UNTUK MENYIMPAN DEPENDENSI SECARA LOKAL
* Install paket venv python3
    ```
    apt-get install python3-venv
    ```
* Install venv pada folder proyek
    ```
    python3 -m venv env
    ```
* Aktifkan venv
    ```
    source env/bin/activate
    ```
---
### INSTALL & PENGGUNAAN DJANGO
* Install django
    ```
    pip install django
    ```
* Buat proyek baru
    ```
    django-admin startproject <nama_proyek> .
    ```
* Menjalankan server pada localhost dengan port 8080
    ```
    python3 manage.py runserver 0.0.0.0:8080
    ```
* Buat app baru
    ```
    python3 manage.py startapp <nama_app>
    ```
* Tambahkan app baru pada settings.py agar dapat digunakan
    ```
    nano <nama_proyek>/settings.py
    ```
    Tambah di baris akhir:
    ```
    INSTALLED_APPS = ['<nama_app>']
    ```
* Ubah <nama_app>/views.py 
    ```bash
    from django.shortcuts import render

    def home(request):
        pass

    def products(request):
        pass

    def costumer(request):
        pass
    ```
* Buat file <nama_app>/urls.py, tambahkan:
    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home),
        path('pelanggarans/', views.pelanggarans),
        path('murid/', views.murid),
        path('guru/', views.guru),
    ]
    ```
* Edit <nama_proyek>/urls.py
    ```
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('skor.urls')),
    ]
    ```
* Tambah 4 file html dan edit <nama_app>/views.py

    dashboard.html
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SKOPEL SMA3</title>
    </head>
    <body>
        <h1>Dashboard</h1>
    </body>
    </html>
    ```
    <nama_app>/views.py
    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    def home(request):
        return render(request, 'skor/dashboard.html')

    def pelanggarans(request):
        return render(request, 'skor/pelanggarans.html')

    def murid(request):
        return render(request, 'skor/murid.html')

    def guru(request):
        return render(request, 'skor/guru.html')
    ```
* Tambah base.html sebagai template & ubah file html yang dibuat sebelumnya

    base.html
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SKOPEL SMA3</title>
    </head>
    <body>
        <h1>Navbar</h1>
        <hr>

        {% block content %} 
        
        
        
        {% endblock %}

        <hr>
        <h5>Our footer</h5>
    </body>
    </html>
    ```
    dashboard.html
    ```
    {% extends 'skor/base.html' %}

    {% block content %}
        <h1>Dashboard</h1>
    {% endblock %}
    ```
* Tambah navbar.html & ubah file base.html

    navbar.html
    ```
    <h1>Navbar</h1>
    <hr>
    ```
    base.html
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SKOPEL SMA3</title>
    </head>
    <body>
        
        {% include 'skor/navbar.html' %}

        {% block content %}          
        
        {% endblock %}

        <hr>
        <h5>Our footer</h5>
    </body>
    </html>
    ```
* Ganti semua isi navbar.html dengan kode dari navbar bootstrap 4 (cari di google)
* Tambah bootstrap 4 css min di base.html (cari di google)
* Buat folder <nama_proyek>/static dengan sub folder css, js, images
* Tambahkan baris perintah berikut pada settings.py 
    ```
    MEDIA_URL = '/images/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    ```
* Tambahkan baris perintah berikut untuk melink file static
    ```
    {% load static %}
    ```
* Tambahkan baris perintah berikut untuk memanggil file static berupa gambar
    ```
    <img src="{% static 'images/logo.png' %}">
    ```
* Tambahkan baris perintah berikut untuk memanggil file static berupa css dan js
    ```
    <link rel="stylesheet" type="text/css" href="{% static '/css/main.css' %}">
    ```
* edit model.py untuk membuat tabel database
    ```
    from django.db import models

    class Pengajar(models.Model):
        JABATAN = (
            ('Kepala Sekolah', 'Kepala Sekolah'),
            ('Wakil Kepala Sekolah Bidang Kesiswaan', 'Wakil Kepala Sekolah Bidang Kesiswaan'),
            ('Pembina Osis', 'Pembina Osis'),
            ('Guru Kelas', 'Guru Kelas'),
            ('Guru BK', 'Guru BK'),
        )

        nama = models.CharField(max_length=200, null=True)
        nip = models.CharField(max_length=200, null=True)
        jabatan = models.CharField(max_length=200, null=True, choices=JABATAN)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.nama
        
        # Menampilkan Pengajar bukan Pengajars
        class Meta:
            verbose_name_plural = "Pengajar"

    class Kelas(models.Model):
        nama = models.CharField(max_length=200, null=True)
        wali = models.ForeignKey(Pengajar, null=True, on_delete=models.SET_NULL, related_name='wali')
        bk = models.ForeignKey(Pengajar, null=True, on_delete=models.SET_NULL, related_name='bk')
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.nama

        class Meta:
            verbose_name_plural = "Kelas"

    class Siswa(models.Model):
        nama = models.CharField(max_length=200, null=True)
        nisn = models.CharField(max_length=200, null=True)
        kelas = models.ForeignKey(Kelas, null=True, on_delete=models.SET_NULL)
        ibu = models.CharField(max_length=200, null=True, blank=True)
        ayah = models.CharField(max_length=200, null=True, blank=True)
        wali = models.CharField(max_length=200, null=True, blank=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.nama

        class Meta:
            verbose_name_plural = "Siswa"

    class Pasal(models.Model):
        nama = models.CharField(max_length=200, null=True, unique=True)
        jenis = models.CharField(max_length=200, null=True, unique=True)
        skor = models.IntegerField(null=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return self.nama
        
        class Meta:
            verbose_name_plural = "Pasal"

    class Pelanggaran(models.Model):
        STATUS = (
            ('Verifikasi', 'Verifikasi'),
            ('Terbukti', 'Terbukti')
        )

        siswa = models.ForeignKey(Siswa, null=True, on_delete=models.SET_NULL)
        pasal = models.ForeignKey(Pasal, null=True, on_delete=models.SET_NULL)
        status = models.CharField(max_length=200, null=True, choices=STATUS)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

        class Meta:
            verbose_name_plural = "Pelanggaran"
    ```
* Edit admin.py agar tabel yang baru dibuat dapat ditampilkan pada halaman admin
    ```
    from django.contrib import admin
    from .models import *

    admin.site.register(Pengajar)
    admin.site.register(Kelas)
    admin.site.register(Siswa)
    admin.site.register(Pasal)
    admin.site.register(Pelanggaran)
    ```