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
        print()


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan

    def getTingkatKesulitan(self):
        return self.__tingkat_kesulitan

    def setTingkatKesulitan(self, tingkat_kesulitan):
        self.__tingkat_kesulitan = tingkat_kesulitan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkat_kesulitan)
        print()


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum):
        super().__init__(nama, spesialisasi, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum

    def getBeratMaksimum(self):
        return self.__berat_maksimum

    def setBeratMaksimum(self, berat_maksimum):
        self.__berat_maksimum = berat_maksimum

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat Maksimum yang Dapat Diangkat:", self.__berat_maksimum)
        print()
        

if __name__ == "__main__":

    yoga_kelas = Yoga("Vivi", "Yoga", 3, "Yoga Pemula", "Senin dan Kamis, 18.00-19.00", "Sedang")

    yoga_kelas.tampilkanInfo()
 
    yoga_kelas.setTingkatKesulitan("Tinggi")

    print("Informasi setelah perubahan:\n")
    yoga_kelas.tampilkanInfo()

    angkat_beban_kelas = AngkatBeban("Lala", "Angkat Beban", 5, "Angkat Beban Dasar", "Selasa dan Jumat, 19.00-20.00", "50 kg")

    angkat_beban_kelas.tampilkanInfo()

    angkat_beban_kelas.setBeratMaksimum("60 kg")
    
    print("Informasi setelah perubahan:\n")
    angkat_beban_kelas.tampilkanInfo()
