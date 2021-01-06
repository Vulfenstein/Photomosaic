
# Split target image into an MxN grid 

def splitImage(image, size):

    W, H = image.size[0], image.size[1]
    m, n = size
    w, h = int(W/n), int(H/m)

    imgs = []
    for j in range(m):
        for i in range(n):
            # append cropped image 
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs