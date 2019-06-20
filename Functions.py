import timeit

import numpy as np
import cv2

maskHeight = 3
maskWidth = 3
mask = np.ones((maskWidth, maskHeight))

def correlationType1(args):

    image = cv2.imread(args["image"])
    imageResult = cv2.imread(args["image"])
    (height, width) = image.shape[:2]

    for h in range (height):
        for w in range (width):
            imageResult[h][w] = applyMaskForPixel(image, h, w)


    cv2.imshow("image", np.hstack([image, imageResult]))
    cv2.waitKey(0)

def applyMaskForPixel(img, x, y):

    try:
        neighborhoodIntensity = img[x - 1][y + 1] * mask[0][0]
        neighborhoodIntensity += img[x - 1][y] * mask[1][0]
        neighborhoodIntensity += img[x - 1][y - 1] * mask[2][0]

        neighborhoodIntensity += img[x][y + 1] * mask[0][1]
        neighborhoodIntensity += img[x][y] * mask[1][1]
        neighborhoodIntensity += img[x][y - 1] * mask[2][1]

        neighborhoodIntensity += img[x + 1][y + 1] * mask[0][2]
        neighborhoodIntensity += img[x + 1][y] * mask[1][2]
        neighborhoodIntensity += img[x + 1][y - 1] * mask[2][2]
    except:
        neighborhoodIntensity = img[x, y]

    return neighborhoodIntensity / (maskWidth * maskHeight)