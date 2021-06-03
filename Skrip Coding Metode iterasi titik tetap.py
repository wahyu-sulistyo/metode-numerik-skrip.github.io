# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 07:32:53 2021

@author: Asus
"""

#Wahyu Sulistiyono,28,M4C
#Kuis Praktek Metode Numerik
print("Buatlah program python menggunkan metode Newton Raphson yang dimodifikasi untuk menyelesaikan persamaan berikut :")
print("f(x)=27x^4+162x^3-180x^2+62x-7")
print("Dengan tebakan awal 0 dan galat toleransi 〖1.10〗^(-4)")
#("Diketahui : X0= 0,Galat = 0.0001")

#mengakses modul
import math
import numpy as np

#Mendefinisikan fungsi x beserta Turunan pertama dan kedua dari fungsi x
def f(x) :
    return 4*x - 64*x**3
#menentukan fungsi g(x)
def g(x) :
    return 1/18*x 


#Diketahui
#Nilai Tebakan Awal
xn = 4
#Nilai Galat
galat = 0.0001
#nilai n
start = 0

#Menyusun pencarian Akar dengan metode iterasi titik tetap
condition = True
while condition:
    #Rumus xr+1 pada Newton Rapson Modif
    xr = g(xn)
    #Syarat dari Nilai Akar harus lebih kecil dari galat
    mt = abs(xr - xn)
    #perintah agar ketika nilai akar lebih kecil dari galat,iterasi dihentikan
    if mt <= galat :
        print('iterasi/penghitungan  ke', start,'adalah :',mt)
        break
    else:
        xn = xr
        print('iterasi/penghitungan  ke', start,'adalah :',mt)
        start +=1