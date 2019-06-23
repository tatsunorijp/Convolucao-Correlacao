import argparse
import numpy as np
import Functions as F

# argumentos do programa
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

maskDimension = int(input("Digite a dimensão da matriz: "))
mask = np.zeros(maskDimension * maskDimension)
mask = mask.reshape((maskDimension, maskDimension))

for i in range(maskDimension):
    for j in range(maskDimension):
        mask[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

print("Aguarde")

F.basicCorrelation(args, mask, maskDimension)
F.fastCorrelation(args, mask, maskDimension)
