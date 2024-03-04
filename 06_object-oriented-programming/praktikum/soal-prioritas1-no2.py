class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = str(nama)
        self.__spesialisasi = str(spesialisasi)
        self.__tahun_pengalaman = int(tahun_pengalaman)

    # Getter untuk nama
    def getNama(self):
        return self.__nama

    # Setter untuk nama
    def setNama(self, nama):
        self.__nama = str(nama)

    # Getter untuk spesialisasi
    def getSpesialisasi(self):
        return self.__spesialisasi

    # Setter untuk spesialisasi
    def setSpesialisasi(self, spesialisasi):
        self.__spesialisasi = str(spesialisasi)

    # Getter untuk tahun pengalaman
    def getTahunPengalaman(self):
        return self.__tahun_pengalaman

    # Setter untuk tahun pengalaman
    def setTahunPengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = int(tahun_pengalaman)

    # Metode untuk menampilkan informasi pelatih
    def tampilkanInfo(self):
        print("Nama Pelatih:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)


# Contoh penggunaan kelas Pelatih
if __name__ == "__main__":
    # Membuat objek pelatih
    pelatih1 = Pelatih("Vira", "Yoga", 5)

    # Menampilkan informasi pelatih
    print("Informasi Pelatih:")
    pelatih1.tampilkanInfo()

    # Mengubah tahun pengalaman pelatih
    pelatih1.setTahunPengalaman(7)

    # Menampilkan informasi pelatih setelah perubahan
    print("\nInformasi Pelatih setelah perubahan:")
    pelatih1.tampilkanInfo()
