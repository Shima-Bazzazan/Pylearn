import cv2
import numpy as np

image_room = cv2.imread("input/room.jpg")
image_floor = cv2.imread("input/floor.jpg")
image_room_mask = cv2.imread("input/room_mask.jpg")

image_new_room_mask = 255 - image_room_mask

image_room_mask = image_room_mask / 255.0
image_new_room_mask = image_new_room_mask / 255.0

result_1 = image_floor * image_room_mask
result_2 = image_room * image_new_room_mask
result = result_1 + result_2

cv2.imwrite("output/room.jpg", result)