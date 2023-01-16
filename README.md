# PROJEK-UAS
NAMA : Muhammad arifin
NIM : 312210330
KELAS : TI.22.A3


Buat paket dan modul dengan struktur


![1](https://user-images.githubusercontent.com/115518274/212716024-e1022312-2d10-4427-b5ef-232023135070.png)


Untuk membuat Package Modul kita buka aplikasi PyCharm :


<img width="594" alt="UAS" src="https://user-images.githubusercontent.com/115518274/212716667-add3ae6f-542b-43b9-b8e0-ae970171b7f3.png">


Pilih New Project Lalu simpan project sesuai Location Directory dan beri nama folder :


<img width="247" alt="P" src="https://user-images.githubusercontent.com/115518274/212716905-14026a0f-3be5-47ec-b363-8dd64b89797d.png">


Kemudian Pilih New > Python Package :


![O](https://user-images.githubusercontent.com/115518274/212717555-5b25aea2-012e-4e82-afef-706509593880.png)


 " -> Kita buat Nama Model dan View "


Tampilan folder Package Model dan View yang terdapat file_init_.py


![I](https://user-images.githubusercontent.com/115518274/212717995-bb589fe8-e781-4d82-9aff-35fab4babe55.png)


Kemudian kita buat nama program Python dengan Klik Folder Model > pilih New >Python File dengan nama : daftar_nilai.py


![U](https://user-images.githubusercontent.com/115518274/212718301-a9b96371-ba40-4b6a-9679-092df5b5a686.png)


Lalu kita buat nama program Python dengan Klik Folder view > pilih New >Python File dengan nama : input_nilai.py dan view_nilai.py


![2](https://user-images.githubusercontent.com/115518274/212718619-175ff11d-ea20-442f-be10-e1a9739695ff.png)


Nama program python sudah kita buat :


![3](https://user-images.githubusercontent.com/115518274/212718684-8ed7b551-6662-43ff-bff5-e987ed52da8f.png)


Buat sintaks program python


**Membuat kode program : daftar_nilai.py**


![0](https://user-images.githubusercontent.com/115518274/212719156-b8798548-7a45-4fbe-9d30-2868172604ff.png)
![1](https://user-images.githubusercontent.com/115518274/212719809-c7c46466-3aa8-4616-b103-712ffac2d8f7.png)



Penjelasan :

~ Disini kita menggunakan kamus ya untuk menyimpan inputan data mahasiswa
Def tambahkan : Dibagian ini kita gunakan print untuk penulisan bagian input data mahasiswa nanti agar terlihat rapih
Def hapus :
Disini kita buat inputan yang menginput nama
Gunanya untuk menghapus data mahasiswa dari nama mahasiswa itu sendiri
Kita gunakan del untuk fungsi menghapus datanya
(Jika)Jika mahasiswa tersebut ada maka data mahasiswa tersebut akan terhapus
(Else)Jika nama mahasiswa tersebut tidak ada maka datanya tidak akan ditemukan
Def ubah
Penjelasan:
Disini kita hampir sama dengan yang hapus, kita gunakan inputan nama untuk mengubah NIM, Nilai Tugas, Ujian Tengah Semester(UTS), ataupun Ujian Akhir Semester(UAS)
Lalu setelah kita memasukkan nama maka dictionary akan mengeksekusi program menggunakan keys untuk mencari data dari nama mahasiswa tersebut
(Jika)Jika nama mahasiswa tersebut ketemu atau ada didalam data maka program akan masuk ke inputan NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS yang baru
(Else)Jika nama mahasiswa tersebut tidak ada didalam data maka program akan memunculkan tulisan atau perintah bahwa data mahasiswa tidak ada
Def cari
Penjelasan:
Fungsinya sama dengan tambahkan Def

**Membuat kode program input_nilai.py**


![2](https://user-images.githubusercontent.com/115518274/212719946-69f9c531-a3ce-4d51-be04-6c6c50871464.png)




Penjelasan:

Dari dan impor
Penjelasan:
From digunakan untuk memanggil package temporary import untuk tujuan yang kita pilih yaitu modul daftar_nilai

Lalu kita gunakan import data_mahasiswa itu gunanya agar saat kita menginputkan data atau setiap kali kita menambah data maka data mahasiswa secara otomatis akan masuk ke dalam dictionary meskipun berbeda atau paket terpisah dan juga modulnya

Def tambah data
Penjelasan:

Disini kita buat inputan karena tadi kita sudah membuat kata - kata outputnya kali ini kita cukup membuat inputan data mahasiswanya saja
Jangan lupa gunakan penambahan untuk menghitunghasil total atau rata- ratanya
**Membuat kode program view_nilai.py **


![3](https://user-images.githubusercontent.com/115518274/212720109-cdb8e948-5f70-4c97-a26d-a24f06d22893.png)
![4](https://user-images.githubusercontent.com/115518274/212720485-d8697b56-527b-41bc-886f-25f9f6aa4206.png)


Penjelasan:

Dari dan impor
Penjelasan:
Fungsinya sama saja dengan yang ada dibagian Input_Nilai

Def tampil
Penjelasan:

Disini kita buat sebuah tabel untuk menampilkan data - data dan nama - nama mahasiswa didalam kamus
(Jika)Jika terdapat data maka data dan nama mahasiswa tersebut akan muncul
Disini kita menggunakan for untuk melakukan perulangan nomor urut
(Else)Jika kita belum menginputkan data sama sekali maka akan muncul tulisan "tidak ada data"
Def mencari data
Penjelasan:

Tadi kita sudah buat print sama seperti dibagian Input_Nilai
Kita akan langsung membuat inputan dengan format nama untuk mencari data dari mahasiswa yang sedang kita cari
(If)Jika data mahasiswa yang dicari ada didalam kamus maka data baik Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS akan muncul
(Else)Jika data mahasiswa yang dicari tidak ada didalam kamus maka akan muncul tulisan "datanya tidak ada"
**Membuat kode program : main.py**


![5](https://user-images.githubusercontent.com/115518274/212720171-9c9b03f6-4931-4f29-89c2-bbab9c1e9c85.png)


Dari dan impor
Penjelasan:
Sama seperti sebelumnya hanya disini saja sedikit berbeda

Dari sini kita tulis package.modulnya lalu import fungsi(def) tadi

Karena dibagian utama ini kita akan menggunakan atau membuat menu pilihan sintaks

Sementara Benar
Penjelasan:

Kita gunakan print untuk membuat pilihan menunya
Lalu kita buat inputan untuk memilih menu nanti ketika program dijalankan
(If dan Elif)Kita gunakan karena kita akan membuat cabang pilihan yang banyak
Lalu dibawahnya kita tambahkan juga fungsi - fungsi yang sudah kita buat tadi
Pada perintah ke 6 kita gunakan break untuk keluar dari program yang kita jalankan
(Else)Jika kita tidak memilih salah satu menu tersebut maka akan muncul peringatan "pilih menu yang tersedia diatas"
Menjalankan program python
Untuk menjalankan program kita klik : Run > main.py
Pilih Menu Nomor : 1. Tambah


Pilih Menu Nomor : 2. Tampil


Untuk menambah data lagi, pilih Menu Nomor : 1. Tambah


Untuk menampilkan data yang kita tambah,Pilih Menu Nomor : 2. Tampil


Pilih Menu Nomor : 3. Hapus


Untuk menampilkan data yang kami hapus,Pilih Menu Nomor : 2. Tampil


Pilih Menu Nomor : 4.Ubah


Untuk menampilkan data yang kami ubah,Pilih Menu Nomor : 2. Tampil


Pilih Menu Nomor : 5. Cari
Kemudian ketik Nama Mahasiswa



Pilih Menu Nomor : 6. Keluar dari program
