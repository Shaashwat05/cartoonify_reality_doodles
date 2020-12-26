import cv2
from yolo import yolo
from draw import get_objects, drawing
from color import coloring
import numpy as np

# Object Detection
image = cv2.imread("gallery/image2.jpg")
boxes, classes = yolo(image.copy())


# Objects -> doodles
boxes_final, objs = get_objects(boxes, classes)


# Coloring the sketched image
colors = coloring(boxes, image)
colors = list(np.array(colors)/255)

# Drawing colored doodles
drawing(boxes_final, objs, colors)
