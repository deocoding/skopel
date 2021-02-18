#  PANDUAN PEMBUATAN APLIKASI SKOPEL SMA3

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
### INSTALL DJANGO
* Install django
    ```
    pip install django
    ```
* Buat proyek baru
    ```
    django-admin startproject <nama_proyek> .
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