
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
7. Membangun template HTML
Template HTML yang akan dibangun terdiri dari sejumlah komponen, antara lain
- Header berupa judur dan tagline
- Name: (berisi nama produk)
- Amount: (berisi jumlah produk dalam lusin)
- Description: (berisi PT pemasok)
- Date in: (berisi tanggal pasokan terakhir datang)
- Stock less than 5 days: (berisi keterangan apakah pasokan akan habis kurang dari lima hari lagi)
- Categories: (berisi keterangan jenis product)
8. Mengimplementasikan Models dan Melakukan Migrate
Komponen models adalah sebagai berikut
- name: character, length <= 25.
- amount: integer, default = 0.  
- description: text, default = "".
- date_in: date.
- stock: boolean, default = 0.
- categories: character, length <=100, default = "uncategorized".<br/>
Setelah semua komponen dibangun, maka jalankan perintah
```python manage.py makemigrations```
dan
```python manage.py migrate```
untuk mengimplementasikan model ke basis data.
9. Membangun fungsi show_main untuk mengintegrasikan
Untuk menghubungkan antara _view_ dan _template_, pertama kita harus memastikan pada views.py. telah dilakukan import render dengan cara menambahkan baris ```from django.shortcuts import render```. Lalu, setelah melakukan import, saya membangun fungsi show_main dengan cara
```
def show_main(request):
    context = {
        'name' : "Aqua",
        'amount' : 12,
        'description': 'PT. Danone',
        'date_in': date.today(),
        'stock': True,
        'categories': 'Beverages',
    }
    return render(request, "main.html", context)
```
10. Mengonfigurasi routing URL <br/>
Di dalam direktori main, saya membuat sebuah  file bernama urls.py yang berisi
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
11. Membangun unit test
Untuk memastikan bahwa program yang telah dibangun akan berjalan sebagaimana mestinya, maka akan dibangun sebuah unit test. ...

## Bagan Request Client 
![Diagram](https://github.com/bryanjeshua/jeshuamart/blob/master/DIAGRAM%20MVT.png?raw=true)

## Why do we need virtual environment?
Kita membutuhkan _virtual environment_ untuk melokalisir pengaturan sejumlah depedency yang  dengan  proyek kita sehingga bila kedepannya terdapat sejumlah proyek yang membutuhkan sejumlah library/framework yang sama, tidak terjadi _conflict_ terhadap versi suatu library yang mampu membuat program tidak berjalan sebagaimana mestinya.
## Perbedaan antara MVC, MVT, MVVM
