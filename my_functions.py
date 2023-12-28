from PIL import Image 
import numpy as np
import random

# this function receives a string filename
# and returns a 2D array of pixel values
def load_file(orig):
    im = Image.open(orig)
    mat = np.array(im)
    return mat

# this function receives a 2D list of pixels and string filename
# and saves the file as an image
def save_file(mat, filename):
    result = Image.fromarray(mat, 'RGB')
    result.save(filename)

def block(origname, newname):
    mat = load_file(origname)
    # these variables will make your life easier
    height = len(mat)
    width = len(mat[0])
    for row in range(height//2, height):
        for col in range(0, width//2):
            mat[row][col] = (0,0,0)
    save_file(mat, newname)

# let's look at the rows and columns
# and how to change one pixel
def experiment(origname, newname):
    mat = load(origname)
    print(type(mat))
    print("\ntop row:\n", mat[0])
    print("\ntop row, first pixel:", mat[0][0])
    print("getting red from top row, first pixel:", mat[0][0][1])
    # TODO

# example 1
# this shows that we can access any pixel (and change it)
def speckle(origname, newname, num_times):
    mat = load_file(origname)
    # these variables will make your life easier
    height = len(mat)
    width = len(mat[0])
    # pseudocode:
    # loop a bunch of times
    # make a random color
    # pick a random row & column
    # set that pixel to the random color
    pass


# example 2
# this functions shows that we can access all pixels
# and alter the r,g,b of any pixel
# NOTE: also iterate half way
def convert_to_greyscale(origname, newname):
    # pseudocode:
    # loop through all rows and columns
    # get the r,g,b of each pixel
    # calculate the average
    # set the pixel to that value
    # example: (50, 100, 150) would become (100, 100, 100)
    pass


# example 3
# NOTE: also iterate cols / rows
def flip_across_vertical(origname, newname):
    # pseudocode:
    # loop through all rows, only HALF way across each column
    # swap the left and right pixels
    pass