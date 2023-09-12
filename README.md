
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
1. Membangun repository github yang baru<br/>
Repository yang baru dibangun dengan nama **jeshuamart** akan menjadi sarana deployment aplikasi pada adaptable. Ini dilakukan dengan cara membangun folder yang sama dengan nama repositorynya, kemudian menuliskan perintah ```git init``` kemudian ```git branch -M main``` lalu ```git remote add origin https://github.com/bryanjeshua/jeshuamart```
2. Mendeploy virtual environment<br/>
Fungsi virtual environment adalah ... . Dalam melakukan deployment, kita menjalankan skrip ```python -m venv env```, setelah itu kita mengaktivasi virtual environment tersebut dengan menjalankan skrip ```env\Scripts\activate``` pada direktori repositori.
3. Menginstal django<br/>
Sesuai dengan tutorial, peng-_instal_-an dilaksanakan dengan menuliskan sejumlah komponen library pada requirements.txt dan kemudian menjalankan perintah ```pip install -r requirements.txt```.  
4. Membuat proyek django<br/>
Proyek django yang baru dibuat dengan menjalankan skrip ```django-admin startproject jeshuamart .```
5. Mengatur _allowed host_<br/>
Melalui penambahan "*" pada ```ALLOWED_HOST``` di ```settings.py```, saya mengizinkan semua host untuk mengakses aplikasi ini secara luas.
6. Membuat aplikasi main<br/>
Dengan menjalankan perintah ```python manage.py startapp main```, maka akan terbangun direktori main. Lalu, pada ```settings.py``` kita menambahkan ```main,``` pada ```INSTALLED_APPS```
7. Membangun template HTML<br/>
Template HTML yang akan dibangun terdiri dari sejumlah komponen, antara lain
- Header berupa judur dan tagline
- Name: (berisi nama produk)
- Amount: (berisi jumlah produk dalam lusin)
- Description: (berisi PT pemasok)
- Date in: (berisi tanggal pasokan terakhir datang)
- Stock less than 5 days: (berisi keterangan apakah pasokan akan habis kurang dari lima hari lagi)
- Categories: (berisi keterangan jenis product)
8. Mengimplementasikan Models dan Melakukan Migrate<br/>
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
9. Membangun fungsi show_main untuk mengintegrasikan<br/>
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
11. Membangun unit test<br/>
Untuk memastikan bahwa program yang telah dibangun akan berjalan sebagaimana mestinya, maka akan dibangun sebuah unit test. ...

## Bagan Request Client 
![Diagram](https://github.com/bryanjeshua/jeshuamart/blob/master/DIAGRAM%20MVT.png?raw=true)
Dari gambar di atas dapat ditarik sebuah kesimpulan yakni dalam aplikasi Django, ketika ada http request, maka urls.py akan meneruskannya menuju kepada views.py yang sesuai. Kemudian views.py akan melakukan ragam perintah yang dilakukan, misalnya melakukan read/write data dengan berinteraksi dengan models.py, kemudian main.html akan melakukan pengaturan tampilan yang sesuai terhadap data/komponen yang akan ditampilkan. Setelah itu, maka akan dikirimkan http response berupa file html kepada pengguna.
## Why do we need virtual environment?
Kita membutuhkan _virtual environment_ untuk melokalisir pengaturan sejumlah depedency yang  dengan  proyek kita sehingga bila kedepannya terdapat sejumlah proyek yang membutuhkan sejumlah library/framework yang sama, tidak terjadi _conflict_ terhadap versi suatu library yang mampu membuat program tidak berjalan sebagaimana mestinya.
## Perbedaan antara MVC, MVT, MVVM
MVT merupakan pola pengembangan arsitektur yang digunakan di _web development_ yang berkaitan erat dengan framework web pada python seperti Django. Terdapat tiga komponen yakni Model (yang merepresentasikan data dan logika utama aplikasi, termasuk membaca dan menyimpan data), View (yang mengatur bagaimana data yang dimiliki akan ditayangkan), Template (yang berfungsi mengatur layout halaman web untuk ditayangkan).
MVC merupakan pola pengembangan arsitektur yang digunakan DALAM _software development_  terutama dalam membangun GUI dan website, dan terdiri atas tiga komponen yakni Model, View (berisi pengaturan layer presentasi data yang didapat dari model, termasuk pengaturan button, forms, dan beragam komponen lainnya), dan Controller (menghubungkan model dan view, misalnya mengelola input dari user pada view untuk diteruskan ke model)
MVVM merupakan pola pengembangan arsitektur yang berkaitan erat dengan pengembangan GUI terutama pada ragam aplikasi yang membutuhkan data binding. MVVM terdiri atas tiga komponen yakni Model, View (bertugas untuk menampilkan data terhadap user dan menangkap interaksi dari user), dan ViewModel (bertugas menghubungkan model dan view, menunjukan data dan perintah yang dapat view gunakan untuk melakukan data binding, dan menyederhanakan tampilan data dari model agar view lebih mudah untuk menampilkannya tanpa berisi logika tampilan antarmukanya)

Perbedaan ketiganya terdapat pada cara mereka mengatur hubungan antara model, view, dan komponen perantaranya (baik template, controller, maupun viewmodel). MVT menggunakan template sebagai perantara model dan view dan bertugas menggambarkan struktur dari halaman web. MVC menggunakan controller untuk mengatur input dari user dan mengelola alur data. Sedangkan, MVVM menggunakan ViewModel sebagai perantara yang mengelola tampilan data yang akan ditampilkan ke view dan mengelola interaksi user.
