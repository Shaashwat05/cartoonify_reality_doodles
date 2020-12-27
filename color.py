import cv2
import numpy as np

def coloring(boxes, image):

    print(image.shape)

    colors = []
    for i in range(len(boxes)):
        x, y, w, h = boxes[i]
        colors.append((np.mean(image[x:x+w, y:y+h, 0]), np.mean(image[x:x+w, y:y+h, 1]), np.mean(image[x:x+w, y:y+h, 2])))
    
    #print(colors)
    return colors

#coloring(cv2.imread("gallery/image1.png"))


