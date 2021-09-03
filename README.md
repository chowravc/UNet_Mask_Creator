# UNet Mask Creator
Pipeline to create UNet Masks for use with https://github.com/chowravc/UNet.git

1. Start by dumping images into the images folder.
2. Next run the imageProcess.py file to darken these images.
3. Now go into the darkened_images folder and open each individual image with an application like paint.
4. Use a paintbrush with the colour white to paint over 'masks' wherever you want the label value to be 1.
5. This paintbrush must be painting complete in white [255, 255, 255]. If any pixel has a value other than white, IT WILL BE 0 IN THE MASK.
6. Run the createMasks.py file and your label txt files should be generated. This is the required format for UNet.