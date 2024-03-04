class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = str(nama)
        self.__usia = int(usia)
        self.__id_pelanggan = str(id_pelanggan)

    def getNama(self):
        return self.__nama

    def setNama(self, nama):
        self.__nama = str(nama)

    def getUsia(self):
        return self.__usia

    def setUsia(self, usia):
        self.__usia = int(usia)

    def getIdPelanggan(self):
        return self.__id_pelanggan

    def setIdPelanggan(self, id_pelanggan):
        self.__id_pelanggan = str(id_pelanggan)

    def tampilkanInfo(self):
        print("Informasi Pelanggan:")
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__id_pelanggan)
        print()


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
        print("Informasi Pelatih:")
        print("Nama Pelatih:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)
        print()


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
        print()


if __name__ == "__main__":
    # Membuat objek Pelanggan
    pelanggan1 = Pelanggan("erista", 35, "A001")

    # Menampilkan informasi pelanggan
    pelanggan1.tampilkanInfo()

    # Membuat objek Pelatih
    pelatih1 = Pelatih("kirani", "Yoga", 7)

    # Menampilkan informasi pelatih
    pelatih1.tampilkanInfo()

    # Membuat beberapa objek KelasLatihan
    kelas_latihan1 = KelasLatihan("Rahel", "Fitness", 5, "Pilates", "Senin dan Rabu, 18.00-19.00")
    kelas_latihan2 = KelasLatihan("Tiara", "Yoga", 3, "Yoga Pemula", "Selasa dan Kamis, 17.00-18.00")
    kelas_latihan3 = KelasLatihan("Lala", "Angkat Beban", 6, "Angkat Beban Dasar", "Rabu dan Jumat, 19.00-20.00")

    # Menampilkan informasi kelas latihan
    kelas_latihan1.tampilkanInfo()
    kelas_latihan2.tampilkanInfo()
    kelas_latihan3.tampilkanInfo()
