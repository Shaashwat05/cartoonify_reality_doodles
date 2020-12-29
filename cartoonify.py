import cv2
from yolo import yolo
from draw import get_objects, drawing, draw_person
from color import coloring
import numpy as np

# Object Detection
image = cv2.imread("gallery/image1.png")
boxes, classes = yolo(image.copy())


# Objects -> doodles
boxes_final, objs, boxes_person, objs_person = get_objects(boxes, classes)


# Coloring the sketched image
colors = coloring(boxes, image)
colors = list(np.array(colors)/255)
print(colors)


# Drawing colored doodles
surface = drawing(boxes_final, objs, colors, classes)
draw_person(surface, boxes_person, objs_person, colors, classes)
