import cv2


class MNISTImage(object):
    """
    Stores MNIST image label and pixels.
    """
    def __init__(self, pixels, label):
        self.m_pixels = pixels
        self.m_label = label

    def displayImage(self):
        """
        Display the image using OpenCV.
        """
        title = 'Label is {label}'.format(label=self.m_label)
        cv2.imshow(title, self.m_pixels)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
