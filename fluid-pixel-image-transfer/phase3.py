"""
Phase3 is the visual of the change, this exports the creation of the image,
in real time, in the form of a .gif format. It loads the images,
iterates over the sizes, converting to floats to it easier to accommodate decimals,
and then converting it all back into an unsigned 8bit integer, exporting
with a high frame duration for ample time to see the final image.
"""

from phase1 import load_image
from phase2 import compute_transport
import numpy as np
from PIL import Image as PILImage
import imageio

img_a = load_image("image_a.jpg", size=(100, 100))
img_b = load_image("image_b.jpg", size=(100, 100))

# Run optimal transport, get pixel assignment map and target pixels
col_ind, pixels_b = compute_transport(img_a, img_b)

size = 100
num_frames = 30

pixels_a = img_a.reshape(-1, 3).astype(np.float32)
pixels_b = pixels_b.astype(np.float32)
# Keep integer version of pixels_a for painting, float values cause issues with color
pixels_a_int = img_a.reshape(-1, 3)

# Convert flat pixel index into 2D grid coordinates (row, col) for each pixel
start_positions = np.array([[i // size, i % size] for i in range(size * size)], dtype=np.float32)
# End positions based on transport map - where each pixel needs to travel to
end_positions = np.array([[col_ind[i] // size, col_ind[i] % size] for i in range(size * size)], dtype=np.float32)

frames = []
for frame in range(num_frames):
    t = frame / (num_frames - 1)

    # Smoothstep easing - starts slow, speeds up, slows down at end
    t = t * t * (3 - 2 * t)

    current_positions = (1 - t) * start_positions + t * end_positions
    frame_img = np.zeros((size, size, 4), dtype=np.uint8)

    for i, pos in enumerate(current_positions):
        row, col = int(pos[0]), int(pos[1])

        if 0 <= row < size and 0 <= col < size:
            r, g, b = pixels_a_int[i]
            if r > 20 or g > 20 or b > 20:
                frame_img[row, col] = [r, g, b, 255]

    frames.append(PILImage.fromarray(frame_img))

# Duplicate last frame to create a hold at the end of the animation
for _ in range(20):
    frames.append(frames[-1])

frames_array = [np.array(f) for f in frames]
imageio.mimsave("phase3_result.gif",
                frames_array,
                duration=50,
                loop=0)
print("Saved to phase3_result.gif")
