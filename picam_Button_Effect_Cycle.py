#From: picamera.readthedocs.io/en/release-1.13/recipes1.html
#Another good site for this is:
# projects.raspberrypi.org/en/projects/getting-started-with-picamera/8

#Author: Gordon Bates
#Date: Started around Jan 2020

#This is an intervalometer camera, designed to use a GPOI button
# as the start/stop. Work in progress.


import time
from time import sleep
import datetime
import picamera
from picamera import PiCamera, Color
from gpiozero import Button
import os

# Button on breadboard, or hooked directly to GPIO pins
# Camera connected through ribbon cable. Have not tried a USB webcam yet.
# Apparently, will not work, picamera library relies on lidmmal, which
# is specifically made for the Pi's amera module. 5.7 in FAQ
button = Button(17)
camera = PiCamera()

# Improvement idea: make a popup that asks for resolution,
# or gives options for res to choose from.
camera.resolution = (1024,768)

# Improvement ides:
# 1) Make selecatable or adjustable image rotation.
# 2) Put the rotation selection on a rotary encoder,
#    or make button presses cycle through rotations
camera.rotation = 180

# Show preview, with slight transparency (range 0-255)
camera.start_preview(alpha=175)

 # I thought color of text is foreground, but nope.
# For a background color, do _background
camera.annotate_background = Color('red')

# Size of text, ange of 6 to 160
camera.annotate_text_size = 40

# Display text on image
# I want a GUI, so I can have the text typed in.
# How do I do
# image_text = input("Enter the text that you want printed on the picture")
# camera.annotate_text = ' image_text '

# Text annotation on the image
#camera.annotate_text = ' Text goes here!!!   :) '

# Image effects: negative, solarize, *sketch, denoise, *emboss, oilpaint, hatch
# gpen, *pastel, *watercolor, film, blur, saturation, colorswap, washedout,
# *posterise, colorpoint, colorbalance, *cartoon, deinterlace1, deinterlace2
# Default effect is none
#camera.image_effect = 'emboss'



# Improvement idea: as per 'the guy' at Installfest- make it see if there is
# the current dates folder. If so, append to that folder, if not,
# create the date folder and start adding to it.
# Currently, I have it start a new folder each time the program runs,
# with date and time, so there are not folder overwrites.
dayFolder = time.strftime("%Y-%m-%d_%H:%M:%S")
directory = "/home/pi/Desktop/images/" + dayFolder + "/"
os.mkdir(directory)

button.wait_for_press()
sleep(1)

# Make sure to hold the button for >= the amount of time specified in the
# lower sleep line, so it interrupts the while loop.
#while not button.is_pressed:

# Improvement: have a menu or popup, where you can select custom
# file naming, and even the location, possibly.
    # This ensures unique file names, so there are not unintentional
    # file overwrites.
    #date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(2)

    date_string = time.strftime("%H:%M:%S")
    full_name = directory + date_string + "_PiCam_image.jpg"
    camera.capture(full_name)

    #prints filename to Python Console, to confirm the program is operating
    print(full_name)


camera.stop_preview()

# Overall, this program could use more interactivity, like rotor encoders,
# and/or a GUI with text entry fields, and/or dropdown menus.
