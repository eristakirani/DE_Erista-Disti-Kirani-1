class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahun_pengalaman = tahun_pengalaman
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        print("Informasi Kelas Latihan:")
        print("Nama Pelatih:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahun_pengalaman)
        print("Jenis Latihan:", self.__jenis_latihan)
        print("Jadwal:", self.__jadwal)


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan

    def aturPosisiYoga(self, posisi):
        print("Posisi Yoga diatur ke:", posisi)

    def tampilkanInfo(self):
        print("Informasi Kelas Yoga:")
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkat_kesulitan)


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum

    def aturBeratBeban(self, berat):
        print("Berat Beban diatur ke:", berat)

    def tampilkanInfo(self):
        print("Informasi Kelas AngkatBeban:")
        super().tampilkanInfo()
        print("Berat Maksimum yang Dapat Diangkat:", self.__berat_maksimum)


# Demonstrasi Penggunaan Metode Khusus
if __name__ == "__main__":
    # Membuat objek Yoga dan AngkatBeban
    yoga_kelas = Yoga("Vivi", "Yoga", 3, "Yoga Pemula", "Senin dan Kamis, 18.00-19.00", "Sedang")
    angkat_beban_kelas = AngkatBeban("Lala", "Angkat Beban", 5, "Angkat Beban Dasar", "Selasa dan Jumat, 19.00-20.00", "50 kg")

    # Mengatur posisi yoga
    yoga_kelas.aturPosisiYoga("Vinyasa")

    # Mengatur berat beban
    angkat_beban_kelas.aturBeratBeban("60 kg")

    
