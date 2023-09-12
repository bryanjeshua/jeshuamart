# Jeshuamart - _Sahabat Belanja Keluarga Anda!_
[Tautan menuju website](https://jeshuamart.adaptable.app/main/) <br/>
Nama    : Bryan Jeshua Mario Timung <br/>
NPM     : 2206027021 <br/>
Kelas   : PBP C <br/>
## Requirements
1. Python3
## Libraries Used
1. Django
2. Datetime
## How to Build
1. Membangun repository github yang baru
Repository yang baru dibangun dengan nama **jeshuamart** akan menjadi sarana deployment aplikasi pada adaptable. Ini dilakukan dengan cara membangun folder yang sama dengan nama repositorynya, kemudian menuliskan perintah ```git init``` kemudian ```git branch -M main``` lalu ```git remote add origin https://github.com/bryanjeshua/jeshuamart```
2. Mendeploy virtual environment
Fungsi virtual environment adalah ... . Dalam melakukan deployment, kita menjalankan skrip ```python -m venv env```, setelah itu kita mengaktivasi virtual environment tersebut dengan menjalankan skrip ```env\Scripts\activate``` pada direktori repositori.
3. Menginstal django
Sesuai dengan tutorial, peng-_instal_-an dilaksanakan dengan menuliskan sejumlah komponen library pada requirements.txt dan kemudian menjalankan perintah ```pip install -r requirements.txt```.  
4. Membuat proyek django
Proyek django yang baru dibuat dengan menjalankan skrip ```django-admin startproject jeshuamart .```
5. Mengatur _allowed host_
Melalui penambahan "*" pada ```ALLOWED_HOST``` di ```settings.py```, saya mengizinkan semua host untuk mengakses aplikasi ini secara luas.
6. Membuat aplikasi main
Dengan menjalankan perintah ```python manage.py startapp main```, maka akan terbangun direktori main. Lalu, pada ```settings.py``` kita menambahkan ```main,``` pada ```INSTALLED_APPS```
8. Membangun template HTML
Template
10. Mengimplementasikan Models dan Melakukan Migrate
Komponen models adalah sebagai berikut
Migrate 
11. Membangun fungsi show_main untuk mengintegrasikan
12. Mengonfigurasi routing URL
13. Membangun unit test
## Bagan Request Client 
...
## Why do we need virtual environment?
Kita membutuhkan _virtual environment_ untuk melokalisir pengaturan sejumlah library/framework yang dependent dengan  proyek kita sehingga bila kedepannya terdapat sejumlah proyek yang membutuhkan sejumlah library/framework yang sama, tidak terjadi _conflict_ yang mampu membuat program tidak berjalan sebagaimana mestinya
## Perbedaan antara MVC, MVT, MVVM
