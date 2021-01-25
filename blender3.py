# Import required modules
import cv2 as cv
import numpy as np
canvas_width = 512
canvas_height = 512
white = [255, 255, 255]
channels = 3
palette_title = "Palette"
canvas_title = "Canvas"
palette_colour = None
# Create a white canvas
# the np.full call creates an array filled with values Blue=255, Green=255, Red=255 (BGR White)
# for  colour of shape canvas_width by canvas_height and channels channels


def createCanvas(colour):
    canvas = np.ones(
        shape=(canvas_height, canvas_width, channels), dtype=np.uint8)
    canvas = canvas*np.uint8(colour)
    return canvas

# Display an image


def displayImage(image, title):
    cv.imshow(title, image)

# Mouse callback function


def mouseCallbackFunction(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        palette_colour = findColour(palette_title, x, y)

# Find the color for an image at the given location


def findColour(image, x: int, y: int):
    # Blue = image[y, x, 0]
    # Green = image[y, x, 1]
    # Red = image[y, x, 2]
    # return [Red, Green, Blue]
    colour = image[0, 0]
    return colour

# Mix two colors


def mixColors(colour1, colour2):
    new_colour = 0.4*colour1 + 0.4*colour2
    return [new_colour]


# Load the color palette
palette = cv.imread("colour-wheel.jpg")
# create the canvas
canvas = createCanvas(white)

cv.namedWindow(palette_title)
cv.namedWindow(canvas_title)

cv.setMouseCallback(palette_title, mouseCallbackFunction)
while(True):
    # display the canvas
    displayImage(palette, palette_title)
    displayImage(canvas, canvas_title)
    if palette_colour is not None:
        canvas_colour = findColour(canvas, 0, 0)
        mixed_colour = mixColors(canvas_colour, palette_colour)
        canvas = createCanvas(mixed_colour)
        displayImage(canvas, canvas_title)
        palette_colour = None
        if cv.waitKey(0) & 0xFF == 27:
            break
cv.destroyAllWindows()
