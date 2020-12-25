import cv2
import numpy

def coloring(image):

    

    doodle = cv2.imread("gallery/circle.png")

    image = cv2.resize(image, (doodle.shape[1], doodle.shape[0]))


    image[doodle == 0] = 0

    cv2.imshow("img", image)
    cv2.waitKey(0)

coloring(cv2.imread("gallery/image1.png"))