import argparse
import Functions as F

# argumentos do programa
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

F.correlationType1(args)