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

2. Menyimpan data di dalam model dan memisahkannya dari template HTML adalah praktik yang sangat penting untuk kemudahan pemeliharaan aplikasi. Jika data ditulis langsung (hard-coded) di file template, setiap kali ada perubahan atau penambahan pengalaman baru, harus membuka dan mengedit kode HTML secara manual. Hal ini tidak efisien dan berisiko merusak struktur tampilan halaman jika terjadi kesalahan ketik pada tag HTML. Dengan menggunakan model, struktur tampilan HTML hanya perlu dibuat satu kali menggunakan looping. Data dapat ditambah, diubah, atau dihapus langsung melalui database atau panel admin tanpa perlu menyentuh kode aplikasi sama sekali. Pemisahan ini membuat kode aplikasi menjadi jauh lebih bersih, rapi, dan mudah dikembangkan di masa mendatang, misalnya jika data portofolio tersebut ingin difilter, dicari, atau digunakan kembali untuk fitur lain.

3. Perbedaan utama antara keduanya terletak pada tahap perancangan dan eksekusi. Perintah makemigrations bertugas untuk mendeteksi perubahan yang buat pada file models.py dan mencatatnya ke dalam bentuk berkas cetak biru (migration file) di folder migrations. Perintah ini baru sebatas menyiapkan draf rencana dan belum mengubah struktur database yang sebenarnya. Sementara itu, perintah migrate adalah langkah eksekusi yang akan membaca berkas cetak biru tersebut dan benar-benar menerapkannya ke dalam database nyata.

Sebagai contoh, saat menambahkan atribut baru di model Experience, yaitu documentation_url = models.URLField(blank=True, null=True). Setelah menambahkan baris tersebut di models.py, wajib menjalankan python manage.py makemigrations terlebih dahulu agar Django membuatkan file instruksi migrasinya. Setelah itu, menjalankan python manage.py migrate supaya kolom documentation_url tersebut benar-benar dibuat sebagai kolom baru di tabel database.

### Tugas 3
## Deskripsi Proyek Tugas 3
Pada Tugas 3 ini, saya melakukan refactoring pada berkas HTML dengan memanfaatkan skeleton template `base.html` sebagai berkas utama yang di-extend oleh halaman lainnya seperti `index.html`, `education.html`, `experience.html`, dan `projects.html`. Saya juga menerapkan form serta mekanisme penyajian data untuk bagian Experience dan Project, termasuk fitur tambah, update, hapus (dengan konfirmasi modal/popover), dan pencarian data. Selain itu, saya mengimplementasikan unit test untuk memastikan seluruh fitur data project dan education berjalan dengan baik. 

## Pertanyaan Reflektif
**1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!**
Karena jika membuat form HTML secara manual akan lebih sulit dan berisiko error. Harus membuat tag '<input>' satu per satu, mengatur validasi input di backend secara manual, dan mencocokkan tipe data input dengan kolom database.

Dengan ModelForm Django, akan otomatis membuat elemen form HTML sesuai dengan struktur field/kolom di model database, menangani validasi data otomatis, dan menyimpan data langsung ke database dengan 'form.save()'

'{% csrf_token %}' adalah fitur keamanan wajib di Django untuk mencegah serangan CSRF (Cross-Site Request Forgery). Serangan CSRF dapat terjadi ketika ada situs yang mencoba mengirimkan request (seperti 'POST') ke aplikasi atas nama pengguna yang sedang login tanpa sepengetahuan mereka. Tag '{% csrf_token %}' akan menghasilkan token unik yang divalidasi oleh Django. Jika request yang masuk tidak membawa token cocok ini, Django akan menolak untuk menjaga keamanan data.

**2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**
Meskipun XML dan JSON sama-sama digunakan untuk pertukaran data, JSON menjadi standar utama diaplikasi web modern karena beberapa alasan, seperti:
1. Ukuran data lebih ringan, karena XML menggunakan tag pembuka dan penutup, sedangkan JSON hanya memakai pasangan key-value. Hal ini membuat ukuran berkas JSON jauh lebih kecil sehingga hemat bandwith dan cepat ditransfer melalui jaringan.
2. Mudah di-parse oleh JavaScript, JSON secara alami berstruktur objek JavaScript. Browser bisa langsung membaca data JSON menjadi objek tanpa butuh library parser tambahan yang berat seperti pada XML.
3. Lebih Readable, karena struktur JSON jauh lebih bersih, ringkas, dan tidak perlu banyak tag-tag markup seperti XML.

**3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?**
Alur pengembalian data portofolio pada JSON, yaitu:
1. Request dari client, browser atau aplikasi frontend mengirimkan HTTP Request ke URL endpoint data (misalnya '/api/project/' atau '/api/experience/').
2. URL routing ('urls.py'), Django akan mengarahkan request tersebut ke fungsi view yang sesuai.
3. Query database ('views.py'), fungsi view akan mengambil data dari database menggunakan ORM Django (misalnya 'Experience.object.all()').
4. Serialization, data objek python/Django QuerySet dikonversi menjadi format string JSON menggunakan serializer ('serializers.serialize("json", data)').
5. Response ('HttpResponse'), fungsi view akan mengemas string JSON tersebut ke dalam 'HttpResponse' dengan 'content_type="application/json"' lalu mengirimkannya kembali ke browser/client.

Serialization perlu dilakukan karena Model/QuerySet Django adalah objek python kompleks yang tersimpan di dalam memori server. Objek ini tidak bisa langsung dikirim begitu saja melalui protokol HTTP ke browser, karena HTTP hanya dapat mentransfer teks/byte mentah. Proses serialization bertugas menerjemahkan/mengubah objek python kompleks tersebut menjadi format teks terstruktur standar (seperti JSON) yang dapat dimengerti dan dibaca oleh bahasa pemrograman apapun di sisi frontend (JavaScript, React, Flutter, dll).

## AI Disclosure 
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi percakapan: [Sesi Percakapan Gemini]
(https://share.gemini.google/bj8yR4oGSo57) 
- Strategi Prompting: 
Saya menggunakan pendekatan interaktif berorientasi masalah dengan membagikan potongan kode, skenario kebutuhan alur aplikasi, serta screenshot pesan error Django secara langsung. Strategi ini saya gunakan untuk mendiagnosis kendala teknis (seperti kesalahan format link Google Drive, penanganan error pada Django routing, hingga pembuatan efek visual CSS) secara bertahap tanpa harus merombak struktur utama proyek yang sedang dikembangkan.

- Bagian yang Dibantu AI:
1. Membantu memformulasikan perubahan struktur URL Google Drive dari halaman pratinjau (/file/d/FILE_ID/view) menjadi direct link ([https://lh3.googleusercontent.com/d/FILE_ID](https://lh3.googleusercontent.com/d/FILE_ID)) agar berkas gambar dapat langsung ditampilkan menggunakan tag <img> maupun dibuka utuh saat tombol diklik.
2. Memberikan panduan implementasi efek kaca buram pada tombol menggunakan kombinasi background transparan (RGBA), backdrop-filter: blur(), serta border semi-transparan.
3. Membantu membedah akar penyebab TypeError: delete_project() got an unexpected keyword argument 'project_id' akibat ketidakcocokan variabel antara urls.py dan views.py, serta menyelesaikan NoReverseMatch dengan mengarahkan redirect menggunakan namespacing aplikasi ('main:show_project').
4. Menjelaskan alur kerja pengubahan (update) data menggunakan ModelForm dengan parameter instance=project agar data lama otomatis terisi (pre-filled) pada form tanpa perlu membuat berkas HTML baru.

- Keterbatasan AI & Perbaikan Mandiri:
1. AI sempat menyarankan pengubahan link Google Drive menjadi direct image link ([https://lh3.googleusercontent.com/d/FILE_ID](https://lh3.googleusercontent.com/d/FILE_ID)). Namun, setelah dipertimbangkan, saya memilih untuk tetap menggunakan URL tautan pratinjau Google Drive standar agar berkas dapat diakses langsung oleh pengguna sesuai kebutuhan awal.
2. AI sempat memberikan atribut CSS glassmorphism, namun efeknya tidak terlihat saat diuji. Saya menyadari dan mengoreksinya secara mandiri dengan menambahkan warna/gradasi pada background utama halaman web agar efek pantulan kaca dan buramnya muncul.
3. AI memberikan contoh template dasar menggunakan value="{{ project.title }}", tetapi saya menyesuaikannya secara mandiri dengan struktur rendering form Django ({{ form.as_p }} / looping field) yang sudah saya buat di berkas HTML proyek.
4. Saat AI menyarankan beberapa opsi penamaan parameter pada views.py dan urls.py, saya memeriksa dan menyelaraskan seluruh nama rute URL secara mandiri di berkas urls.py agar tetap konsisten dengan konvensi penamaan proyek saya.

### Tugas 4
## Deskripsi Proyek Tugas 4
Pada Tugas 4 ini, saya mengimplementasikan sistem autentikasi dan otorisasi berbasis Role-Based Access Control (RBAC) menggunakan framework bawaan Django untuk mengamankan data dan fitur pada portofolio. 

## AI Disclosure
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi percakapan: [Sesi Percakapan Gemini]
(https://share.gemini.google/OFeSW03GRxAD) 
- Strategi Prompting: 
Saya menggunakan pendekatan berbasis masalah secara bertahap. Dibandingkan meminta AI membuatkan kode dari nol, saya lebih banyak membagikan potongan kode yang sedang saya kerjakan, menggunggah tangkapan layar pesan error Django yang muncul, dan mengonfirmasi pemahaman konsep tertentu. Strategi ini membantu saya menemukan letak kesalahan teknis tanpa harus merusak struktur kode atau desain kustom yang sudah saya rancang sendiri. 

- Bagian yang Dibantu AI:
1. Membantu menjelaskan bahwa untuk autentikasi tidak perlu membuat kelas model User baru di models.py melainkan menggunakan django.contrib.auth.models.User serta cara menghubungkannya ke model lain menggunakan ForeignKey. 
2. Membantu melacak penyebab error yang disebabkan oleh typo penulisan kode.
3. Memberikan gambaran alur kerja end-to-end untuk fitur AJAX/Fetch pada Django, mulai dari logika JsonResponse, pendaftaran url, hingga pemrosesan data starred_by pada keluaran API JSON.

- Keterbatasan AI & Perbaikan Mandiri:
1. AI sempat memberikan contoh kode HTML standar untuk tombol login dan navbar. Namun, saya memilih untuk tidak langsung copy, melainkan menyelaraskan perbaikan sintaks yang diberikan ke dalam kode HTML yang sudah saya buat. 
2. Ketika terjadi error NoReverseMatch with arguments, AI awalnya hanya berfokus pada perbaikan baris tag {% url %} di HTML. Saya menyadari dan mengecek secara mandiri bahwa masalah utamanya juga bersumber dari nama atribut primary key pada model serta memastikan looping membungkus elemen tersebut dengan benar. 
3. AI tidak dapat memantau network request atau console di Developer Tools browser saya secara langsung. Saya melakukan inspeksi mandiri pada tab Console browser saat tombol star diklik untuk memverifikasi apakah status respon dari server bernilai 200, 404 Not Found, atau 403 Forbidden. 

### Tugas 5
## Deskripsi Proyek Tugas 5
Tugas 5 berfokus pada transformasi antarmuka dan mekanisme pertukaran data pada aplikasi web Django dari Server-Side Rendering (SSR) menjadi Client-Side Rendering berbasis AJAX (Asynchronous JavaScript and XML). Pengembangan ini bertujuan untuk meningkatkan pengalaman pengguna (UX) dengan meminimalisir page reload saat berinteraksi dengan data proyek. Dengan mengimplementasikan Asynchronous Data Rendering (AJAX Fetch), pencarian dinamis dengan Debouncing, manajemen data berbasis modal & AJAX, sistem notifikasi Toast, dan penanganan state UI dan pengamanan XSS. 

## Pertanyaan Reflektif 
**1.Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**
Debouncing adalah teknik pemrograman yang digunakan untuk menunda eksekusi suatu fungsi (seperti pengiriman request AJAX) sampai pengguna berhenti melakukan aksi (seperti mengetik di kolom pencarian) selama interval waktu tertentu (misalnya 300–500 ms). Jika pengguna mengetik huruf baru sebelum jeda waktu tersebut selesai, timer akan di-reset dari awal.

Tanpa debouncing, setiap kali pengguna mengetik satu karakter (misalnya pada event input atau keyup), aplikasi akan langsung mengirimkan HTTP request ke server melalui fetch(). 
- Jika pengguna mengetik kata "Project" (7 huruf), maka akan ada 7 kali request beruntun ke server. 
- Dampak: Beban server membengkak (over-fetching), penggunaan bandwidth boros, dan berisiko terjadi race condition (di mana respon dari pencarian karakter pertama tiba lebih lambat daripada karakter terakhir, sehingga hasil di layar menjadi salah/tidak akurat). Dengan debouncing, request hanya dikirim 1 kali setelah pengguna benar-benar selesai mengetik.

**2.Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
Penggunaan await memberi tahu JavaScript untuk menghentikan sementara eksekusi kode di dalam fungsi async sampai Promise dari fetch() (atau dari .json()) selesai (resolved). await membuat penulisan kode asinkron terasa seperti sinkron, sehingga variabel yang dipanggil setelah baris await dipastikan sudah berisi objek HTTP Response atau data JSON yang siap diolah.

Jika memanggil fetch() tanpa await (dan tanpa .then()), variabel penampung tidak akan berisi data JSON dari server, melainkan berisi objek Promise <pending>. 
- Dampaknya: Saat mencoba membaca atau mengiterasi data (misalnya data.forEach(...)), JavaScript akan melempar error seperti TypeError: data.forEach is not a function atau menampilkan data undefined, karena JavaScript langsung mengeksekusi kode rendering sebelum respon data selesai diunduh dari server.

**3.Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**
XSS adalah celah keamanan di mana peretas (attacker) berhasil memasukkan (inject) skrip berbahaya (biasanya berupa JavaScript) ke dalam data aplikasi web. Saat pengguna lain membuka halaman yang memuat data tersebut, browser akan mengeksekusi skrip jahat tersebut secara otomatis (misalnya mencuri cookie session, token autentikasi, atau melakukan tindakan merugikan atas nama pengguna).

- Di Template Django (Server-Side Rendering): 
Django secara otomatis menerapkan fitur auto-escaping pada semua variabel yang di-render via tag {{ variable }}. Jika ada input berisi <script>alert('xss')</script>, Django secara otomatis merubahnya menjadi entitas aman &lt;script&gt;... sehingga tidak tereksekusi sebagai kode HTML/JS di browser. 

- Di AJAX/JavaScript (Client-Side Rendering): 
Saat mengambil data JSON via fetch() dan merender kartu/grid menggunakan JavaScript (misalnya menyisipkan teks langsung ke elemen HTML dengan properti .innerHTML = data.title), JavaScript tidak memiliki proteksi auto-escaping bawaan. Jika teks data.title mengandung elemen HTML atau atribut onerror jahat, browser akan langsung mengeksekusinya sebagai HTML/JS aktif. Oleh karena itu, di Tugas 5 wajib melakukan escaping manual (atau menggunakan textContent) di JavaScript serta membersihkan input di server dengan strip_tags.

## AI Disclosure
- Tool yang Digunakan: Google Gemini
- Tautan Log / Sesi percakapan: [Sesi Percakapan Gemini]
(https://share.gemini.google/AO7SLrDDWKrw) 
- Strategi Prompting: 
1. Menanyakan klarifikasi struktur HTML secara spesifik untuk memastikan posisi elemen (tombol uji coba toast) berada di tempat yang tepat sesuai petunjuk instruksi tugas. 
2. Meminta penjelasan mengenai cara merubah URL berbagi (share link) Google Drive menjadi format thumbnail direct link beserta pembedahan struktur parameternya (id dan sz). 
3. Mengirimkan kendala operasional (notifikasi toast yang me-return error "terjadi kesalahan") untuk dianalisis indikasi penyebabnya secara sistematis dari sisi input form, token CSRF, hingga validation error.

- Bagian yang Dibantu AI:
1. Penjelasan logika posisi elemen HTML mengenai frasa "di bawah div project-header" yang berarti diletakkan setelah tag penutup </div>, bukan di dalam tag header.
2. Ekstraksi FILE_ID dari URL Google Drive (1SVJnXo0eIgt4gTAk0uu08SGEKDQGplwN) dan penyusunan struktur URL thumbnail ([https://drive.google.com/thumbnail?id=...&sz=w1000](https://drive.google.com/thumbnail?id=...&sz=w1000)) agar gambar bisa dirender langsung di tag <img> HTML.
3. Analisis potensi error pada pengiriman form AJAX, meliputi kualifikasi input URLField yang terpotong, pemeriksaan token CSRF, dan panduan langkah inspection via DevTools Network tab serta log terminal Django.

- Keterbatasan AI & Perbaikan Mandiri:
1. AI memberikan beberapa kemungkinan error, namun verifikasi bahwa URL di dalam field input benar-benar terpotong di bagian akhir (...thumbnail?id=1SVJnXo0eIgt4gTAk0uu08SGEKDQGplw) tetap diidentifikasi dan diperbaiki secara mandiri di tampilan browser.
2. AI tidak bisa melihat respon HTTP secara langsung, sehingga eksekusi Inspect Element (F12) pada tab Network dan pengecekan terminal python manage.py runserver untuk melihat traceback 400/500 dilakukan secara langsung pada lingkungan lokal.