print("Selamat Datang!")
print("--Menu--")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
print("=======================")
print ("Silahkan memilih menu")
print("=======================")
pilih_menu = int(input("Masukan nomor menu yang anda pilih :"))
orang = ["Fawaz","Eko","Budi"]
nomor =["08123456789", "081298765432","081223344556677"]

if pilih_menu == 1:
     print ("Nama :", orang [0])
     print("No Telp :", nomor[0])
     print ("Nama :", orang [1])
     print("No Telp :", nomor[1])
     print ("Nama :", orang [2])
     print("No Telp :", nomor[2]) 
elif pilih_menu == 2:
    data = str(input("Masukan nama :"))
    data2 = str(input("Masukan nomor telepon :"))
    print("Kontak Telah berhasil ditambahkan")
elif pilih_menu == 3:
    print("******************************")
    print("Program selesai, sampai jumpa")
    print("******************************")
else:
    print("********************")
    print("Menu Tidak Tersedia")
    print("********************")
