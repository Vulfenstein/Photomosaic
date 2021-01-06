
from scipy.spatial import KDTree as kdtree
# Return index of the best image match, based on average RGB value distances #

def getBestMatchIndex(input_avg, tree):

    # traverse tree finding nearest neighbor
    res, index = tree.query(input_avg, k=1)
    
    return index
