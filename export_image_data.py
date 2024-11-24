import csv
import cv2
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

# This would be used in tandem with the file reading to save the properly 
# converted files to a re-usable format.

labels = ["test"]
images = [cv2.imread("./example_image.png")]

# Writes the given image to a csv file for recording purposes. 
# Currently, there's a few issues with it, a fix would be to
# properly append information ala "[4,3,2]" for each pixel value.
with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    print("test")
    for image, label in zip(images, labels):
        writer.writerow([image, str(label)])
