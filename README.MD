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

### INSTALL DJANGO
1. pip install django

### UBAH GROUP FOLDER 
1. cd /path/to/repo.git
2. sudo chgrp -R groupname .
3. sudo chmod -R g+rwX .
4. find . -type d -exec chmod g+s '{}' +