from PIL import Image 
import numpy as np
import random

# this function receives a string filename
# and returns a 2D array of pixel values
def load_file(orig):
def load_file(orig):
    im = Image.open(orig)
    # im.show() # try this (here or other places)!
    mat = np.array(im)
    return mat

# this function receives a 2D list of pixels and string filename
# and saves the file as an image
def save_file(mat, filename):
    result = Image.fromarray(mat, 'RGB')
    result.save(filename)




# let's look at the rows and columns
# and how to change one pixel
def experiment(origname, newname):
    mat = load_file(origname)
    print(type(mat))
    height = len(mat)
    width = len(mat[0])
    print("\nheight is ", height)
    print("width is ", width)

    print("\ntop row:\n", mat[0])
    print("\ntop row, first pixel:", mat[0][0])
    print("getting red from top row, first pixel:", mat[0][0][0])
    

    mat[0][0] = (0,0,0) # set one pixel to black
    print("\n", mat[0])
    save_file(mat, newname)



# example: iterating through a section of pixels
def block(origname, newname):
    mat = load_file(origname)
    # these variables will make your life easier
    height = len(mat)
    width = len(mat[0])
    for row in range(height//2, height):
        for col in range(0, width//2):
            mat[row][col] = (0,0,0)
    save_file(mat, newname)




# this shows that we can access any pixel (and change it)
def speckle(origname, newname, num_times):
    pass



# this functions shows that we can access all pixels
# and alter the r,g,b of the pixels
def convert_to_greyscale(origname, newname):
    pass



# remember to iterate through *all* rows and *half* of the columns
def flip_across_vertical(origname, newname):
    pass