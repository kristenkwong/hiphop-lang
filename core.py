# Core functions for image processing

from runenv import saved_vars
import numpy as np
import cv2
import numpy as np

###### FILE OPERATIONS ######

def openfile(filename, id):

    print("Open file function called. Parameters: {}, {}".format(filename, id))
    img = cv2.imread(filename)
    saved_vars.add_var(id, img)
    cv2.imshow('hi', saved_vars.get_var(id))

    return

def savefile(id, filename):

    #TODO: Fill in this function to save the image with the given id as the filename.

    print("Save file function. Parameters: {}, {}".format(id, filename))
    cv2.imwrite(filename, saved_vars.get_var(id))

    return


###### IMAGE OPERATIONS ######

def blur(id, value):

    #TODO: Apply the blur function to the image saved with id.
    img = saved_vars.get_var(id)
    blurred = cv2.blur(img, (value, value))
    saved_vars.add_var(id, blurred)
    # print("TODO: BLUR FUNCTION. Parameters: {}, {}".format(id, value))
    return

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
