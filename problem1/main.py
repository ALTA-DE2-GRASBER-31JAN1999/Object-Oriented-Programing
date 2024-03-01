class BangunDatar:
    def __init__(self, nama):
        self.nama = nama

    def hitung_luas(self):
        pass

    def hitung_keliling(self):
        pass


class Persegi(BangunDatar):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi, sisi1, sisi2, sisi3):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return self.sisi1 + self.sisi2 + self.sisi3


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


def main():
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4, 3, 4, 5)
    persegi_panjang = PersegiPanjang(7, 8)

    print("Luas")
    print(f"{persegi.nama} : {persegi.hitung_luas()}")
    print(f"{segitiga.nama} : {segitiga.hitung_luas()}")
    print(f"{persegi_panjang.nama} : {persegi_panjang.hitung_luas()}")

    print("\nKeliling")
    print(f"{persegi.nama} : {persegi.hitung_keliling()}")
    print(f"{segitiga.nama} : {segitiga.hitung_keliling()}")
    print(f"{persegi_panjang.nama} : {persegi_panjang.hitung_keliling()}")


if __name__ == "__main__":
    main()