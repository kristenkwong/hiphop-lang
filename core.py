# Core functions for image processing

# Add to function names when implementing new functions:
func_names = ["blur", "blackandwhite"]

from runenv import saved_vars, saved_macros
import cv2

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

def blur(id, value):

    img = saved_vars.get_var(id)
    blurred = cv2.blur(img, (value, value))
    saved_vars.add_var(id, blurred)

def blackandwhite(id):

    print("Grayscale function called. Parameters: {}".format(id))

    img = saved_vars.get_var(id)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saved_vars.add_var(id, gray_image)
