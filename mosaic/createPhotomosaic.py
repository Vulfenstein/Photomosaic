from getAverageRGB import getAverageRGB
from splitImage import splitImage
from getBestMatchIndex import getBestMatchIndex
from createImageGrid import createImageGrid
# Creates a photomosaic given target and input images

def createPhotomosaic(target_image, input_images, grid_size, reuse_images=True):  

    # split target image into tiles
    print('splitting input image...')
    target_images = splitImage(target_image, grid_size)

    print('finding image matches...')
    # for each tile pick matching input image
    output_images = []
    count = 0
    batch_size = int(len(target_images)/10)

    # calculate average for input image
    avgs = []
    for img in input_images:
        avgs.append(getAverageRGB(img))

    for img in target_images:
        # find average RGB value
        avg = getAverageRGB(img)
        # find closest match
        match_index = getBestMatchIndex(avg, avgs)
        output_images.append(input_images[match_index])
        # user feedback
        if count > 0 and batch_size > 10 and count % batch_size == 0:
            print('processing %d of %d...' % (count, len(target_images)))
        count += 1
        if not reuse_images:
            input_images.remove(match)
    print('creating mosaic...')
    mosaic_image = createImageGrid(output_images, grid_size)

    return mosaic_image