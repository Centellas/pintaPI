import numpy as np
import cv2 as cv
#from matplotlib import pyplot as plt
from picamera import PiCamera



def selectroifromcorners(xs): ## get best corners a partir de la roi

    goodvalues =[]
    sorted1 = np.sort(xs, axis = 0)
    
    goodvalues.append(sorted1[0])
    goodvalues.append(sorted1[-1])
   
    corners = np.int0(goodvalues)
    x1,y1 = corners[0].ravel()
    x2,y2 = corners[1].ravel()

    return x1,y1,x2,y2


def findroi(img): ### dibuixa roi i crida a detection corners. (shi tomasi!!!)

    corners = cv.goodFeaturesToTrack(img,25,0.01,10) ## call to shi tomasi to find 25 best corners
    corners = np.int0(corners)
    x1,y1,x2,y2= selectroifromcorners(corners)
    img = cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

    img = img[y1:y2, x1:x2]


    return img

def colorquantization(img): # color cuantization, redueix la imatge a 4 colors

    height, width = img.shape[:2]   
    print (width)
    print (height)  
    ## traduir a 4 colors tots els pixels
    for i in range(width): 
        for j in range(height):
            tmp = img[j][i]
            tmp = (tmp // 64) * 85 
            img[j][i] = tmp

    return img


def esborde(i,j, img): # determina si un pixel es borde mirant els veïns
    tmp = img[j][i]
    try:
        if (tmp != img[j-1][i] or tmp != img[j][i-1] or tmp != img[j+1][i] or tmp != img[j][i+1]):
            return True
        else:
            return False
    except:
        return True



def puntillismo(img): ## generacio de puntillismo, si es borde, pinta de color negre. si no, pinta blanc

    #
    #   input       output
    #   0-63        0
    #   64-127      85
    #   128-191     170
    #   192-255     255
    #
    height, width = img.shape[:2]
    old_0 = "White"
    old_1 = "White"
    imorg = np.array(img, copy=True)  
    for j in range(height):
        for i in range(width):

            tmp = img[j][i]

            if esborde(i, j,imorg): ## pintar si es borde de color negre
                img[j][i] = 0
            else:
                img[j][i] = 255 ## pintar blanc si no es borde
    return img
                    



def transform(): ## funcio main principal, amb tots els canvis de color necesaris
    #camera = PiCamera()
    #camera.start_preview()
    #sleep(5)
    #camera.capture('/home/pi/Desktop/LENO.jpg')
    #camera.stop_preview()
    
    image = cv.imread('lena.jpeg') ## llegeix una imatge si no es fa servir la picam
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # conversio a escala de grisos

    cv.imshow('Original image',image)

    roi = findroi(gray) # detecta roi

    cv.imshow('Roi', roi)

    gray_cuantized=colorquantization(roi) # Cuantitzacio de colors 

    cv.imshow('Roi Quantized', gray_cuantized) 


    puntimg = puntillismo(gray_cuantized) ## pasa cuantitzacio a puntillisme
    cv.imshow('puntillismo', puntimg)
    #fichero = open('lena.txt', 'w')
    #fichero.write(str(puntimg.shape[:2] ))
    #fichero.write('\n')
    #fichero.write('[')
    #for line in puntimg:
    #    fichero.write( str(line))
    #    fichero.write('\n')
    #fichero.write(']')
    #fichero.close()
    print(puntimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return puntimg ## retorna

