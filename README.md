
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
Fungsi virtual environment adalah supaya library yang kita pakai senantiasa konsisten, baik versi dan pengaturan lainnya. Dalam melakukan deployment virtual environment, kita menjalankan skrip ```python -m venv env```, setelah itu kita mengaktivasi virtual environment tersebut dengan menjalankan skrip ```env\Scripts\activate``` pada direktori repositori.
3. Menginstal django<br/>
Sesuai dengan tutorial, peng-_instal_-an dilaksanakan dengan menuliskan sejumlah komponen library pada requirements.txt dan kemudian menjalankan perintah ```pip install -r requirements.txt```.  
4. Membuat proyek django<br/>
Proyek django yang baru dibuat dengan menjalankan skrip ```django-admin startproject jeshuamart .```
5. Mengatur _allowed host_<br/>
Melalui penambahan "*" pada ```ALLOWED_HOST``` di ```settings.py```, saya mengizinkan semua host untuk mengakses aplikasi ini secara luas.
6. Membuat aplikasi main<br/>
Dengan menjalankan perintah ```python manage.py startapp main```, maka akan terbangun direktori main. Lalu, pada ```settings.py``` kita menambahkan ```main,``` pada ```INSTALLED_APPS```
7. Membangun template HTML<br/>
Template HTML yang akan dibangun pada direktori ```templates``` di dalam ```main``` terdiri dari sejumlah komponen, antara lain
- Header berupa judur dan tagline
- Name: (berisi nama produk)
- Amount: (berisi jumlah produk dalam lusin)
- Description: (berisi PT pemasok)
- Date in: (berisi tanggal pasokan terakhir datang)
- Stock less than 5 days: (berisi keterangan apakah pasokan akan habis kurang dari lima hari lagi)
- Categories: (berisi keterangan jenis product)
- Identitas nama dan NPM
8. Mengimplementasikan Models dan Melakukan Migrate<br/>
Komponen models pada ```models.py``` dalam direktori main yang hendak diatur adalah sebagai berikut
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
untuk mengimplementasikan model yang baru tersebut ke basis data.
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
10. Mengonfigurasi routing URL dalam aplikasi main<br/>
Di dalam direktori ```main```, saya membuat sebuah file bernama ```urls.py``` sehingga fungsi yang dipetakan ```views.py``` tepat sasaran. File ini  berisi
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
11. Mengonfirmasi routing URL proyek<br/>
Di dalam direktori ```jeshuamart```, saya mengimpor fungsi ```include``` dari ```django.urls```, dan menambahkan ```path('main/', include('main.urls')),``` pada ```url_patterns``` sehingga rute URL tingkat proyek dapat mengimpor rute URL dari aplikasi-aplikasi (yang terdapat di ```urls.py``` masing-masing) sehingga aplikasi django lebih modular.
12. Membangun unit test<br/>
Untuk memastikan bahwa program yang telah dibangun akan berjalan sebagaimana mestinya, maka akan dibangun sebuah unit test. Unit test yang dibangun ada dua, yang pertama untuk memastikan path URL dapat diakses, dan yang kedua yakni untuk mengetes apakah template ```main.html``` telah berhasil diterapkan pada halaman ```/main/``` yang sudah dirender
13. Melakukan deployment ke github<br/>
Semua perubahan akan ditambahkan dengan menjalankan perintah ```git add .```, lalu lakukan commit dengan menjalankan perintah ```git commit -m "deployment app"```, dan lakukan push ke repository dengan menjalankan instruksi```git push origin master```.
14. Melakukan deployment ke adaptable<br/>
Setelah aplikasi telah berjalan di local machine dan telah di-deploy di github, deployment dilakukan melalui adaptable dengan menghubungkan adaptable kepada existing repository, dalam kasus ini ialah repository jeshuamart. Branch yang sesuai dipilih, dengan pengaturan python app template sebagai app template  postgresql sebagai database template, lalu versi python sesuai projek dipilih (dalam kasus ini 3.11) dan deployment command ```python manage.py migrate && gunicorn jeshuamart.wsgi``` dimasukkan.
## Bagan Request Client 
![Diagram](https://github.com/bryanjeshua/jeshuamart/blob/master/DIAGRAM%20MVT.png?raw=true)
Dari gambar di atas dapat ditarik sebuah kesimpulan yakni dalam aplikasi Django, ketika ada http request, maka urls.py akan meneruskannya menuju kepada views.py yang sesuai. Kemudian views.py akan melakukan ragam perintah yang dilakukan, misalnya melakukan read/write data dengan berinteraksi dengan models.py, kemudian main.html akan melakukan pengaturan tampilan yang sesuai terhadap data/komponen yang akan ditampilkan. Setelah itu, maka akan dikirimkan http response berupa file html kepada pengguna oleh views.py.
## Why do we need virtual environment?
Kita membutuhkan _virtual environment_ untuk melokalisir pengaturan sejumlah depedency yang berhubungan dengan  proyek kita sehingga bila kedepannya terdapat sejumlah proyek yang membutuhkan sejumlah library/framework yang sama, tidak terjadi _conflict_ terhadap versi maupun pengaturan suatu library yang mampu membuat program tidak berjalan sebagaimana mestinya.
## Perbedaan antara MVC, MVT, MVVM
MVT merupakan pola pengembangan arsitektur yang digunakan di _web development_ yang berkaitan erat dengan framework web pada python seperti Django. Terdapat tiga komponen yakni Model (yang merepresentasikan data dan logika utama aplikasi, termasuk membaca dan menyimpan data), View (yang mengatur bagaimana data yang dimiliki akan ditayangkan), Template (yang berfungsi mengatur layout halaman web untuk ditayangkan).
MVC merupakan pola pengembangan arsitektur yang digunakan dalam _software development_  terutama dalam membangun GUI dan website, dan terdiri atas tiga komponen yakni Model, View (berisi pengaturan layer presentasi data yang didapat dari model, termasuk pengaturan button, forms, dan beragam komponen lainnya), dan Controller (menghubungkan model dan view, misalnya mengelola input dari user pada view untuk diteruskan ke model)
MVVM merupakan pola pengembangan arsitektur yang berkaitan erat dengan pengembangan GUI terutama pada ragam aplikasi yang membutuhkan data binding. MVVM terdiri atas tiga komponen yakni Model, View (bertugas untuk menampilkan data terhadap user dan menangkap interaksi dari user), dan ViewModel (bertugas menghubungkan model dan view, menunjukan data dan perintah yang dapat view gunakan untuk melakukan data binding, dan menyederhanakan tampilan data dari model agar view lebih mudah untuk menampilkannya tanpa berisi logika tampilan antarmukanya)

Perbedaan ketiganya terdapat pada cara mereka mengatur hubungan antara model, view, dan komponen perantaranya (baik template, controller, maupun viewmodel). MVT menggunakan template sebagai perantara model dan view dan bertugas menggambarkan struktur dari halaman web. MVC menggunakan controller untuk menghubungkan model dan view, mengatur input dari user, dan mengelola alur data. Sedangkan, MVVM menggunakan ViewModel sebagai perantara yang mengelola tampilan data yang akan ditampilkan ke view dan mengelola interaksi user.
## Apa perbedaan antara form POST dan form GET dalam Django?
Perbedaan antara form POST dan form GET dalam Django adalah sebagai berikut
<br/>POST :
- Ketika menggunakan metode POST, data form dikirimkan sebagai bagian dari HTTP Request Body, bukan sebagai parameter query dalam URLnya. Metode ini lebih aman jika dibandingkan dengan GET karena data tersebut tidak terlihat di URL sehingga jauh lebih aman untuk mengirimkan informasi sensitif seperti password.
- Metode POST dapat mengolah data dalam jumlah besar jika dibandingkan dengan GET sehingga jauh lebih disarankan jika ingin melibatkan data submission.
<br/>GET :
- Ketika menggunakan metode GET, data dari form akan dikirimkan sebagai parameter query pada URL. Biasanya, metode ini digunakan ketika kita hendak mengakses data dari server atau ketika kita hendak melakukan operasi hanya membaca. Metode ini juga cocok untuk melakukan pencarian forms sederhana. 
- Data ini dapat dilihat pada URL. Ini menyebabkan informasi menjadi kurang aman dan membatasi jumlah data yang dapat dikirimkan.
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan utama antara XML, JSON, dan HTML adalah sebagai berikut
- XML = menggunakan tag (serupa dengan HTML) akan tetapi dapat didefinisikan user. Tidak memiliki tipe data dan memperlakukan semuanya sebagai text. Jauh lebih mudah dibaca orang. Cocok untuk dokumen yang rumit, termasuk pertukaran data yang tidak mendukung JSON.
- JSON = Menggunakan pasangan key dan value, mendukung tipe data string, number, booleans, array, dan object. Kurang deskriptif jika dibandingkan dengan XML. Ukurannya lebih kecil. Umum digunakan pada web applications, APIs, dan file konfigurasi.0 
- HTML = Menggunakan tags yang sudah didefinisikan sebelumnya, digunakan untuk mempresentasikan data dan bukan untuk mendeskripsikan tipe data. Untuk menjalankannya, diperlukan browser atau HTML parser. Digunakan untuk web page design, dan tidak umum digunakan untuk pertukaran data.    
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena
1. Ringan karena ukuran data yang kecil
2. Mudah dibaca oleh orang
3. Dapat diolah oleh berbagai bahasa
4. Aspek keamanan yang lebih baik
5. Parsing yang lebih efisien
6. Kompatibilitas
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. 
