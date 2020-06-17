#!/usr/bin/env pypy
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import os

def reduce_array(n, arr):
    out = []
    r = arr.shape[0]
    c = arr.shape[1]
    for i in range((r + n-1)//n):
        out.append([])
        for j in range((c+n-1)//n):
            summa = 0
            num = 0
            for di in range(n):
                for dj in range(n):
                    if(i*n + di >= r or j*n + dj >= c):
                        continue
                    summa += arr[i*n+di][j*n+dj]
                    num += 1
            out[-1].append(summa/num)
    return np.array(out, dtype="int16")

def getband(bandnumber,array):
  temp = array[bandnumber]
  #temp = temp[4000:10000, 3500:]  #Crop images here
  return temp

  

def savePic(filename):
  dataset = gdal.Open("MTD_MSIL1C.xml").GetSubDatasets()[0][0]
  array = gdal.Open(dataset).ReadAsArray()
  blue = getband(0,array)
  green = getband(1,array)
  red = getband(2,array)
  nir = getband(3,array)

def calc_ndvi(save_name, dir_name, red_num):
        sds = gdal.Open(dir_name + "/MTD_MSIL1C.xml", gdal.GA_ReadOnly).GetSubDatasets()
        data = gdal.Open(sds[0][0]).ReadAsArray()
        blue = getband(0,data)
        green = getband(1,data)        
        red = getband(2,data)
        nir = getband(3,data)

        
        blue_red = reduce_array(red_num, blue.astype(float))
        green_red = reduce_array(red_num, green.astype(float))
        red_red = reduce_array(red_num, red.astype(float))
        nir_red = reduce_array(red_num, nir.astype(float))
        np.savez(dir_name +"/"+ save_name, red=red_red, nir=nir_red, blue=blue_red, green=green_red)
        


#calc_ndvi(save_name,	dir_name,	red_num)
calc_ndvi("bgrnir.npz", "Forest_fires/Australia/20200130.SAFE", 3) 


