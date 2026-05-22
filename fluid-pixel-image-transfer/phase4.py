"""
Changes from Phase3 to Phase4
A massive change in computation time was to switch to a KDTree which matches to the nearest
approximate neighbor, this didn't work because it allowed multiple pixels to go after the same
target pixel. For images with different colors, you get collisions and leave gaps with a very
ugly looking result.

So instead of using KDTrees, Phase4 keeps the linear_sum_assignment for 1-1 assignment and
increases resolution to 100x100 from 64x64
run from phase4 and removed the phase2 dependency
switched from PIL's frames[0].save() to imageio because GIF output was reliable
removed pixels_a_int for cleaner code
"""

from phase1 import load_image
import numpy as np
from PIL import Image as PILImage
import imageio
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist

img_a = load_image("image_a.jpg", size=(100, 100))
img_b = load_image("image_b.jpg", size=(100, 100))

pixels_a = img_a.reshape(-1, 3).astype(np.float32)
pixels_b = img_b.reshape(-1, 3).astype(np.float32)

cost_matrix = cdist(pixels_a, pixels_b, metric='euclidean')
_, col_ind = linear_sum_assignment(cost_matrix)

pixels_a_int = img_a.reshape(-1, 3)

size = 100
num_frames = 30

start_positions = np.array([[i // size, i % size] for i in range(size * size)], dtype=np.float32)
end_positions = np.array([[col_ind[i] // size, col_ind[i] % size] for i in range(size * size)], dtype=np.float32)

frames = []
for frame in range(num_frames):
    t = frame / (num_frames - 1)
    t = t * t * (3 - 2 * t)

    current_positions = (1 - t) * start_positions + t * end_positions
    frame_img = np.zeros((size, size, 3), dtype=np.uint8)

    for i, pos in enumerate(current_positions):
        row, col = int(pos[0]), int(pos[1])
        if 0 <= row < size and 0 <= col < size:
            r, g, b = pixels_a_int[i]
            frame_img[row, col] = [r, g, b]

    frames.append(PILImage.fromarray(frame_img))

for _ in range(20):
    frames.append(frames[-1])

frames_array = [np.array(f) for f in frames]
imageio.mimsave("phase4_result.gif", frames_array, duration=50, loop=0)
print("Saved to phase4_result.gif")
