# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:13:20 2021

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
    return 27*x**4 + 162*x**3 - 180*x**2 + 62*x -7
#Turunan Pertama Fungsi X
def g(x) :
    return 108*x**3 + 486*x**2 - 360*x + 62
#Turunan Kedua Fungsi x
def h(x) :
    return 324*x**2 + 972*x - 360

#Diketahui
#Nilai Tebakan Awal
xn = 0
#Nilai Galat
galat = 0.0001
#nilai n
start = 0

#Menyusun pencarian Akar dengan metode Newton Rhapson Modifikasi
condition = True
while condition:
    #Rumus xr+1 pada Newton Rapson Modif
    xr = xn - ((f(xn) * g(xn)) / ((g(xn) **2) - h(xn) * f(xn)))
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