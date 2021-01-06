import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np
# Given a directory of images, return list of images #

def getImages(imageDir):

    files = os.listdir(imageDir)
    images = []

    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            # avoid resource crunch #
            fp = open(filePath, "rb")
            im = Image.open(fp)
            images.append(im)
            
            # force load image #
            im.load()
            fp.close()
        except:
            print("Invalid image: %s" % (filePath,))
    return images