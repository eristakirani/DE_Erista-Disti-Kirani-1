### Soal **Eksplorasi (20)**

1. Eksplorasi API RentABook:
    - Pelajari dokumentasi API RentABook: **https://app.swaggerhub.com/apis-docs/sepulsa/RentABook-API/1.0.0**.
    - Identifikasi endpoint yang tersedia beserta fungsinya.
    
Berdasarkan dokumentasi API RentABook, berikut adalah daftar endpoint yang tersedia dan fungsinya:

**Authentication**:
   - **GET /auth/token**: Meminta atau mendapatkan token akses.

**Client**: 
   - **GET /client/{id}**: Mengambil data klien berdasarkan ID.
   - **PUT /client/{id}**: Memperbarui data klien berdasarkan ID.
   - **DELETE /client/{id}**: Menghapus klien berdasarkan ID.
   - **GET /client**: Mendapatkan daftar semua klien.
   - **POST /client**: Menambahkan klien baru.

**User**:
   - **GET /users**: Mengambil daftar semua pengguna.
   - **GET /users/{id}**: Mengambil informasi detail pengguna berdasarkan ID.
   - **PUT /users/{id}**: Memperbarui informasi pengguna berdasarkan ID.
   - **DELETE /users/{id}**: Menghapus pengguna berdasarkan ID.

**Book**:
   - **GET /books**: Mengambil daftar semua buku yang tersedia untuk disewa.
   - **GET /books/{id}**: Mengambil detail buku berdasarkan ID.
   - **GET /books/search**: Mencari buku berdasarkan judul atau penulis.
   - **POST /books**: Menambahkan buku baru.
   - **PUT /books/{id}**: Memperbarui detail buku berdasarkan ID.
   - **DELETE /books/{id}**: Menghapus buku berdasarkan ID.

**Rent**:
   - **GET /rent/{id}**: Mengambil transaksi penyewaan buku berdasarkan ID.
   - **GET /rent**: Mengambil semua transaksi penyewaan buku.
   - **POST /rent**: Menyewa sebuah buku.

2. Implementasi 4 Metode pada RentABook API:
    - Lakukan request dengan metode GET, POST, PUT, dan DELETE pada endpoint yang tersedia di RentABook API.
    - Contoh: Lakukan operasi CRUD pada resource client.

    - **DOKUMENTASI**:
    [Screenshots](../Screenshots)
    
3. Dokumentasi Eksplorasi:
    - Simpan semua request dan response terkait RentABook API dalam Postman Collection baru.