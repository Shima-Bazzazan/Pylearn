import os
import imageio

file_list =sorted(os.listdir("sessions/session8/image"))
IMAGES=[]

for file_name in file_list:
    file_path="sessions/session8/image/" + file_name
    image= imageio.v2.imread (file_path)
    IMAGES.append(image)

imageio.mimsave("sessions/session8/output.gif", IMAGES)
