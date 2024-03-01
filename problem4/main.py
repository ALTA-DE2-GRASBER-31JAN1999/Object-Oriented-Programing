class Pengiriman:
    HARGA_STANDAR = 5000

    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi
        berat_pembulatan = round(self.berat)

        if volume < 50 or berat_pembulatan < 1:
            return 0

        harga = max(volume, berat_pembulatan) * Pengiriman.HARGA_STANDAR
        return harga


def main():
    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1

    pengiriman = Pengiriman(panjang, lebar, tinggi, berat)
    harga = pengiriman.hitung_harga()

    print(f"Harga : Rp {5000}")


if __name__ == "__main__":
    main()