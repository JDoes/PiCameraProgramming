from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview(alpha=60)
camera.start_recording('/home/pi/Desktop/python_video/video.h264')
sleep(10)
camera.stop_recording()   
camera.stop_preview()
