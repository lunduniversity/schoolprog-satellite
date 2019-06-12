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

def calc_ndvi(save_name, dir_name, red_num):

    try:
        with np.load(save_name + ".npz", "r") as data:
            RED_red = data["red"]
            NIR_red = data["nir"]
        #plt.imshow(NIR_red)
        #plt.savefig("NIR_red.png")

    except FileNotFoundError:
        sds = gdal.Open(dir_name + "/MTD_MSIL1C.xml", gdal.GA_ReadOnly).GetSubDatasets()
        data = gdal.Open(sds[0][0]).ReadAsArray()
        RED = data[2]
        NIR = data[3]
        RED = RED[3500:5500, 8000:10000]
        NIR = NIR[3500:5500, 8000:10000]
        
        RED_red = reduce_array(red_num, RED.astype(float))
        NIR_red = reduce_array(red_num, NIR.astype(float))
        np.savez(save_name + ".npz", RED_red, NIR_red, red=RED_red, nir=NIR_red)
        


    ndvi = (NIR_red.astype(float) - RED_red.astype(float))/(NIR_red.astype(float) + RED_red.astype(float))
    fig = plt.figure(figsize=(10,10))
    plt.pcolormesh(ndvi, cmap='PiYG')
    plt.ylim(ndvi.shape[0], 0)
    plt.clim(-1, 1)
    plt.colorbar(label="NDVI")
    plt.savefig(save_name + "ndvi.png")

def calc_ndvi_folder(folder_name, save_folder):
    for path in os.listdir(folder_name):
        calc_ndvi(save_folder + "/" + path + "_computed", folder_name + "/" + path, red_number)


red_number = 3

calc_ndvi_folder("same_pic_bokskog", "bokskogen_bra")


