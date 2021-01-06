import numpy as np
# Return the average color value as (r,g,b) for each input image #
    
def getAverageRGB(image):

    # get each tile image as a numpy array #
    im = np.array(image)

    # get shape of each input image #
    w,h,d = im.shape

    # get average RGB value #
    return tuple(np.average(im.reshape(w*h, d), axis=0))
