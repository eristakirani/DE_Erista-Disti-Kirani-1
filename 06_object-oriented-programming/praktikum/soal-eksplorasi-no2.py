class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal
        self.__tersedia = True  # Menandakan kelas tersedia atau tidak

    def tampilkanInfo(self):
        print("Informasi Kelas Latihan:")
        print("Nama Pelatih:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)
        print("Jenis Latihan:", self.__jenis_latihan)
        print("Jadwal:", self.__jadwal)
        print("Tersedia:", "Ya" if self.__tersedia else "Tidak")

    def pesanKelas(self):
        if self.__tersedia:
            print("Kelas", self.__jenis_latihan, "telah berhasil dipesan.")
            self.__tersedia = False
        else:
            print("Maaf, kelas", self.__jenis_latihan, "tidak tersedia saat ini.")

    def batalkanKelas(self):
        if not self.__tersedia:
            print("Kelas", self.__jenis_latihan, "telah berhasil dibatalkan.")
            self.__tersedia = True
        else:
            print("Maaf, kelas", self.__jenis_latihan, "belum tersedia untuk dibatalkan.")


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum


# Demonstrasi Pemesanan dan Pembatalan Kelas dengan Polimorfisme
if __name__ == "__main__":
    # Membuat objek Yoga dan AngkatBeban
    yoga_kelas = Yoga("Vivi", "Yoga", 3, "Yoga Pemula", "Senin dan Kamis, 18.00-19.00", "Sedang")
    angkat_beban_kelas = AngkatBeban("Lala", "Angkat Beban", 5, "Angkat Beban Dasar", "Selasa dan Jumat, 19.00-20.00", "50 kg")

    # Menampilkan informasi kelas sebelum pemesanan
    print("Sebelum Pemesanan:")
    yoga_kelas.tampilkanInfo()
    angkat_beban_kelas.tampilkanInfo()

    # Pemesanan kelas
    print("\nPemesanan Kelas:")
    yoga_kelas.pesanKelas()
    angkat_beban_kelas.pesanKelas()

    # Menampilkan informasi kelas setelah pemesanan
    print("\nSetelah Pemesanan:")
    yoga_kelas.tampilkanInfo()
    angkat_beban_kelas.tampilkanInfo()

    # Pembatalan kelas
    print("\nPembatalan Kelas:")
    yoga_kelas.batalkanKelas()
    angkat_beban_kelas.batalkanKelas()

    # Menampilkan informasi kelas setelah pembatalan
    print("\nSetelah Pembatalan:")
    yoga_kelas.tampilkanInfo()
    angkat_beban_kelas.tampilkanInfo()
