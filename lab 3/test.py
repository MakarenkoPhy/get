from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 1024)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('lab 3/calibrovka.jpg')