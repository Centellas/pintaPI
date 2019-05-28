import RPi.GPIO as GPIO
import time
#import cv2
#from matplotlib import pyplot as plt
#plt.rcParams['image.cmap']='gray'

def up_down_pen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    p=GPIO.PWM(17,50) #PWM with 50Hz
    p.start(7.5)

    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)

    p.stop()
    GPIO.cleanup()

def moure_eix_principal(direccio):
    GPIO.setmode(GPIO.BOARD)

    pinDir = 36
    pinStep = 32
    numStep = 5
    microPausa = 0.0075

    GPIO.setup(pinDir, GPIO.OUT)
    GPIO.setup(pinStep,GPIO.OUT)

    GPIO.output(pinDir,direccio)
    for x in range(0, numStep):
        GPIO.output(pinStep,True)
        time.sleep(microPausa)
        GPIO.output(pinStep,False)
        time.sleep(microPausa)

    time.sleep(microPausa)
    GPIO.cleanup()

def moure_eix_secundari(direccio):
    GPIO.setmode(GPIO.BOARD)

    pinDir2 = 37
    pinStep2 = 35
    numStep = 5
    microPausa = 0.0075

    GPIO.setup(pinDir2, GPIO.OUT)
    GPIO.setup(pinStep2,GPIO.OUT)

    GPIO.output(pinDir2,direccio)
    for x in range(0, numStep):
        GPIO.output(pinStep2,True)
        time.sleep(microPausa)
        GPIO.output(pinStep2,False)
        time.sleep(microPausa)

    time.sleep(microPausa)
    GPIO.cleanup()



"""

img = [[255,0,255,0,255,0],[0,255,0,255,0,255],[255,0,255,0,255,0],[255,0,255,0,255,0],[0,255,0,255,0,255],[255,0,255,0,255,0]]
for i in range(6):
    for j in range(6):
        if img[i][j] != 255:
        up_down_pen()
        print ("llapis")
            moure_eix_secundari(0)
            print ("moure eix secundari")
        else:
            moure_eix_secundari(0)
            print ("moure eix secundari")
    print ("moure al inici eix secundari")
    for j in range(5):
        moure_eix_secundari(1)
    moure_eix_principal(1)
    print ("moure eix principal")
print ("moure al inici eix principal")
for j in range(5):
    moure_eix_principal(0)

print ("finish")

"""
