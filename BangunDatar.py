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
        break # keluar loop setelah hitung selesai
   
    elif pilihan == 2:
        print("Anda Mamilih Persegi Panjang")
        panjang = int(input("masukan panjang: "))
        lebar = int(input("masukan lebar: "))
        print("luas persegi panjang adalah:", luaspersegipanjang(panjang,lebar))
        print("keliling persegi panjang adalah:", kelilingpersegipanjang(panjang,lebar))
        break # keluar loop setelah hitung selesai

    elif pilihan == 3:
        print("Anda Memilih Segitiga")
        alas = int(input("Masukan Alas"))
        tinggi = int(input("Masukan Tinggi"))
        print("luas segitiga adalah:" ,luassegitiga(alas, tinggi))
        s1 = int(input("masukkan sisi 1:"))
        s2 = int(input("masukkan sisi 2:"))
        s3 = int(input("masukkan sisi 3:"))
        print("keliling segitiga adalah:",kelilingsegitiga(s1, s2, s3))
        break # keluar loop setelah hitung selesai

    elif pilihan == 4:
        print("Anda Memilih Lingkaran")
        jari_jari = int(input("masukan jari-jari:" ))
        print("luas lingkaran adalah:",luaslingkaran(jari_jari))
        print("keliling lingkaran adalah:",kelilinglingkaran(jari_jari))
        break # keluar loop setelah hitung selesai

    else:
        print("Pilihan Tidak Tersedia")
        # Minta input ulang jika pilihan salah
        pilihan = int(input("Masukan pilihan anda kembali (1-4):"))
#SELESAI  TERIMA KASIH