import picamera
from PIL import Image
import p3picam
import os
import signal
import RPi.GPIO as GPIO
import time
import multiprocessing
import pytesseract
switch = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)
#GPIO.setup(4, GPIO.IN,GPIO.PUD_DOWN)
sflag = False
#count = 0
#run_once = 1
def begin():
    global infunc
    infunc = True
    is_moving = p3picam.motion()
    while is_moving == True:
        os.system('espeak "hold still" ')
        print ("holdstill")
        is_moving = p3picam.motion()
    print ("starting")
    os.system('espeak "ready"')
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture("/home/pi/Desktop/final_version/image.jpeg")
        print ("captured")
        os.system('espeak "image captured"')
        im = Image.open("/home/pi/Desktop/final_version/image.jpeg")
        text = pytesseract.image_to_string(im, lang ='eng')
        t = open("/home/pi/Desktop/final_version/txt.txt","w")
        t.write(text)
        t.close()
        os.system('espeak -ven-us+f4 -s 170 < /home/pi/Desktop/final_version/txt.txt')
        return False

'''proc1 = multiprocessing.Process(target =begin)
q = multiprocessing.Queue()
def a():
    global sflag,run_once
    if run_once == 1:
        sflag = True
       run_once = 0'''
infunc= False
def mi(channel):
        global sflag,infunc
        if sflag == False and not infunc:
            sflag = True
            
def breaker(channel):
    if proc1.is_alive():
       proc1.terminate()

#GPIO.add_event_detect(4, GPIO.RISING, callback = breaker, bouncetime = 300)
GPIO.add_event_detect(18, GPIO.RISING, callback = mi, bouncetime = 300)
while True:
    '''if count == 1 :
       count = 0
       if not proc1.is_alive():
            proc1.start()
            proc1.join()
            if not q.empty():
             sflag= q.get()
            print(sflag)
    else:
        pass'''
    if sflag == True and not infunc:
            infunc = begin()
            sflag = False

