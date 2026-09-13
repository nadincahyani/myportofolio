Nama : Nadin Putri Cahyani
NPM : 2506623332
Kelas : PBP E

Pertanyaan Reflektif 
### Tugas 1
1. Ya, saya menggunakan elemen semantik HTML5 seperti <header>, <nav>, <section>, dan <footer> dalam merancang struktur website portofolio ini. 
Elemen-elemen semantik tersebut sangat membantu dalam pembuatan static web melalui beberapa aspek: 
- Struktur kode yang readable dan maintainability. Penggunaan <section> membagi halaman menjadi blok-blok informasi yang jelas (seperti hero, education, dan experience). Hal ini mempermudah pembacaan kode baik saat debugging maupun untuk pengembangan lain. 
- Elemen semantik memberikan konteks struktural bagi screen reader yang digunakan oleh penyandang disabilitas untuk menavigasi halaman dengan lebih mudah.
- Optimasi SEO, search engine dapat memahami hierarki dan tingkat kepentingan konten secara lebih efektif.
- Memudahkan penerapan styling CSS secara langsung tanpa harus memberikan class secara berlebihan pada setiap pembungkus elemen. 

2. Tantangan terbesar yang saya temui saat mengatur responsivitas CSS adalah saat peralihan dari CSS Grid ke Single-Column Layout. Pada tampilan dekstop, bagian hero menggunakan grid-template-columns untuk menyandingkan teks intro di kiri dan ID Card di kanan. Pada layar mobile yang sempit, layout dua kolom ini menjadi sangat padat dan tidak proporsional. Selain itu, kesulitan pada  penyesuaian timeline experience. Komponen timeline dengan garis dan titik koordinat perlu disesuaikan dengan padding dan posisinya agar tidak memakan terlalu banyak ruang horizontal pada layar ponsel. 

Dalam mengevaluasi elemen mana yang harus diubah atau diprioritaskan saat breakpoint mobile, adalah:
- Prioritas hierarki informasi. Pada tampilan mobile, perhatian pengunjung adalah informasi diri dan kontak. Oleh karena itu, saya menumpuk layout secara vertikal di mana teks pengenalan diri dan kontak diposisikan paling atas, diikuti oleh visual id card. 
- Akomodasi ruang sentuh. Elemen interaktif seperti informasi kontak dan experience card disesuaikan ukurannya agar memiliki padding yang cukup untuk di-tap menggunakan jari pada layar sentuh. 
- Penggunaan unit fleksibel. Saya memanfaatkan clamp() untuk ukuran heading dan unit relatif (rem, %, vh) agar ukuran teks dan jarak antar elemen beradaptasi secara halur sebelum mencapai breakpoint media query tertentu. 

3. Sebagai static web murni, terdapat beberapa batasan utama yang dirasakan saat menyajikan informasi portofolio, seperti: 
- Pengelolaan konten manual. Setiap kali ada pembaruan pengalaman, proyek, atau perubahan data diri, saya harus mengubah file HTML/CSS secara manual. 
- Form kontak atau pengiriman pesan tidak dapat memproses data secara real-time tanpa bantuan backend atau layanan pihak ketiga. 
- TGidak ada manajemen status. Fitur seperti pergantian tema (light/dark mode) atau penyaringan (filter) pengalaman berdasarkan kategori belum bisa tersimpan secara permanen sesuai preferensi pengguna. 

Fungsionalitas dinamis yang ingin ditambahkan selanjutnya adalah mengambil data pengalaman/proyek dari file eksternal secara dinamis, menambahkan fitur filtering untuk kategori tertentu, dan menambahkan dark atau light mode. 

### Tugas 2
1. Ketika pengguna membuka halaman portofolio baru di browser, prosesnya dimulai dari memasukkan alamat URL. Pertama-tama, Django menerima request tersebut melalui file urls.py milik proyek utama. File ini berfungsi sebagai pintu gerbang utama yang mengarahkan permintaan ke file urls.py di tingkat aplikasi (main/urls.py). Di dalam urls.py aplikasi, URL tersebut dicocokkan dengan rute yang sesuai untuk menentukan fungsi view mana yang harus menangani permintaan tersebut, misalnya fungsi show_experience.

Setelah rute ditemukan, view mengambil alih peran sebagai pengolah logika. Jika halaman membutuhkan data portofolio, view akan berkomunikasi dengan models.py. Model inilah yang bertindak sebagai jembatan ke database untuk mengambil data objek yang diperlukan. Setelah data berhasil diambil dari database, view membungkus data tersebut ke dalam sebuah variabel yang dinamakan context.

Langkah terakhir terjadi saat view menyerahkan data context tersebut ke file template HTML (seperti experience.html). Di dalam template, data diolah menggunakan Django Template Language (DTL) agar bisa ditampilkan secara dinamis melalui perulangan. Django kemudian memproses seluruh kode tersebut menjadi file HTML murni dan mengirimkannya kembali ke browser pengguna untuk ditampilkan secara visual.

2. Menyimpan data di dalam model dan memisahkannya dari template HTML adalah praktik yang sangat penting untuk kemudahan pemeliharaan aplikasi. Jika data ditulis langsung (hard-coded) di file template, setiap kali ada perubahan atau penambahan pengalaman baru, kita harus membuka dan mengedit kode HTML secara manual. Hal ini tidak efisien dan berisiko merusak struktur tampilan halaman jika terjadi kesalahan ketik pada tag HTML. Dengan menggunakan model, struktur tampilan HTML hanya perlu dibuat satu kali menggunakan looping. Data dapat ditambah, diubah, atau dihapus langsung melalui database atau panel admin tanpa perlu menyentuh kode aplikasi sama sekali. Pemisahan ini membuat kode aplikasi menjadi jauh lebih bersih, rapi, dan mudah dikembangkan di masa mendatang, misalnya jika data portofolio tersebut ingin difilter, dicari, atau digunakan kembali untuk fitur lain.

3. Perbedaan utama antara keduanya terletak pada tahap perancangan dan eksekusi. Perintah makemigrations bertugas untuk mendeteksi perubahan yang kita buat pada file models.py dan mencatatnya ke dalam bentuk berkas cetak biru (migration file) di folder migrations. Perintah ini baru sebatas menyiapkan draf rencana dan belum mengubah struktur database yang sebenarnya. Sementara itu, perintah migrate adalah langkah eksekusi yang akan membaca berkas cetak biru tersebut dan benar-benar menerapkannya ke dalam database nyata.

ebagai contoh, saat menambahkan atribut baru di model Experience, yaitu documentation_url = models.URLField(blank=True, null=True). Setelah menambahkan baris tersebut di models.py, kita wajib menjalankan python manage.py makemigrations terlebih dahulu agar Django membuatkan file instruksi migrasinya. Setelah itu, kita menjalankan python manage.py migrate supaya kolom documentation_url tersebut benar-benar dibuat sebagai kolom baru di tabel database kita.