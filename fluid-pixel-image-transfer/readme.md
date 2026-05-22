# Pixel Transport

Inspired by [this video](https://www.youtube.com/shorts/MeFi68a2pP8), where an algorithm 
rearranges any image's pixels into the shape of Obama using optimal transport and a fluid 
dynamics simulation, this project does the same thing but between any two images of your choice.

## What It Does

Takes two images. Uses the mathematics of optimal transport to find the most color-efficient 
way to rearrange every pixel from image A into the layout of image B, then animates that 
rearrangement so you can watch it happen in real time.

## How It Works

The project was built in 4 phases:

**Phase 1 - Image Loading**  
Both images are loaded, converted to RGB, resized to the same dimensions, and flattened 
into pixel arrays for processing.

**Phase 2 - Optimal Transport**  
A cost matrix is built by calculating the color distance between every pixel in image A 
and every pixel in image B. `linear_sum_assignment` solves the assignment problem, finding 
the globally optimal 1-to-1 pixel matching that minimizes total color distance across all pixels.

**Phase 3 - Animation**  
Each pixel's journey from its start position to its assigned end position is animated using 
linear interpolation with smoothstep easing, producing a GIF of the pixels flowing into 
their new arrangement.

**Phase 4 - Optimization**  
KDTree approximate nearest neighbor matching was tested as a faster alternative but was 
dropped. It allowed pixel collisions that left gaps and produced poor results on images 
with different color distributions. Phase 4 keeps `linear_sum_assignment` for reliable 
1-to-1 assignment, increases resolution to 100x100, removes the phase2 dependency, 
and switches to imageio for cleaner GIF output.

## Requirements

```bash
pip install numpy scipy pillow matplotlib opencv-python imageio
```

## Usage

Place your two images in the project folder as `image_a.jpg` and `image_b.jpg`, then run:

```bash
python phase4.py
```

`image_a.jpg` is the color source, its pixels are used to recreate `image_b.jpg`.

## Example

Spheal's pixels rearranged into Meguru Bachira from Blue Lock:

![example](https://github.com/user-attachments/assets/30dd3378-3293-4448-9400-c8d12cf7a63d)

## What I Learned

This project introduced me to scipy's optimization tools, numpy array manipulation 
for image processing, and animation output with imageio. It also exposed me to 
optimal transport as a concept and the tradeoffs between exact and approximate 
algorithms when performance matters.
