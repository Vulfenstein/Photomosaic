import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np
# Return index of the best image match, based on average RGB value distances #

def getBestMatchIndex(input_avg, avgs):

    avg = input_avg

    # Get closest RGB value to input, based on RGB distance #
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0])*(val[0] - avg[0]) +
                (val[1] - avg[1])*(val[1] - avg[1]) +
                (val[2] - avg[2])*(val[2] - avg[2]))
        if dist < min_dist:
            min_dist = dist
            min_index = index 
        index += 1
    return min_index