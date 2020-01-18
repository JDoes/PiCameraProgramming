# for help, use help(PiCamera)

from picamera import PiCamera, Color
from time import sleep
from time import time

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1600, 1200)
camera.framerate = 15


camera.start_preview(alpha=150)  ##alpha=50 , for example, does transparency


camera.image_effect = 'solarize'
camera.brightness = 60
#none negative solarize sketch denoise emboss oilpaint hatch gpen
#cartoon watercolor pastel
#and many more on
#projects.raspberrypi.org/en/projects/getting-started-with-picamera/8

# put red bar behind whatever text is there
#camera.annotate_background = Color('red')

#camera.annotate_foreground = Color('Green')


camera.annotate_text = "I like cats."
camera.annotate_text_size = 120 ## range is from 6 to 160
# camera.annotate_color = 'Green'

camera.brightness = 50 ## neutral is 50. range 0 to 100
for i in range(100):
#camera.annotate_text = "Brightness: %s" % i
# grade through range of brightness and
# display brightness value on screen
#camera.brightness = i
#sleep(0.1)


## camera.contrast = 0
##for i in range(100):
##    camera.annotate_text = "Contrast: %s" % i
##    camera.contrast = i
##    sleep(0.1)
## maybe the 0.1 is so that from 0 to 100 fits inside of 10 seconds.
## But also, maybe the 10 seconds has not yet come into effect,
## because that is later in the code.
    

#camera.start_recording('/home/pi/Desktop/videoeffects/video_brightness.h264')
camera.capture('/home/pi/Desktop/ZakkiePooPooChaCha.jpeg')
sleep(3) 
#for video, this takes video for n seconds

## camera.stop_recording()   
camera.stop_preview()
