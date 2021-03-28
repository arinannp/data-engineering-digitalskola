tahun_biasa = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
tahun_kabisat = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

inp_tanggal_mulai = input("Masukan tanggal mulai: ")
inp_tanggal_akhir = input("Masukan tanggal akhir: ")

tahun_mulai, bulan_mulai, hari_mulai = [int(data) for data in inp_tanggal_mulai.split("-")]
tahun_akhir, bulan_akhir, hari_akhir = [int(data) for data in inp_tanggal_akhir.split("-")]

# print(tahun_mulai, bulan_mulai, hari_mulai)
# print(tahun_akhir, bulan_akhir, hari_akhir)

total_hari_biasa = 0
total_hari_kabisat = 0
total_hari = 0

hari_tahun_kabisat1 = 0
hari_tahun_kabisat2 = 0
hari_tahun_kabisat3 = 0
hari_tahun_kabisat4 = 0
hari_tahun_kabisat_w = 0
hari_tahun_kabisat_x = 0
hari_tahun_kabisat_y = 0
hari_tahun_kabisat_z = 0

hari_tahun_biasa1 = 0
hari_tahun_biasa2 = 0
hari_tahun_biasa3 = 0
hari_tahun_biasa4 = 0
hari_tahun_biasa_w = 0
hari_tahun_biasa_x = 0
hari_tahun_biasa_y = 0
hari_tahun_biasa_z = 0

tahun_ke = tahun_mulai
total_bulan = 12

while tahun_ke != (tahun_akhir + 1):
    # print(tahun_ke)

    if tahun_ke % 4 == 0:
        # print('tahun kabisat', tahun_ke)

        if (tahun_ke == tahun_mulai) & (tahun_ke == tahun_akhir):
            for i in range((bulan_akhir - bulan_mulai) + 1):
                bulan_ke = bulan_mulai + i
                # print(bulan_ke)
                if bulan_ke == bulan_mulai:
                    hari_tahun_kabisat1 = (tahun_kabisat[bulan_ke] + 1) - hari_mulai
                elif bulan_ke == bulan_akhir:
                    hari_tahun_kabisat1 = hari_akhir
                else:
                    hari_tahun_kabisat1 = tahun_kabisat[bulan_ke]
                hari_tahun_kabisat_w += hari_tahun_kabisat1

        elif tahun_ke == tahun_mulai:
            for i in range((total_bulan - bulan_mulai) + 1):
                bulan_ke = bulan_mulai + i
                if bulan_ke == bulan_mulai:
                    hari_tahun_kabisat2 = (tahun_kabisat[bulan_ke] + 1) - hari_mulai
                else:
                    hari_tahun_kabisat2 = tahun_kabisat[bulan_ke]
                hari_tahun_kabisat_x += hari_tahun_kabisat2

        elif tahun_ke == tahun_akhir:
            for i in range(bulan_akhir):
                bulan_ke = i + 1
                if bulan_ke == bulan_akhir:
                    hari_tahun_kabisat3 = hari_akhir
                else:
                    hari_tahun_kabisat3 = tahun_kabisat[bulan_ke]
                hari_tahun_kabisat_y += hari_tahun_kabisat3

        else:
            for i in range(total_bulan):
                bulan_ke = i + 1
                hari_tahun_kabisat4 = tahun_kabisat[bulan_ke]
                hari_tahun_kabisat_z += hari_tahun_kabisat4

        total_hari_kabisat = (hari_tahun_kabisat_w + hari_tahun_kabisat_x + hari_tahun_kabisat_y + hari_tahun_kabisat_z)
        # print(hari_tahun_kabisat_w)
        # print(hari_tahun_kabisat_x)
        # print(hari_tahun_kabisat_y)
        # print(hari_tahun_kabisat_z)

    else:
        # print('tahun biasa', tahun_ke)

        if (tahun_ke == tahun_mulai) & (tahun_ke == tahun_akhir):
            for i in range((bulan_akhir - bulan_mulai) + 1):
                bulan_ke = bulan_mulai + i
                # print(bulan_ke)
                if bulan_ke == bulan_mulai:
                    hari_tahun_biasa1 = (tahun_biasa[bulan_ke] + 1) - hari_mulai
                elif bulan_ke == bulan_akhir:
                    hari_tahun_biasa1 = hari_akhir
                else:
                    hari_tahun_biasa1 = tahun_biasa[bulan_ke]
                hari_tahun_biasa_w += hari_tahun_biasa1

        elif tahun_ke == tahun_mulai:
            for i in range((total_bulan - bulan_mulai) + 1):
                bulan_ke = bulan_mulai + i
                if bulan_ke == bulan_mulai:
                    hari_tahun_biasa2 = (tahun_biasa[bulan_ke] + 1) - hari_mulai
                else:
                    hari_tahun_biasa2 = tahun_biasa[bulan_ke]
                hari_tahun_biasa_x += hari_tahun_biasa2

        elif tahun_ke == tahun_akhir:
            for i in range(bulan_akhir):
                bulan_ke = i + 1
                if bulan_ke == bulan_akhir:
                    hari_tahun_biasa3 = hari_akhir
                else:
                    hari_tahun_biasa3 = tahun_biasa[bulan_ke]
                hari_tahun_biasa_y += hari_tahun_biasa3

        else:
            for i in range(total_bulan):
                bulan_ke = i + 1
                hari_tahun_biasa4 = tahun_biasa[bulan_ke]
                hari_tahun_biasa_z += hari_tahun_biasa4

        total_hari_biasa = (hari_tahun_biasa_w + hari_tahun_biasa_x + hari_tahun_biasa_y + hari_tahun_biasa_z)
        # print(hari_tahun_biasa_w)
        # print(hari_tahun_biasa_x)
        # print(hari_tahun_biasa_y)
        # print(hari_tahun_biasa_z)

    # print(total_hari_kabisat)
    # print(total_hari_biasa)
    total_hari = total_hari_kabisat + total_hari_biasa
    tahun_ke += 1

print("Jumlah hari:", total_hari)
