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