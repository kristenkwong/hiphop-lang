# Core functions for image processing

# Add to function names when implementing new functions:

from runenv import saved_vars, saved_macros
import cv2
import numpy as np
import os
from hiphoperrors import hiphop_error, file_error
from termcolor import colored
import colorama

###### FILE OPERATIONS ######


def openfile(filename, id):

    # print("Open file function called. Parameters: {}, {}".format(filename, id))
    img = cv2.imread(filename)
    if (img is None):
        raise hiphop_error("OpenImageError", "Filename does not exist.")
    saved_vars.add_var(id, img)
    # cv2.imshow('hi', saved_vars.get_var(id))


def savefile(id, filename):

    # print("Save file function. Parameters: {}, {}".format(id, filename))

    if (filename.startswith('../')):
        # should throw error here
        raise file_error(
            "SaveError", "Cannot save file, filename should not start with ../")

    new_filename = filename

    # id filename just start with /
    if (filename.startswith('/')):
        new_filename = "." + filename

    # if filename does not start with ./
    if not (new_filename.startswith('./')):
        new_filename = "./" + filename

    head_tail = os.path.split(new_filename)

    if not (os.path.exists(head_tail[0])):
        os.makedirs(head_tail[0])

    cv2.imwrite(new_filename, saved_vars.get_var(id))

    print(colored("Image at id {} successfully saved to {}".format(id, filename), "green"))


###### IMAGE OPERATIONS ######
def scale(id, x, y):
    img = saved_vars.get_var(id)
    width = int(img.shape[1] * x)
    height = int(img.shape[0] * y)
    dim = (width, height)
    scaled = cv2.resize(img, dim)
    saved_vars.add_var(id, scaled)
    return


def blur(id, value):

    img = saved_vars.get_var(id)
    blurred = cv2.blur(img, (value, value))
    saved_vars.add_var(id, blurred)


def grayscale(id):

    # print("Grayscale function called. Parameters: {}".format(id))

    img = saved_vars.get_var(id)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saved_vars.add_var(id, gray_image)
    return


def erode(id, value):
    # print("Eroding function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.erode(img, kernel, iterations=1)
    saved_vars.add_var(id, eroded)
    return


def dilate(id, value):
    # print("Dilating function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.dilate(img, kernel, iterations=1)
    saved_vars.add_var(id, eroded)
    return


def outline(id, value):
    # print("Outline function called. Paramters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
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
    res = cv2.bitwise_and(img, img, mask=mask)
    saved_vars.add_var(id, res)
    return

# crop would crop id with specified range
# where the range of image is [-1, 1] for width and height with 0 at center
# for example a image with width 200 and height 100
# widthlow = -0.5 widthhigh = 0.5 heightlow = -0.5 heighthigh = 0.5
# would return a new image with pixels width ranged [50, 150] and height ranged [25, 75] of original image


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

# impose will overlay a new photo on top of an existing opened image
# the method will need opacity and x y values as args


def impose(id, overlay):
    img = saved_vars.get_var(id)
    other_image = saved_vars.get_var(overlay)
    # print(img.shape)
    # print(img2.shape)

    # Define mask
    mask = np.zeros(img.shape, dtype=np.bool)
    mask[:other_image.shape[0], :other_image.shape[1]] = True

    locs = np.where(mask != 0)  # Get the non-zero mask locations

    # Case #1 - Other image is grayscale and source image is colour
    if len(img.shape) == 3 and len(other_image.shape) != 3:
        img[locs[0], locs[1]] = other_image[locs[0], locs[1], None]
    # Case #2 - Both images are colour or grayscale
    elif (len(img.shape) == 3 and len(other_image.shape) == 3) or \
            (len(img.shape) == 1 and len(other_image.shape) == 1):
        img[locs[0], locs[1]] = other_image[locs[0], locs[1]]
    # Otherwise, we can't do this
    else:
        raise Exception("Incompatible input and output dimensions")
    return
