import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def extractHair():
    # For Extracting Hair Segment class as an image from the Segmentation Mask
    # Read the segmentation mask image
    im = cv.imread('files\initialSegmentation.jpg')

    ims = im.copy()

    # Iterate through all rows of image matrix
    for i in range(1,im.shape[0]):
        # Iterate through all columns of image matrix
        for j in range(1,im.shape[1]):
            # Checks whether pixel belongs to Hair class and represents it as white (255) else black (0)
            if im[i,j,1] == 17:
                ims[i,j,0] = 255
                ims[i,j,1] = 255
                ims[i,j,2] = 255
            else:
                ims[i,j,0] = 0
                ims[i,j,1] = 0
                ims[i,j,2] = 0
    
    cv.imwrite('files/binoutput.jpg', ims, [int(cv.IMWRITE_JPEG_QUALITY), 100])
    

    # Use Hair segmentation image for Extracting RGB Hair image from the original image
    # Read the original image 
    imo = cv.imread('files\input.jpg')

    # Resize Segmentation Mask into Original Image Size if they are unqual
    if imo.shape[0:2] != ims.shape[0:2]:
        imrs = cv.resize(ims, [imo.shape[1], imo.shape[0]])
    else:
        imrs = ims.copy()

    imo = np.array(imo)
    imrs = np.array(imrs)
    hairExtract = np.uint8(imo * (imrs / 255))
    cv.imwrite('files/output.jpg', hairExtract, [int(cv.IMWRITE_JPEG_QUALITY), 100])
    return 'Hair Extracted!'

    
