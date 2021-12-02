# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:26:53 2021

@author: jofin
"""

def buat(nf):
    nama = input('Masukkan Nama : ')
    nim = input('Masukkan NIM : ')
    tahun = input('Masukkan Tahun Angkatan : ')
    teks = 'Nama: {}\nNIM: {}\nTahun Angkatan{}'.format(nama, nim, tahun)

    file_serti = open(str(nf), "w")
    file_serti.write(teks)
    file_serti.close()
    print('File Telah DItambahkan')
    
    
def baca(bf):
    file_biodata = open(str(bf), "r")
    print(file_biodata.read())
    print()
    file_biodata.close()


def tambah(tf) :
    sahabat = input('Masukkan Nama Sahabat : ')
    catatan = input('Masukkan Catatan Tambahan : ')
    
    teks = 'Nama Sahabat: {}\nCatatan: {}'.format(sahabat, catatan)
    file_serti = open(str(tf), "a")
    file_serti.write(teks)
    file_serti.close()
    
    
    
n = ''

print('--- Program File ---')
print('1. Membuat Dan Menulis File')
print('2. Membaca File')
print('3. Menambah Text Pada File')
print('4. Keluar Dari Program')

while (n != '4'):
    n = int(input('Masukkan Pilihan Berupa Angka Yang Tertera Diatas : '))
    
    if n == 4:
        print('Terima Kasih Telah Menggunakan Program Kami')
        break
    if n == 1:
        nf = str(input('Masukkan Nama File : '))
        buat(nf)
    elif n == 2 :
        bf = str(input('Masukkan Nama File Yang Ingin Dibaca : '))
        baca(bf)
    elif n == 3 :
        tf = str(input('Masukkan Nama File Yang Ingin Ditambah : '))
        tambah(tf)
    else : 
        print('Tolong Masukkan Sesuai Angka Diatas !')