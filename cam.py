import picamera
from PIL import Image

import p3picam
import RPi.GPIO as GPIO
import os
import time
switch = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN,GPIO.PUD_DOWN)
import pytesseract
            
'''def _capture():
            print ("starting")
            os.system("espeak starting")
            with picamera.PiCamera() as camera:
                camera.resolution = (1280,720)
                camera.capture("/home/pi/Desktop/exp/image.jpg")

            print ("picture taken")
            os.system('espeak "picture taken"')
            im = Image.open("/home/pi/Desktop/trail/image.jpg")
            text = pytesseract.image_to_string(im, lang ='eng')
            os.system("tesseract /home/pi/Desktop/exp/image.jpg text")
            os.system("espeak < text")
            print (text)
            return'''

def begin():
    
    is_moving = p3picam.motion()
    while is_moving == True:
        os.system('espeak "hold still" ')
        print ("holdstill")
        is_moving = p3picam.motion()
    print ("starting")
    os.system('espeak "starting"')
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture("/home/pi/Desktop/final_version/image.jpeg")
        print ("picture taken")
        os.system('espeak "picture taken"')
        im = Image.open("/home/pi/Desktop/final_version/image.jpeg")
        text = pytesseract.image_to_string(im, lang ='eng')
        t = open("/home/pi/Desktop/final_version/txt.txt","w")
        t.write("{}".format(text))
        t.close()
        print("{}".format(text))
        os.system('espeak -s 110 < /home/pi/Desktop/final_version/txt.txt')
    return True



    
        
    
