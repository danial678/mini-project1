print('Nama = Danial Hirzan Akbary')
print('NIM  = 2409116098')

print('-----------------------(selamat datang user)-------------------------')
print('-----(silahkan masukan username dan password untuk proses regis)-----')
#program regis
nama = str(input('masukan username yang ingin di gunakan = '))
sandi = str(input('masukan sandi menggunakan (NIM)        = '))

#proses login 
login = True
while login:
    print('-----anda memasuki menu login-----')
    username = str(input("masukan username anda = " ))
    password = str(input("masukan password anda = " ))
    if username==nama and password==sandi:
        print('----------Selamat Datang' ,nama , 'dengan Nim' , sandi,'----------')
#proses transak si (penghitungan diskon)
        barang = str(input('masukan nama barang belanjaan pelangan = '))
        harga = int(input('masukan harga barang yang pembeli inginkan = Rp'))
        jumlah = int(input('masukan jumlahnya = '))
        jumlah2 = harga * jumlah

        if jumlah2 >= 250000:
            diskon = jumlah2 - (0.25 * jumlah2)
            harga = jumlah2 - diskon
            print('-----selamat karena total belanja anda >= 250rb-----')
            print('anda mendapatkan diskon sebesar 25%')
            print('sehingga harga yang anda bayar menjadi = Rp',diskon)
            print('____________________________________________________')
            print('silahkan pilih menu dibawah ini')
            print('1.transaksi selesai')
            print('2.transaksi lainya')
            pilihan = int(input('masukan pilihan anda = '))
            if pilihan == 1 :
                break
            elif pilihan == 2:
                print('transaksi dilanjutkan')
            else:
                print('pilihan yang anda masukan tidak valid')
                break

        else:
            print('total harga barang anda tidak memenuhi untuk mendapatkan diskon')

#menu perulangan
            print('silahkan pilih menu dibawah ini')
            print('1.transaksi selesai')
            print('2.transaksi lainya')
            pilihan = int(input('masukan pilihan anda = '))
            if pilihan == 1 :
                print('-----(transaksi anda selesai)-----')
                break
            elif pilihan == 2:
                print('-----(transaksi dilanjutkan)-----')
            else:
                print('pilihan yang anda masukan tidak valid')
                break
    
    elif username==nama or password==sandi:
        print('-----(username atau password salah coba lagi)-----')
    else:
        print("-----(username dan pasword salah coba lagi)-----")