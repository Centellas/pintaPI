import suport_motors as s
import numpy as np
#import cv2
#import bw_test
#from matplotlib import pyplot as plt
#plt.rcParams['image.cmap']='gray'

img = np.loadtxt("test.txt",dtype=np.int)
#img = bw_test.transform()

height, width = img.shape[:2]
i = 0
for fila in img:
    if i %2 == 0:
        for columna in fila:
            if columna != 255:
		#print ("baixa llapis")
            	s.up_down_pen()
            	#print ("mou despres")
            	s.moure_eix_secundari(0)
            else:
                #print ("mou a la seguent posicio")
                s.moure_eix_secundari(0)
    else:

#    for j in fila:
#        print ("inici linea")
#        s.moure_eix_secundari(1)

        for j in np.flip(fila,0):
            if j != 255:
                #print ("baixa llapis")
                s.up_down_pen()
                #print ("mou despres")
                s.moure_eix_secundari(1)
            else:
                #print ("mou a la seguent posicio")
                s.moure_eix_secundari(1)
    #print ("mou a la seguent linea")
    s.moure_eix_principal(1)
    i=i+1
#print ("torna al inici")    
for i in img:
    s.moure_eix_principal(0)
#if i % 2 != 0:
    #s.moure_eix_secundari(1)
print ("finish")
