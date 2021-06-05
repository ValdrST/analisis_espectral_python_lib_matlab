'''
Clase que se encarga de graficar
'''
import numpy as np 

import matplotlib.pyplot as plt
from math import pi
'''
Se requiere añadir al LD_LIBRARY_PATH la ruta del runtime que se instala
'''
import os
os.environ['LD_LIBRARY_PATH'] = '/usr/local/MATLAB/MATLAB_Runtime/v910/runtime/glnxa64'
import analisis_espectral

class Graficador():
  def __init__(self, data, out_file="/tmp/grafica.png", type = None):
    self.data = data
    self.out_file = out_file
    self.type = type
  
  def crear_grafica(self):
    ax = plt.subplot()
    ax.set_title(self.data["title"])
    ax.set_xlabel(self.data["xlabel"])
    ax.set_ylabel(self.data["ylabel"])
    for data_list in self.data["data"]:
        ax.plot(data_list)
    plt.legend(self.data["labels"],labelspacing=0.1, fontsize='small')
    plt.savefig(self.out_file)
    plt.close()
  

  def get_data(self, filename):
    ae = analisis_espectral.initialize()
    res = ae.analisis_espectral(filename, nargout=2)
    self.data = {
      "title": "Análisis Espectral",
      "xlabel": "X",
      "ylabel": "Y",
      "labels":["Respuesta en frecuencia"],
      "data": [np.log(res[1])/np.log(20)]
    }
    return res
