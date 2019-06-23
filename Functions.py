import numpy as np
import cv2
import timeit

def basicCorrelation(args, mask, maskDimension):
    startTime = timeit.default_timer()

    image = cv2.imread(args["image"])
    (height, width) = image.shape[:2]

    imageResult = np.float64(image)
    for h in range(height):
        for w in range(width):
            imageResult[h][w] = applyMaskForPixel(image, h, w, mask, maskDimension)

    imageResult = np.uint8(normalize(imageResult))

    endTime = timeit.default_timer()
    print("Tempo do algoritmo basico de correlacao: ", endTime - startTime)

    showImages("Normal Correlation", [image, imageResult])

def applyMaskForPixel(img, x, y, mask, maskDimension):
    neighborhoodIntensity = 0
    posX = x - 1
    posY = y - 1

    for i in range(maskDimension):
        for j in range(maskDimension):
            try:
                neighborhoodIntensity += img[posX + i][posY + j] * mask[i][j]
            except:
                neighborhoodIntensity += 0

    return neighborhoodIntensity / (maskDimension * maskDimension)


def fastCorrelation(args, mask, maskDimension):
    startTime = timeit.default_timer()
    BLACK = [0, 0, 0]
    border = 1
    image = cv2.imread(args["image"])
    (height, width) = image.shape[:2]

    images = []
    weights = createMask(mask, maskDimension)

    imageBordered = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_CONSTANT, None, value=BLACK)
    imageBordered = np.float64(imageBordered)

    for i in range(len(weights)):
        imageAux = np.copy(imageBordered)
        imageAux = np.roll(imageAux, weights[i][0][0], axis=0)
        imageAux = np.roll(imageAux, weights[i][0][1], axis=1)
        np.multiply(imageAux, weights[i][1], out=imageAux, casting='unsafe')
        images.append(imageAux)

    result = np.sum(images, axis = 0)
    result = np.uint8(normalize(result))
    result = result[1:height+1, 1:width+1]

    endTime = timeit.default_timer()
    print("Tempo do algoritmo rapido de correlacao: ", endTime - startTime)

    showImages("Fast Correlation", [image, result])

def createMask(mask, maskDimension):
    weights = []
    for i in range(maskDimension):
        for j in range(maskDimension):
            x = -abs(i) + 1
            y = -abs(j) + 1
            coordinate = [x, y]
            weights.append([coordinate, mask[i][j]])
    return weights

def normalize(image):
    image += np.abs(np.amin(image))
    image *= (1.0 / np.amax(image))
    image *= 255.0
    return image

def showImages(name, images):
    cv2.imshow(name, np.hstack(images))
    cv2.waitKey(0)



