import glob
import os
import numpy as np
from PIL import Image
import cv2

images = glob.glob('./images/*.tif')

print("Found "+str(len(images))+" images to darken.")

for imageName in images:

	print(imageName)

	data = cv2.imread(imageName)

	image = Image.fromarray(data//4)

	name = "./darkened_images/"+imageName.split('.')[1].split("\\")[-1]+'.jpg'

	image.save(name)

print("Done.")