import glob
import os
import numpy as np
from PIL import Image
import cv2
import glob

images = glob.glob('./images/*.tif')

if len(glob.glob('darkened_images/')) == 0:
	os.mkdir('darkened_images/')

print("Found "+str(len(images))+" images to darken.")

for imageName in images:

	print(imageName)

	data = cv2.imread(imageName)

	image = Image.fromarray(data//4)

	name = "./darkened_images/"+imageName.split('.')[1].split("\\")[-1]+'.jpg'

	image.save(name)

print("Done.")