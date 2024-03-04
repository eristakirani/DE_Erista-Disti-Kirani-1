class KelasLatihan:
    def pesanKelas(self):
        pass

    def batalkanKelas(self):
        pass


class Yoga(KelasLatihan):
    def pesanKelas(self):
        print("Pesanan kelas Yoga berhasil dibuat.")

    def batalkanKelas(self):
        print("Pesanan kelas Yoga berhasil dibatalkan.")


class AngkatBeban(KelasLatihan):
    def pesanKelas(self):
        print("Pesanan kelas Angkat Beban berhasil dibuat.")

    def batalkanKelas(self):
        print("Pesanan kelas Angkat Beban berhasil dibatalkan.")


# Fungsi untuk melakukan pemesanan dan pembatalan kelas dengan polimorfisme
def main():
    # pemesanan dan pembatalan kelas Yoga
    kelas_yoga = Yoga()
    kelas_yoga.pesanKelas()
    kelas_yoga.batalkanKelas()

    # pemesanan dan pembatalan kelas Angkat Beban
    kelas_angkat_beban = AngkatBeban()
    kelas_angkat_beban.pesanKelas()
    kelas_angkat_beban.batalkanKelas()


if __name__ == "__main__":
    main()
