'''
Se requiere añadir al LD_LIBRARY_PATH la ruta del runtime que se instala
'''
import os
os.environ['LD_LIBRARY_PATH'] = '/usr/local/MATLAB/MATLAB_Runtime/v910/runtime/glnxa64/'

import matplotlib.pyplot as plt
import analisis_espectral

def analizar_espectro(filename):
    resx = ae.analisis_espectral(filename, nargout=2)
    return resx


if __name__ == '__main__':
    ae = analisis_espectral.initialize()
    resx = ae.analisis_espectral('xn.txt', nargout=2)
    rexy = ae.analisis_espectral('yn.txt', nargout=2)
    plt.plot(resx[0])
    plt.show()
    plt.plot(resx[1])
    plt.show()
    #plt.plot(yfft)
    #plt.show()
