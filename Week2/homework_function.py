try:
    film = input('Masukan nama film: ')
    tiket_terjual = int(input('Masukan jumlah tiket terjual: '))
    harga_tiket = int(input('Masukan harga tiket: Rp'))
    kota_diputar = set(input('Kota tempat film diputar: ').split(','))
except:
    print('Masukan input transaksi yang benar!!!')


def transaksi_tiket(film, tiket_terjual, harga_tiket, kota_diputar):
    total_pendapatan = tiket_terjual * harga_tiket
    print('Tiket film "' + film + '" terjual sebanyak ' + str(tiket_terjual) +
          ' dengan total pendapatan Rp' + str(total_pendapatan) + 
          ' di kota', tuple(kota_diputar))


transaksi_tiket(film, tiket_terjual, harga_tiket, kota_diputar)
