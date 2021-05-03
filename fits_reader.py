from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

path_to_data = '/madfs/data/dc-fuma1/MUSELLSDATA/'

QSOlist = np.loadtxt('QSOlist.txt', dtype =str)
J_dir = QSOlist[:,0]

QSO_fits_example = fits.open(path_to_data + str(J_dir[5]) + '/COMBINED_CUBE_bootvar_cubex.fits')
QSO_fits_example.info()

#header_fits = open('header_example.txt', 'w')
#header_fits.write(str(QSO_data_fits[5][0].header))
#header_fits.close()

#### APERTURA DI TUTTI I 28 FITS file #######

#QSO_data_fits = []

#for i in range(len(J_dir)):

#    QSO_data_fits.append(fits.open(path_to_data + str(J_dir[i]) + '/COMBINED_CUBE_bootvar_cubex.fits' ))

#    if ((i+1)%28) == 0:
#        print('caricato ' + str(i+1) + '/28')

 