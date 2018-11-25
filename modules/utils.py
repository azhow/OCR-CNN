import numpy as np
import csv
import modules.MNISTImage as MNISTImage


def readSet(csvFilePath):
    """
    Reads the entire csv set file and returns it in readImages list
    as 28x28 2D array.
    """
    # Read images are stored in this list
    readImages = []
    with open(csvFilePath, 'r') as csvFile:
        for data in csv.reader(csvFile):
            # The first column is the label
            label = data[0]

            # The rest of columns are pixels
            pixels = data[1:]

            # Make those columns into a array of 8-bits pixels
            # This array will be of 1D with length 784
            # The pixel intensity values are integers from 0 to 255
            pixels = np.array(pixels, dtype='uint8')

            # Reshape the array into 28 x 28 array (2-dimensional array)
            pixels = pixels.reshape((28, 28))

            # Return list
            readImages.append(MNISTImage.MNISTImage(pixels, label))

    return readImages
