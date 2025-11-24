# 1. Program Lengkap Nilai Tempat pada Suatu Bilangan (Maksimal 10 Juta)
# Menampilkan digit, nama tempat, dan nilai angka secara rapi

# Input bilangan
bilangan = int(input("Masukkan bilangan (maksimal 20.000.000): "))

if bilangan > 20_000_000:
    print("Bilangan tidak boleh lebih dari 20 juta!")
else:
    print("\n====================================")
    print("   PROGRAM NILAI TEMPAT BILANGAN   ")
    print("====================================")
    print(f"Bilangan: {bilangan:,}".replace(",", "."))
    print("------------------------------------")
    print(f"{'Digit':<10}{'Nama Tempat':<20}{'Nilai Angka':>20}")
    print("------------------------------------")

    # Daftar nama tempat (hingga jutaan)
    nama_tempat = [
        "satuan",
        "puluhan",
        "ratusan",
        "ribuan",
        "puluh ribuan",
        "ratus ribuan",
        "jutaan"
    ]

    # Ubah bilangan ke string
    str_bil = str(bilangan)
    panjang = len(str_bil)

    # Tampilkan hasil
    for i, digit in enumerate(str_bil):
        posisi = panjang - i - 1
        nama = nama_tempat[posisi] if posisi < len(nama_tempat) else f"10^{posisi}"
        nilai_tempat = int(digit) * (10 ** posisi)
        print(f"{digit:<10}{nama:<20}{nilai_tempat:>20,}".replace(",", "."))

    print("------------------------------------")
    print("Keterangan: Nilai tempat menunjukkan posisi dan nilai setiap digit dalam bilangan.")