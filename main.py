import suport_motors as s
import numpy as np
import bw_test


img = bw_test.transform() 

height, width = img.shape[:2]
i = 0
for fila in img:
    if i %2 == 0:
        for columna in fila:
            if columna != 255:
            	s.up_down_pen()
            	s.moure_eix_secundari(0)
            else:
                s.moure_eix_secundari(0)
    else:
        for j in np.flip(fila,0):
            if j != 255:
                s.up_down_pen()
                s.moure_eix_secundari(1)
            else:
                s.moure_eix_secundari(1)
    s.moure_eix_principal(1)
    i=i+1
for i in img:
    s.moure_eix_principal(0)
print ("finish")
