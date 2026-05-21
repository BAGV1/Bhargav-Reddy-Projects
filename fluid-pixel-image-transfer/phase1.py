"""
Phase 1 of the Project simply takes 2 images as
image_a and image_b before sizing them to 200x200 pixels,
then printing them out as image_c side by side in an array.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib

# We use Agg because we're not utilizing a Tkinter backend
matplotlib.use('Agg')

def load_image(path, size=(100, 100)):
    """
    The function takes the path of the image and sets size to 200x200 pixels.
    Returns the resized image as an array for future use.
    """
    img = Image.open(path)
    img = img.convert("RGB")
    img = img.resize(size)

    return np.array(img)

img_a = load_image("image_a.jpg")
img_b = load_image("image_b.jpg")

print("Image A Shape: ", img_a.shape)
print("Image B Shape: ", img_b.shape)

fig, axes = plt.subplots(1, 2)

axes[0].imshow(img_a)
axes[0].set_title("Image A")

axes[1].imshow(img_b)
axes[1].set_title("Image B")

plt.savefig("image_c.jpg")
print("Saved to image_c.jpg")

