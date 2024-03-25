Soal-Prioritas 1 

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.

1. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.

1. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.


Jawab: 

1. Perbedaan Data Terstruktur dan Data Tidak Terstruktur: 

**Data terstruktur** adalah data yang terorganisir dalam format yang rapi dan terdefinisi dengan baik, seperti tabel, database, atau spreadsheet. Data ini mudah dianalisis dan dicari karena memiliki skema yang jelas, yang menentukan format dan hubungan antar data.

**Contoh data terstruktur:**

- Data kontak pelanggan dalam database CRM
- Daftar produk dalam toko online
- Data keuangan dalam spreadsheet
- Transaksi kartu kredit dalam tabel database

**Data tidak terstruktu**r adalah data yang tidak memiliki format yang rapi dan terdefinisi dengan baik. Data ini bisa berupa teks, gambar, audio, video, email, dan lain sebagainya. Data ini lebih sulit dianalisis dan dicari karena tidak memiliki skema yang jelas.

**Contoh data tidak terstruktur:**

- Email
- Postingan media sosial
- Foto dan video
- Dokumen teks
- Pesan instan

Data terstruktur dan data tidak terstruktur adalah dua jenis data yang berbeda dengan karakteristik dan penggunaannya masing-masing. Data terstruktur lebih mudah dianalisis dan dicari, sedangkan data tidak terstruktur lebih sulit dianalisis dan dicari tetapi dapat memberikan wawasan yang lebih mendalam.





1. **Basis data relasional** adalah sistem penyimpanan data yang mengorganisir data dalam tabel-tabel yang saling terkait. Setiap tabel terdiri dari baris (record) dan kolom (field). Setiap baris mewakili satu entitas (misalnya, pelanggan, produk, atau pesanan), dan setiap kolom mewakili satu atribut dari entitas tersebut (misalnya, nama, alamat, atau harga).

`             `**Cara Kerja:** 

- Data disimpan dalam tabel: Data terstruktur dalam tabel dengan baris dan kolom. Setiap tabel memiliki skema yang mendefinisikan nama dan tipe data dari setiap kolom.
- Hubungan antar tabel: Tabel-tabel dihubungkan satu sama lain melalui kunci. Kunci utama (primary key) di satu tabel dihubungkan dengan kunci asing (foreign key) di tabel lain.
- Akses data: Data dapat diakses dan dimanipulasi menggunakan Structured Query Language (SQL). SQL adalah bahasa pemrograman yang dirancang khusus untuk mengelola data dalam basis data relasional.

**Contoh Penggunaan:**

- Sistem Point of Sale (POS): Menyimpan data tentang penjualan, produk, dan pelanggan.
- Sistem Manajemen Pelanggan (CRM): Menyimpan data tentang pelanggan, kontak, dan peluang penjualan.

1. Normalisasi basis data adalah proses mendekomposisi data dalam basis data relasional untuk mengurangi redundansi dan anomali data. Proses ini dilakukan dengan membagi data menjadi tabel-tabel yang lebih kecil dan terhubung dengan kunci.

   Konsep Normalisasi:

- Bentuk Normal Pertama (1NF): Setiap kolom dalam tabel hanya boleh berisi satu nilai atom.

- Bentuk Normal Kedua (2NF): Setiap kolom yang bukan kunci utama harus bergantung sepenuhnya pada kunci utama.

- Bentuk Normal Ketiga (3NF): Setiap kolom yang bukan kunci utama tidak boleh bergantung pada kolom lain yang bukan kunci utama.

Pentingnya Normalisasi:

Normalisasi sangat penting dalam konteks basis data relasional karena:

- Meningkatkan kualitas data: Data yang ternormalisasi lebih akurat dan konsisten, sehingga dapat menghasilkan analisis yang lebih baik.

- Meningkatkan kinerja: Basis data yang ternormalisasi lebih efisien dan performant.

- Mempermudah pengembangan aplikasi: Struktur data yang ternormalisasi memudahkan pengembang untuk membuat aplikasi yang menggunakan data tersebut
- Meningkatkan skalabilitas: Basis data yang ternormalisasi dapat diubah ukurannya dengan lebih mudah.

Referensi: 

- Elmasri, R., & Navathe, S. B. (2010). Fundamentals of database systems (6th ed.). Boston, MA: Addison-Wesley.
- Korth, H. F., & Silberschatz, A. (2016). Database system concepts (7th ed.). New York, NY: McGraw-Hill Education.
- https://en.wikipedia.org/wiki/Database\_normalization
