import cv2
from yolo import yolo
from draw import get_objects, drawing
#from color import coloring

# Object Detection
image = cv2.imread("gallery/image1.png")
boxes, classes = yolo(image)


# Objects -> doodles
boxes_final, objs = get_objects(boxes, classes)
drawing(boxes_final, objs)

# Coloring the sketched image
#coloring(image)


