#inisialisasi nama file
daftar_file = "Nomor.txt"

#menyetel book dari file
daftar = {}
with open(daftar_file, "r") as no:
    for line in no:
        nama, nomor = line.strip().split("\t")
        daftar[nama] = nomor

while True :
    print("Masuk ke dalam Kontak\n1. Tambah Kontak\n2. Hapus Kontak\n3. Update Kontak\n4. Lihat Kontak\n5. Cari Kontak\n6. Keluar...")

    pilihan = input("Pilihan : ")


    #kondisi dimana input user memengaruhi menu yang dipilihnya.
    #tambah kontak
    if pilihan == "1":
        nama  = input("Masukkan nama kontak : ")
        nomor = input("Masukkan nomor kontak : ")
        daftar[nama] = nomor
        print(f"{nama} telah ditambahkan kedalam kontak.\n")

    #hapus kontak
    elif pilihan == "2":
        nama = input("Masukkan nama kontak yang akan dihapus : ")
        if nama in daftar:
            del daftar[nama]
            print(f"{nama} telah dihapus dari kontak.\n")
        else :
            print(f"{nama} tidak ada didalam kontak.\n")
    
    #update kontak
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan di-Update : ")
        if nama in daftar:
            nomor = input("Masukkan nomor kontak yang baru : ")
            daftar[nama] = nomor
            print(f"{nama} telah berhasil di-Update.\n")
        else :
            print(f"{nama} tidak ada didalam kontak.\n")
        
    #lihat kontak
    elif pilihan == "4":
        if daftar:
            print("\nList kontak: ")
            for nama, nomor in daftar.items():
                print(f"{nama} \t {nomor}")
            print()
    
    #cari kontak
    elif pilihan == "5":
        nama = input("Masukkan nama yang dicari :")
        if nama in daftar:
            print(f"{nama} \t {nomor}\n")
        else :
            print(f"{nama} tidak ada didalam kontak.\n")

    #keluar program
    elif pilihan == "6":
        with open(daftar_file, "w") as no:
            for nama, nomor in daftar.items():
                no.write(f"{nama} \t {nomor}\n")
        
        print("Anda telah keluar dari kontak list\n")
        break

    else :
        print("Masukkan pilihan dengan benar!\n")

