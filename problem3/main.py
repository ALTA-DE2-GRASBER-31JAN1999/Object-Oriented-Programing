class Kalkulator:
    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(self, a, b):
        return a - b

    def perkalian(self, a, b):
        return a * b

    def pembagian(self, a, b):
        return a / b


def main():
    kalkulator = Kalkulator()

    angka1 = 3
    angka2 = 4
    hasil_penjumlahan = kalkulator.penjumlahan(angka1, angka2)
    print(f"Penjumlahan : {hasil_penjumlahan}")

    angka1 = 15
    angka2 = 4
    hasil_pengurangan = kalkulator.pengurangan(angka1, angka2)
    print(f"Pengurangan : {hasil_pengurangan}")

    angka1 = 10
    angka2 = 10
    hasil_perkalian = kalkulator.perkalian(angka1, angka2)
    print(f"Perkalian : {hasil_perkalian}")

    angka1 = 12
    angka2 = 3
    hasil_pembagian = kalkulator.pembagian(angka1, angka2)
    print(f"Pembagian : {hasil_pembagian}")


if __name__ == "__main__":
    main()