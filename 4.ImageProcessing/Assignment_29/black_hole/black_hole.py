import os
import cv2
import numpy as np

def noise_reducer(images_folder):
    images_path = os.listdir(images_folder)
    images = []
    for image_path in images_path:
        image = cv2.imread(images_folder + "/" + image_path)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)
    for image in images:
        result += image

    result = result / len(images)
    result = result.astype(np.uint8)
    return result
