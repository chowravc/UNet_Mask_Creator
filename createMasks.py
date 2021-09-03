import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import glob

if len(glob.glob('labels/')) == 0:
	os.mkdir('labels/')

if __name__ == '__main__':
	
	imPaths = glob.glob('darkened_images/*.jpg')

	for imPath in imPaths:

		print(imPath)

		imRay = cv2.imread(imPath)
		
		imRay = cv2.resize(imRay, dsize=(1892, 1892), interpolation=cv2.INTER_CUBIC)

		imRay = imRay[:,:,0] + imRay[:,:,1] + imRay[:,:,2]

		mask = (imRay >= 220)*1.0

		# plt.imshow(mask)
		# plt.colorbar()
		# plt.show()

		labelPath = imPath.replace('darkened_images', 'labels').replace('jpg', 'txt')

		np.savetxt(labelPath, mask)