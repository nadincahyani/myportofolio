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