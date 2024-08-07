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

image_parts = []
for i in range(4):
    result = noise_reducer("input/" + str(i+1))
    cv2.imwrite("output/" + str(i+1) + "/modified_" + str(i+1) + ".jpg", result)
    image_parts.append(result)

os.makedirs
image_top = np.concatenate((image_parts[0], image_parts[1]), axis=1)
image_bottom = np.concatenate((image_parts[2], image_parts[3]), axis=1)
image_black_hole = np.concatenate((image_top, image_bottom), axis=0)
image_black_hole = image_black_hole.astype(np.uint8)
cv2.imwrite("output/image_black_hole.jpg", image_black_hole)
