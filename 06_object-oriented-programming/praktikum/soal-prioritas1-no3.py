class Pelatih:
    def __init__(self, nama, spesialisasi, tahun_pengalaman):
        self.__nama = str(nama)
        self.__spesialisasi = str(spesialisasi)
        self.__tahun_pengalaman = int(tahun_pengalaman)

    def getNama(self):
        return self.__nama

    def setNama(self, nama):
        self.__nama = str(nama)

    def getSpesialisasi(self):
        return self.__spesialisasi

    def setSpesialisasi(self, spesialisasi):
        self.__spesialisasi = str(spesialisasi)

    def getTahunPengalaman(self):
        return self.__tahun_pengalaman

    def setTahunPengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = int(tahun_pengalaman)

    def tampilkanInfo(self):
        print("Nama Pelatih:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)


class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialisasi, tahun_pengalaman)
        self.__jenis_latihan = str(jenis_latihan)
        self.__jadwal = str(jadwal)

    def getJenisLatihan(self):
        return self.__jenis_latihan

    def setJenisLatihan(self, jenis_latihan):
        self.__jenis_latihan = str(jenis_latihan)

    def getJadwal(self):
        return self.__jadwal

    def setJadwal(self, jadwal):
        self.__jadwal = str(jadwal)

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan:", self.__jenis_latihan)
        print("Jadwal:", self.__jadwal)


# Contoh penggunaan kelas KelasLatihan
if __name__ == "__main__":
    # Membuat objek kelas latihan
    kelas_latihan = KelasLatihan("tiara kalbia", "Yoga", 5, "Yoga Pemula", "Senin dan Rabu, 18.00-19.00")

    # Menampilkan informasi kelas latihan
    print("Informasi Kelas Latihan:")
    kelas_latihan.tampilkanInfo()

    # Mengubah jadwal kelas latihan
    kelas_latihan.setJadwal("Selasa dan Kamis, 17.00-18.00")

    # Menampilkan informasi kelas latihan setelah perubahan
    print("\nInformasi Kelas Latihan setelah perubahan:")
    kelas_latihan.tampilkanInfo()
