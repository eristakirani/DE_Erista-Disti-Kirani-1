class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = str(nama)
        self.__usia = int(usia)
        self.__id_pelanggan = str(id_pelanggan)

    # Getter untuk nama
    def getNama(self):
        return self.__nama

    # Setter untuk nama
    def setNama(self, nama):
        self.__nama = str(nama)

    # Getter untuk usia
    def getUsia(self):
        return self.__usia

    # Setter untuk usia
    def setUsia(self, usia):
        self.__usia = int(usia)

    # Getter untuk ID pelanggan
    def getIdPelanggan(self):
        return self.__id_pelanggan

    # Setter untuk ID pelanggan
    def setIdPelanggan(self, id_pelanggan):
        self.__id_pelanggan = str(id_pelanggan)

    # Metode untuk menampilkan informasi pelanggan
    def tampilkanInfo(self):
        print("Nama Pelanggan:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__id_pelanggan)

if __name__ == "__main__":
    # Membuat objek pelanggan
    pelanggan1 = Pelanggan("kirana", 30, "D001")

    # Menampilkan informasi pelanggan
    print("Informasi Pelanggan:")
    pelanggan1.tampilkanInfo()

    # Mengubah nama pelanggan
    pelanggan1.setNama("rahel")
    pelanggan1.setUsia(25)
    pelanggan1.setIdPelanggan("D002")

    # Menampilkan informasi pelanggan setelah perubahan
    print("\nInformasi Pelanggan setelah perubahan:")
    pelanggan1.tampilkanInfo()
