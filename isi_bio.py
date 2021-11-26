# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:28:12 2021

@author: jofi
"""


def masukkan():
    teks = "Nama: {}\nUmur: {}\nAlamat: {}\nEmail: {}\nDosen Wali: {}".format(nama, umur, alamat, email, dosen)

    file_bio = open("Biodata.txt", "w")
    file_bio.writelines(teks)
    file_bio.close()
    
    keluaran()

def keluaran():
    file_biodata = open("Biodata.txt", "r")
    print(file_biodata.read())
    file_biodata.close()




nama = input('Masukkan Nama : ')
umur = input('Masukkan Umur : ')
alamat = input('Masukkan Alamat : ')
email = input('Masukkan Email : ')
dosen = input('Masukkan Dosen Wali : ')

masukkan()