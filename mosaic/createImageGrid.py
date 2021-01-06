import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np
# Given a list of images and a grid size(m,n) create a grid of images

def createImageGrid(images, dims):

    m, n = dims

    #sanity check
    assert m*n == len(images)

    #get maximum height and width of the images
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    #create target image
    grid_img = Image.new('RGB', (n*width, m*height))

    #paste the tile images into the image grid
    for index in range(len(images)):
        row = int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))
    return grid_img