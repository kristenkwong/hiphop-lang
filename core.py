# Core functions for image processing

# Add to function names when implementing new functions:
func_names = ["blur", "blackandwhite"]

from runenv import saved_vars, saved_macros
import cv2
import numpy as np

###### FILE OPERATIONS ######

def openfile(filename, id):

    print("Open file function called. Parameters: {}, {}".format(filename, id))
    img = cv2.imread(filename)
    saved_vars.add_var(id, img)
    cv2.imshow('hi', saved_vars.get_var(id))

def savefile(id, filename):

    #TODO: Fill in this function to save the image with the given id as the filename.

    print("Save file function. Parameters: {}, {}".format(id, filename))
    cv2.imwrite(filename, saved_vars.get_var(id))


###### IMAGE OPERATIONS ######
def scale(id, x, y):
    img = saved_vars.get_var(id)
    width = int(img.shape[1] * x)
    height = int(img.shape[0] * y)
    dim = (width,height)
    scaled = cv2.resize(img, dim)
    cv2.imshow("scaling", scaled)
    saved_vars.add_var(id, scaled)
    return

def blur(id, value):

    img = saved_vars.get_var(id)
    blurred = cv2.blur(img, (value, value))
    saved_vars.add_var(id, blurred)

def blackandwhite(id):

    print("Grayscale function called. Parameters: {}".format(id))

    img = saved_vars.get_var(id)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saved_vars.add_var(id, gray_image)
    return

def erode(id, value):
    print("Eroding function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value,value),np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.erode(img,kernel,iterations = 1)
    saved_vars.add_var(id, eroded)
    return

def dilate(id, value):
    print("Dilating function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value,value),np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.dilate(img,kernel,iterations = 1)
    saved_vars.add_var(id, eroded)
    return

def outline(id, value):
    print("Outline function called. Paramters: {}, {}".format(id, value))
    kernel = np.ones((value,value), np.uint8)
    img = saved_vars.get_var(id)
    morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    saved_vars.add_var(id, morph_gradient)
    return

def filtercolor(id, lowR, lowG, lowB, highR, highG, highB):

    img = saved_vars.get_var(id)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lower_range = np.array([lowB, lowG, lowR])
    upper_range = np.array([highB, highG, highR])

    # Threshold the HSV image to get only specified colors
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img ,img, mask=mask)
    saved_vars.add_var(id, res)
    return

# crop would crop id with specified range
# where the range of image is [-1, 1] fir width and height with 0 at center
# for example a image with width 200 and height 100
# widthlow = -0.5 widthhigh = 0.5 heightlow = -0.5 heighthigh = 0.5
# would return a new image with pixels ranged [50, 150] for width and [25, 75] for height 
def crop(id, widthlow, widthhigh, heightlow, heighthigh):

    img = saved_vars.get_var(id)
    height, width, channels = img.shape

    heighthalf = height/2
    widthhalf = width/2
    hl = round(heighthalf + heightlow * heighthalf)
    hh = round(heighthalf + heighthigh * heighthalf)
    wl = round(widthhalf + widthlow * widthhalf)
    wh = round(widthhalf + widthhigh * widthhalf)

    crop_img = img[hl:hh, wl:wh]
    saved_vars.add_var(id, crop_img)
    return