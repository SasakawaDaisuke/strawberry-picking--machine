from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution= (640,480)

camera.start_preview(fullscreen=False, window=(-100, 50, 640, 360))
sleep(2)
camera.stop_preview()