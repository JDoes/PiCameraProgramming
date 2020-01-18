from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(640, 480), framerate=10)
camera.iso = 400

camera.rotation = 180
camera.start_preview(alpha=255)

sleep(3)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode= 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

camera.capture_sequence(['/home/pi/Desktop/TimelapseTrials/image3%02d.jpg' % i for i in range(10)])
 
camera.stop_preview()
