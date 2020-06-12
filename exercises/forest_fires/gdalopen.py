from osgeo import gdal
import numpy as np


def savePic(filename):
  dataset = gdal.Open("MTD_MSIL1C.xml").GetSubDatasets()[0][0]
  array = gdal.Open(dataset).ReadAsArray()
  RED = array[2] 
  RED = RED[7000:-1, 1000:3000]
  NIR = array[3]
  NIR = NIR[7000:-1, 1000:3000]
  np.savez(filename+ ".npz", red=RED, nir=NIR)

savePic("red_and_nir")
  
