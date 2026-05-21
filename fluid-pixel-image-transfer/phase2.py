"""
Phase 2 of the Project takes the 2 given images and reshapes them into
a Column/Row of 200*200=40000 pixels each. Then it finds optimal pixel
assignment between them based on RGB color similarity and then rearranges
image B's pixels into image A's layout.

"""
from phase1 import load_image
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
from PIL import Image as PILImage

# Wrapped into a function so phase3 can call it directly
def compute_transport(img_a, img_b):
    # Flatten into a flat list 40000, 3 to compare colors
    # -1 means numpy figures out row count automatically
    pixels_a = img_a.reshape(-1 , 3)
    pixels_b = img_b.reshape(-1, 3)

    print("Pixels A shape: ", pixels_a.shape)
    print("Pixels B shape: ", pixels_b.shape)

    # Convert to floating point 32 so decimal values aren't lost
    pixels_a = pixels_a.astype(np.float32)
    pixels_b = pixels_b.astype(np.float32)

    # Compares every pixel in A to every pixel in B to find
    # optimal pixel placement
    cost_matrix = cdist(pixels_a, pixels_b, metric='euclidean')
    print("Cost matrix shape: ", cost_matrix.shape)

    # Finds the most optimized set of matches
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    print("row_ind shape: ", row_ind.shape)
    print("col_ind shape: ", col_ind.shape)

    # col_ind tells which pixel goes where
    # pixels_b[col_ind] fetches the pixels in the assigned order
    matched_pixels = pixels_b[col_ind]
    print("Matched pixels shape: ", matched_pixels.shape)

    return col_ind, pixels_b
