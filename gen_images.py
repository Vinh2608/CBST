import cv2
import numpy as np

# Define the image and mask dimensions
height, width = 760, 1280


for i in range(5):
    # Generate a random grayscale image
    img = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    cv2.imwrite(f'issegm/dataset/synthia/Image/images_{i}.png', img)

    # # Generate a random grayscale mask
    mask = np.random.randint(0, 256, (height, width), dtype=np.uint8)
    cv2.imwrite(f'issegm/dataset/synthia/Mask/labels_{i}.png', mask)