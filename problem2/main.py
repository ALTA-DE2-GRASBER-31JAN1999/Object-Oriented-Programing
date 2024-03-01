class BangunRuang:
    def __init__(self, nama):
        self.nama = nama

    def hitung_volume(self):
        pass


class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__("Kubus")
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi


class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__("Tabung")
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return 3.14 * self.jari_jari ** 2 * self.tinggi


def main():
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)

    print("Volume")
    print(f"{kubus.nama} : {kubus.hitung_volume()}")
    print(f"{balok.nama} : {balok.hitung_volume()}")
    print(f"{tabung.nama} : {tabung.hitung_volume()}")


if __name__ == "__main__":
    main()