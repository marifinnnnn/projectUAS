from Model.daftar_nilai import data_mahasiswa


def tampil():
    if data_mahasiswa.items():
        print('\n========================== Daftar Nilai Mahasiswa ====================================')
        print('======================================================================================')
        print('|  NO. |      NAMA     |     NIM    |    TUGAS   |   UTS   |   UAS   |  NILAI AKHIR  |')
        print('======================================================================================')
        i = 0
        for x in data_mahasiswa.items():
            i += 1
            print('| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | '
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print('======================================================================================')
    else:
        print('===================================== Daftar Nilai ===================================')
        print('======================================================================================')
        print('|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |')
        print('======================================================================================')
        print('|                                    Tidak Ada Data                                  |')
        print('======================================================================================')



def caridata():
    nama = input("Masukan Nama\t: ")
    if nama in data_mahasiswa.keys():
        print("============================ Daftar Nilai ========================================")
        print("==================================================================================")
        print("====================| NAMA | (NIM, TUGAS, UTS, UAS, NILAI AKHIR) |================")
        print("==================================================================================")
        print("                    | {0} | {1} | ".format(nama, data_mahasiswa[nama]))
        print("==================================================================================")
    else:
        print("Datanya {0} tidak ada ".format(nama))
Footer
