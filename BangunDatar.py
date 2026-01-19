# Daftar bangun datar yang didukung dengan 4 jenis bangun datar
daftar_BangunDatar = ["persegi", "persegi panjang", "lingkaran", "segitiga sama sisi"]


def luaspersegi(sisi):
    return sisi * sisi
def kelilingpersegi(sisi):
    return 4 * sisi
# Tambahkan fungsi untuk bangun datar lain
def luaspersegipanjang (panjang,lebar):
    return panjang * lebar
def kelilingpersegipanjang (panjang, lebar):
    return 2 * (panjang + lebar)
def luassegitiga(alas, tinggi):
    return (alas * tinggi) / 2
def kelilingsegitiga(s1, s2, s3):
    return s1 + s2 + s3
def luaslingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari
def kelilinglingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

nama = input("masukkan nama anda:")

print(nama, " ,selamat datang di program Bangun Datar")

print("Pilih Bangun Datar")
daftar_Bangun_Datar = [
    "1. pesegi",
    "2.persegi panjang",
    "3.segitiga", 
    "4.lingkaran"
    ]
i = 0
while i < len(daftar_Bangun_Datar):
    print(daftar_Bangun_Datar[i])
    i += 1

pilihan = int(input("masukan pilihan anda(1-4): "))

while True:
    if pilihan == 1:
        sisi = int(input("Masukan Sisi Persegi: "))
        print("Luas Persegi adalah:", luaspersegi(sisi))
        print("Keliling Pesegi adalah:", kelilingpersegi(sisi))
        
   
    elif pilihan == 2:
        print("Anda Mamilih Persegi Panjang")
        panjang = int(input("masukan panjang: "))
        lebar = int(input("masukan lebar: "))
        print("luas persegi panjang adalah:", luaspersegipanjang(panjang,lebar))
        print("keliling persegi panjang adalah:", kelilingpersegipanjang(panjang,lebar))
        
    elif pilihan == 3:
        print("Anda Memilih Segitiga")
        alas = int(input("Masukan Alas"))
        tinggi = int(input("Masukan Tinggi"))
        print("luas segitiga adalah:" ,luassegitiga(alas, tinggi))
        s1 = int(input("masukkan sisi 1:"))
        s2 = int(input("masukkan sisi 2:"))
        s3 = int(input("masukkan sisi 3:"))
        print("keliling segitiga adalah:",kelilingsegitiga(s1, s2, s3))
       

    elif pilihan == 4:
        print("Anda Memilih Lingkaran")
        jari_jari = int(input("masukan jari-jari:" ))
        print("luas lingkaran adalah:",luaslingkaran(jari_jari))
        print("keliling lingkaran adalah:",kelilinglingkaran(jari_jari))
    break
while True:
    print("\nMenu Bangun Datar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        sisi = int(input("Masukkan sisi: "))
        print("Luas:", luaspersegi(sisi))
        print("Keliling:", kelilingpersegi(sisi))

    elif pilihan == "2":
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        print("Luas:", luaspersegipanjang(panjang, lebar))
        print("Keliling:", kelilingpersegipanjang(panjang, lebar))

    elif pilihan == "3":
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        print("Luas:", luassegitiga(alas, tinggi))

    elif pilihan == "4":
        jari = int(input("Masukkan jari-jari: "))
        print("Luas:", luaslingkaran(jari))
        print("Keliling:", kelilinglingkaran(jari))

    else:
        print("Pilihan tidak valid!")
        continue

    hitung_lagi = input("Hitung lagi? (ya/tidak): ").lower()
    if hitung_lagi != "ya":
        print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI ;) ")
        break