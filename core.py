# Core functions for image processing

# Add to function names when implementing new functions:

from runenv import saved_vars, saved_macros, env_vars
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
    saved_vars.add_var(id, img, filename)
    # cv2.imshow('hi', saved_vars.get_var(id))


def reload(id):
    # print(saved_vars.get_path(id))
    openfile(saved_vars.get_path(id), id)


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
    saved_vars.add_var(id, scaled, saved_vars.get_path(id))
    return


def blur(id, value):

    img = saved_vars.get_var(id)
    blurred = cv2.blur(img, (value, value))
    saved_vars.add_var(id, blurred, saved_vars.get_path(id))


def grayscale(id):

    # print("Grayscale function called. Parameters: {}".format(id))

    img = saved_vars.get_var(id)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saved_vars.add_var(id, gray_image, saved_vars.get_path(id))
    return


def erode(id, value):
    # print("Eroding function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.erode(img, kernel, iterations=1)
    saved_vars.add_var(id, eroded, saved_vars.get_path(id))
    return


def dilate(id, value):
    # print("Dilating function called. Parameters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
    img = saved_vars.get_var(id)
    eroded = cv2.dilate(img, kernel, iterations=1)
    saved_vars.add_var(id, eroded, saved_vars.get_path(id))
    return


def outline(id, value):
    # print("Outline function called. Paramters: {}, {}".format(id, value))
    kernel = np.ones((value, value), np.uint8)
    img = saved_vars.get_var(id)
    morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    saved_vars.add_var(id, morph_gradient, saved_vars.get_path(id))
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
    saved_vars.add_var(id, res, saved_vars.get_path(id))
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
    saved_vars.add_var(id, crop_img, saved_vars.get_path(id))
    return

# impose will overlay a new photo on top of an existing image
# requires image id, pixel values for x and y placement based
# off of top left corner of imposed image


def impose(id, overlay, px, py):
    img = saved_vars.get_var(id)
    other_image = saved_vars.get_var(overlay)

    # Mask ranges from 0 to width / height of overlay
    mask = np.zeros(img.shape, dtype=np.bool)
    mask[:other_image.shape[0], :other_image.shape[1]] = True

    locs = np.where(mask != 0)  # Get the non-zero mask locations

    # Following conditional logic is equivalent to copyTo from other languages
    # TODO implement overflow logic to cutoff instead of wrap

    # Background is colored but overlay is grayscale
    if len(img.shape) == 3 and len(other_image.shape) != 3:
        img[locs[0] + px, locs[1] + py] = other_image[locs[0], locs[1], None]
    # Both overlay and background are grayscale
    elif (len(img.shape) == 3 and len(other_image.shape) == 3) or \
            (len(img.shape) == 1 and len(other_image.shape) == 1):
        img[locs[0] + px, locs[1] + py] = other_image[locs[0], locs[1]]
    # Otherwise, we can't do this
    else:
        raise hiphop_error("InvalidFunctionError",
                           "Incompatible input and output dimensions.")
    saved_vars.add_var(id, img, saved_vars.get_path(id))
    return

# wave applies a sine wave to the image in either horizontal,
# vertical, or multirdirectional ways


def wave(id, direction, amplitude):
    img = saved_vars.get_var(id)
    img_output = np.zeros(img.shape, dtype=img.dtype)
    rows, cols, mask = img.shape
    if direction == "v":
        # print("Dir v")
        for i in range(rows):
            for j in range(cols):
                offset_x = int(int(amplitude) * np.sin(2 * 3.14 * i / 180))
                offset_y = 0
                if j+offset_x < rows:
                    img_output[i, j] = img[i, (j+offset_x) % cols]
                else:
                    img_output[i, j] = 0
    elif direction == "h":
        # print("Dir h")
        for i in range(rows):
            for j in range(cols):
                offset_x = 0
                offset_y = int(int(amplitude) * np.sin(2 * 3.14 * j / 150))
                if i+offset_y < rows:
                    img_output[i, j] = img[(i+offset_y) % rows, j]
                else:
                    img_output[i, j] = 0

    elif direction == "m":
        for i in range(rows):
            for j in range(cols):
                offset_x = int(int(amplitude) * np.sin(2 * 3.14 * i / 150))
                offset_y = int(int(amplitude) * np.cos(2 * 3.14 * j / 150))
                if i+offset_y < rows and j+offset_x < cols:
                    img_output[i, j] = img[(i+offset_y) %
                                           rows, (j+offset_x) % cols]
                else:
                    img_output[i, j] = 0
    else:
        raise hiphop_error("InvalidFunctionError",
                           "Invalid parameters.")
    saved_vars.add_var(id, img_output, saved_vars.get_path(id))
    return
