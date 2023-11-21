# Jeshuamart - _Sahabat Belanja Keluarga Anda!_
[Tautan menuju website](https://bryan-jeshua-tugas) <br/>
Nama    : Bryan Jeshua Mario Timung <br/>
NPM     : 2206027021 <br/>
Kelas   : PBP C <br/>
## Requirements  
1. Python3
## Libraries Used
1. Django
2. Datetime 
<details>
<summary> <b> WEEK 02</b> </summary>

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
![Diagram](https://github.com/bryanjeshua/jeshuamart/blob/master/image/DIAGRAM%20MVT.png)
Dari gambar di atas dapat ditarik sebuah kesimpulan yakni dalam aplikasi Django, ketika ada http request, maka urls.py akan meneruskannya menuju kepada views.py yang sesuai. Kemudian views.py akan melakukan ragam perintah yang dilakukan, misalnya melakukan read/write data dengan berinteraksi dengan models.py, kemudian main.html akan melakukan pengaturan tampilan yang sesuai terhadap data/komponen yang akan ditampilkan. Setelah itu, maka akan dikirimkan http response berupa file html kepada pengguna oleh views.py.

## Why do we need virtual environment?
Kita membutuhkan _virtual environment_ untuk melokalisir pengaturan sejumlah depedency yang berhubungan dengan  proyek kita sehingga bila kedepannya terdapat sejumlah proyek yang membutuhkan sejumlah library/framework yang sama, tidak terjadi _conflict_ terhadap versi maupun pengaturan suatu library yang mampu membuat program tidak berjalan sebagaimana mestinya.

## Perbedaan antara MVC, MVT, MVVM
MVT merupakan pola pengembangan arsitektur yang digunakan di _web development_ yang berkaitan erat dengan framework web pada python seperti Django. Terdapat tiga komponen yakni Model (yang merepresentasikan data dan logika utama aplikasi, termasuk membaca dan menyimpan data), View (yang mengatur bagaimana data yang dimiliki akan ditayangkan), Template (yang berfungsi mengatur layout halaman web untuk ditayangkan).
MVC merupakan pola pengembangan arsitektur yang digunakan dalam _software development_  terutama dalam membangun GUI dan website, dan terdiri atas tiga komponen yakni Model, View (berisi pengaturan layer presentasi data yang didapat dari model, termasuk pengaturan button, forms, dan beragam komponen lainnya), dan Controller (menghubungkan model dan view, misalnya mengelola input dari user pada view untuk diteruskan ke model)
MVVM merupakan pola pengembangan arsitektur yang berkaitan erat dengan pengembangan GUI terutama pada ragam aplikasi yang membutuhkan data binding. MVVM terdiri atas tiga komponen yakni Model, View (bertugas untuk menampilkan data terhadap user dan menangkap interaksi dari user), dan ViewModel (bertugas menghubungkan model dan view, menunjukan data dan perintah yang dapat view gunakan untuk melakukan data binding, dan menyederhanakan tampilan data dari model agar view lebih mudah untuk menampilkannya tanpa berisi logika tampilan antarmukanya)

Perbedaan ketiganya terdapat pada cara mereka mengatur hubungan antara model, view, dan komponen perantaranya (baik template, controller, maupun viewmodel). MVT menggunakan template sebagai perantara model dan view dan bertugas menggambarkan struktur dari halaman web. MVC menggunakan controller untuk menghubungkan model dan view, mengatur input dari user, dan mengelola alur data. Sedangkan, MVVM menggunakan ViewModel sebagai perantara yang mengelola tampilan data yang akan ditampilkan ke view dan mengelola interaksi user.
</details>

<details>
<summary><b>WEEK 03</b></summary>

## Apa perbedaan antara form POST dan form GET dalam Django?
Perbedaan antara form POST dan form GET dalam Django adalah sebagai berikut
<br/>POST :
- Ketika menggunakan metode POST, data form dikirimkan sebagai bagian dari HTTP Request Body, bukan sebagai parameter query dalam URLnya. Metode ini lebih aman jika dibandingkan dengan GET karena data tersebut tidak terlihat di URL sehingga jauh lebih aman untuk mengirimkan informasi sensitif seperti password.
- Metode POST dapat mengolah data dalam jumlah besar jika dibandingkan dengan GET sehingga jauh lebih disarankan jika ingin melibatkan data submission.
<br/>GET :
- Ketika menggunakan metode GET, data dari form akan dikirimkan sebagai parameter query pada URL. Biasanya, metode ini digunakan ketika kita hendak mengakses data dari server atau ketika kita hendak melakukan operasi membaca. Metode ini juga cocok untuk melakukan pencarian forms sederhana. 
- Data ini dapat dilihat pada URL. Ini menyebabkan informasi menjadi kurang aman dan membatasi jumlah data yang dapat dikirimkan.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan utama antara XML, JSON, dan HTML adalah sebagai berikut
- XML = menggunakan tag (serupa dengan HTML) akan tetapi dapat didefinisikan user. Tidak memiliki tipe data dan memperlakukan semuanya sebagai text. Jauh lebih mudah dibaca orang. Cocok untuk dokumen yang rumit, termasuk pertukaran data yang tidak mendukung JSON.
- JSON = Menggunakan pasangan key dan value, mendukung tipe data string, number, booleans, array, dan object. Kurang deskriptif jika dibandingkan dengan XML. Ukurannya lebih kecil. Umum digunakan pada web applications, APIs, dan file konfigurasi.0 
- HTML = Menggunakan tags yang sudah didefinisikan sebelumnya, digunakan untuk mempresentasikan data dan bukan untuk mendeskripsikan tipe data. Untuk menjalankannya, diperlukan browser atau HTML parser. Digunakan untuk web page design, dan tidak umum digunakan untuk pertukaran data.    

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena
1. Ringan karena ukuran data yang kecil
2. Mudah dibaca oleh orang sehingga memudahkan saat membangun program
3. Dapat diolah oleh berbagai bahasa pemrograman
4. Aspek keamanan yang lebih baik
5. Parsing yang lebih efisien, bisa langsung dilakukan dengan method JSON.parse()
6. Kompatibilitas dengan sejumlah framework teknologi (misalnya dengan RESTful APIs.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Saya menjalankan virtual environment terlebih dahulu
2. Kemudian, saya memperbaiki routing urls.py dengan mengubah path main menjadi ''
3. Selanjutnya, saya membangun forms.py di dalam direktory main untuk menerima data produk yang baru yang akan disimpan ke inventory. Fields yang akan dipakai antara lain ["name", "amount", "price","description", "categories"]
4. Karena terjadi kebutuhan akan adanya form, maka saya mengimport ProductForm pada views.py. Kemudian, saya juga perlu membangun method create_product untuk membuat formulir yang bisa menambahkan data produk secara otomatis saat submisi dilakukan. Lalu, saya menambahkan fungsi show_main dengan menambahkan konteks antara lain'name', 'amount', 'description', 'date_in', 'stock', 'categories', dan 'products'. Selain itu, saya juga membangun method show_xml, show_json, show_json_by_id, show_xml_by_id.
5. Lalu saya mengimport fungsi create_product pada urls.py di main, dan menambahkan path url ke dalam variable urlpatterns. Begitu juga untuk method yang lainnya
6. Setelah itu, saya membangun folder templates di root. Saya kemudian membuat base.html untuk template dasar sebagai kerangka umum berbagai halaman lainnya dalam web.
7. Saya kemudian mengatur agar base.html bisa terdeteksi melalui settings.py
8. Kemudian, saya mengubah tampilan main.html sesuai yang diinginkan. Saya menambahkan button "Add New Product" dan mengatur tampilan lainnya
9. Tak berhenti di sana, saya kemudian membuat pada main/templates suatu file create_product.html yang menampilkan form untuk mengisi.
10. Lalu saya mencoba mengoperasikan postman sebagai data viewer

## SCREENSHOT GAMBAR
1. HTML ![](https://github.com/bryanjeshua/jeshuamart/blob/master/image/HTML.png)
2. JSON ![](https://github.com/bryanjeshua/jeshuamart/blob/master/image/JSON.png)
3. JSON BY ID ![](https://github.com/bryanjeshua/jeshuamart/blob/master/image/JSONbyID.png)
4. XML ![](https://github.com/bryanjeshua/jeshuamart/blob/master/image/XML.png)
5. XML BY ID ![](https://github.com/bryanjeshua/jeshuamart/blob/master/image/XMLbyID.png)
</details>

<details>
<summary><b> WEEK 04</b> </summary>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah suatu built-in class-based form yang sudah disertakan dalam package 'django.contrib.auth.forms' yang digunakan untuk memudahkan pendaftaran pengguna aplikasi yang kita bangun. Secara default, terdapat bagian username, password, dan password confirmation. Kelebihannya yakni builtin ini sangat mudah untuk diimplementasikan, sudah termasuk dengan fitur validasi data, sudah dilengkapi juga dengan fitur keamanan yakni hashing password, dokumentasi yang lengkap, adanya komunitas yang membantu pengembangan produk kita, serta dapat dikustomisasi sesuai kebutuhan. Akakn tetepi, terdapat juga kekurangan yakni default yang terbatas sehingga perlu membangun subclass baru jika ingin meminta input email, first_name, dan sebagainya, validasi yang disediakan hanyalah validasi dasar yang perlu dikembangkan jika ingin lebih kompleks, serta tidak dilengkapi dengan fungsi lain misalnya captcha atau konfirmasi email.
## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi merupakan proses verifikasi identitas pengguna (yang biasanya menggunakan username dan password, sedangkan otorisasi adalah proses penentuan komponen yang dapat diakses oleh pengguna setelah melakukan autentikasi. Keduanya penting karena autentikasi diperlukan untuk memastikan bahwa pengguna merupakan entitas yang sesuai dengan yang diakuinya, dan otorisasi diperlukan untuk membatasi akses untuk melakukan aksi-aksi tertentu.
## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan data kecil yang disimpan di browser pengguna oleh website. Djanggo menggunakan cookies untuk mengelola data sesi pengguna. Data sesi ini digunakan untuk mengidentifikasi pengguna dan informasi terkait selama web digunakan oleh pengguna.
## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara default, cookies tetap perlu diwaspadai penggunaannya, terutama untuk menyimpan informasi yang sensitif. Ada sejumlah risiko yang harus diwaspadai antara lain risiko cookies hijacking (pencurian cookies sehingga orang tidak perlu lagi melakukan log in karena sesi pada cookienya masih aktif), risiko modifikasi data jika cookies tidak dienkripsi. Mitigasi yang dapat dilakukan adalah dengan menggunakan HTTPS dan melakukan pengaturan flag "Secure", "HttpOnly", serta tidak sembarangan menggunakan WiFi publik.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Saya mengaktivasi virtual environment
2. Saya menghubungkan product dengan user. Ini dilakukan dengan cara memanggil User dari library django.contrib.auth.models pada file models.py. Pada models, saya membangun relationship dengan menggunakan ForeignKey pada django. Saya juga menambahkan context untuk menampilkan user yang sedang login.
3. Saya membangun form registrasi dengan nama file register.html dan membuat fungsinya di views.py. Saya juga mengimport URL pathnya ke urls.py pada variable urlpattern. 
4. Saya membangun form login dengan nama file login.html dan membuat fungsi login dan logout di views.py. Saya juga mengimport URL pathnya ke urls.py pada variable url pattern. Saya juga sembari mengimplementasikan cookies di tahap ini dengan memanggil method set_cookie pada fungsi login dan delete_cookie pada fungsi logout pada instance response dan menambahkan 'last_login' pada context.
5. Saya merestriksi akses halaman main dengan builtin login_required
6. Saya merapikan semua html sesuai keinginan saya, lalu push ke github.
</details>

<details>
<summary><b> WEEK 05</b></summary>

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector dapat digunakan untuk memilih semua element berdasarkan nama tagnya. Ini dapat digunakan jika kita hendak melakukan styling terhadap semua elemen dengan jenis tag tertentu.
Struktur element selector yakni
```
p {
    background-color : yellow;
}
```
## HTML5 Tags Explanation


| HTML TAG | Description                        |
|----------|---------------------------------   |
| `<td>`   | Membuat sebuah sel dalam sebuah    |
|`<tr>`    | Membuat baris dalam sebuah tabel   |
|`<th>`    | Membuat sebuah sel header tabel    |
|`<style>` | Membuat informasi gaya dalam dokumen |
|`<thead>`| Membuat isi header dalam satu tabel menjadi satu kelompok|
|`<tbody>`| Membuat isi body dalam satu tabel menjadi satu kelompok|
|`<a>`| Membuat hyperlink |
|`<link>`|  Membangun hubungan antara dokumen dan sumber daya eksternal|
|`<img>`| Membuat gambar |
|`<option>`|Membuat drop down|
|`<form>` | Membuat sebuah form HTML untuk input dari pengguna|

## Jelaskan perbedaan antara margin dan padding.
Padding merupakan ruang kosong pada bagian dalam sebuah element yang dibatasi border, sedangkan margin merupakan ruang di luar border yang membatasi sebuah elemen dengan elemen yang lain. 

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Bootstrap menyediakan jauh lebih banyak komponen yang telah didefinisikan sebelumnya, sedangkan tailwind mengharuskan perogrammer membangun sejumlah komponen jika hendak membuat komponen yang kompleks. Jika kita hendak membangun program sederhana, ataupun baru saja mencoba belajar, bootstrap adalah framework yang cocok karena jauh lebih sederhana dan mudah pakai. Akan tetapi, kita tak akan terlalu bisa membuat banyak komponen yang kompleks. Jika hendak membangun komponen yang kompleks, Tailwind cocok karena menawarkan flexibilitas yang lebih tinggi

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Saya mengimport semua file yang dibutuhkan seperti text dan gambar ke dalam folder static
- Setelah itu, saya melakukan load static pada setiap html file 
- Lalu, saya melakukan styling sesuai keinginan saya. Saya mencari inspirasi yang sesuai di internet dan mengimplementasikannya. Urutannya adalah saya mengerjakan login page, register page, main page, add new product page, dan edit product page. Saya memastikan saat login ada navbar berisi logo perusahaan saya. Saya merapikan semua tabel dan form yang akan muncul. Saya juga memastikan peletakan button sesuai estetika.

</details>
<details>
<summary><b>WEEK 06</b></summary>

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming mengeksekusi program yang diperintahkan satu per satu secara berurutan. Sedangkan, asynchronous programming memungkinkan tugas-tugas yang perlu dieksekusi untuk berjalan tanpa harus menunggu yang sebelumnya selesai. Ini akan memungkinkan program berjalan lebih responsif.
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan paradigma pemrograman ketika program merespons kejadian yang terjadi seperti klik mouse, hover mouse, input pengguna, hingga permintaan AJAX. Pada tugas ini, contoh event-driven programming adalah ketika menekan tombol add product, akan muncul jendela modal yang meminta data-data benda yang hendak dibuat.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan nya ada pada permintaan HTTP (seperti GET dan POST) untuk dilakukan secara asynchronous sehingga tidak menghentikan program utama. Hasil dari permintaan tersebut akan diproses saat data diterima dari server tanpa harus menunggu terlebih dahulu. Ini akan memungkinkan web kita lebih responsif dan pengalaman penggunanya lebih baik.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API adalah standar baru untuk membuat HTTP Request di Javascript. Dia menggunakan Promis untuk mengelola respons dari HTTP Request. Kelebihannya adalah lebih modern, ringan, dan terintegrasi dengan Javascript yang baru. Namun, pemakaian fetch API bisa membutuhkan lebih banyak kode jika penggunaan yang hendak dilakukan lebih kompleks.
jQuery adalah library JavaScript untuk mengimplementasikan AJAX yang dirancang supaya bisa cross browser. Kode dari jQuery versi lama masih bisa berfungsi di jQuery yang baru yang menunjukkan tingginya kompatibilitas. jQuery juga mendukung high level abstraction untuk mengimplementasikan AJAX, animasi, dan DOM manipulation sehingga proses pengembangan lebih cepat. Banyak juga plugin yang dimiliki oleh jQuery sehingga akan mempercepat development. Menurut saya, karena proyek ini merupakan proyek kecil, dan akan lebih baik menggunakan standar yang lebih baru, preferensi saya jatuh ke Fetch API. Banyak fitur javascript modern yang dapat diimplementasikan oleh FetchAPI. Tapi, ada kemungkinan jika proyeknya lebih besar dan perlu mengintegrasikan ke beragam browser, jQuery akan lebih baik untuk digunakan. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Saya mengubah tampilan awalnya terlebih dahulu dari bentuk tabel menjadi bentuk cards. Ini dilakukan dengan cara fetch semua datanya terlebih dahulu dalam fungsi getProducts. Lalu, saya bangun kode untuk cardsnya dalam fungsi refreshProducts.
- Lalu, Saya membangun fungsi create_ajax di views.py. Kemudian saya menghubungkan pathnya pada urls.py. 
- Setelah itu, saya membangun kode untuk menampilkan modalnya beserta buttonnya yang akan menjadi event source nya.
- Kemudian, di main.html saya membuat kode addProducts yang akan terpanggil ketika tombol add product di jendela modal dipanggil.
- Setelah itu, saya juga membangun fungsi delete_product_ajax untuk menghapus product yang terpilih. Saya juga menghubungkan pathnya pada urls.py.
- Setelahnya, saya membangun kode untuk menampilkan button delete untuk menghapus productnya dan kode javascriptnya yang akan terpanggil jika ditekan. 
</details>