# Import required modules
import cv2 as cv
import numpy as np
canvas_width = 512
canvas_height = 512
white = 255
channels = 3
# Create a white canvas
# the np.full call creates an array filled with values Blue=255, Green=255, Red=255 (BGR White)
# for  colour of shape canvas_width by canvas_height and channels channels
# 
def createCanvas():
    canvas = np.full(shape=(canvas_height,canvas_width,channels), fill_value=white, dtype=np.uint8)
    return canvas

# Display an image
def displayImage(image, title):
    cv.imshow(title,image)

# Load the color palette
palette = cv.imread("colour-wheel.jpg")

#create the canvas
canvas = createCanvas()

#display the canvas
displayImage(canvas,"Canvas")
key = cv.waitKey(0) # or it vanishes!

#display the colour  palette # or it vanishes!
displayImage(palette,"Palette")
key = cv.waitKey(0)
