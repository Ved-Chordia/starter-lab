import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

# Define the size you want all images to be (or take from the first image)
standard_size = (640, 480)

for filename in filenames:
    img = Image.open(filename).convert("RGB")  # Open and convert to RGB
    img = img.resize(standard_size)            # Resize to standard size
    images.append(np.array(img))               # Convert to numpy array for imageio

iio.imwrite('team.gif', images, duration=500, loop=0)
