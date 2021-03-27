import datetime
from datetime import date

inp_tanggal_mulai = input('Masukan tanggal mulai: ')
inp_tanggal_akhir = input('Masukan tanggal akhir: ')

tahun_mulai, bulan_mulai, hari_mulai = [int(data) for data in inp_tanggal_mulai.split('-')]
tahun_akhir, bulan_akhir, hari_akhir = [int(data) for data in inp_tanggal_akhir.split('-')]

tanggal_mulai = date(tahun_mulai, bulan_mulai, hari_mulai)
tanggal_akhir = date(tahun_akhir, bulan_akhir, hari_akhir)
total_hari = tanggal_akhir - tanggal_mulai

print('Jumlah hari:', total_hari, 'exclude first day')
