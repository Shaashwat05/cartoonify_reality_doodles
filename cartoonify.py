import cv2
from yolo import yolo
from draw import get_objects, drawing, position

# Object Detection
image = cv2.imread("gallery/image1.png")
boxes, classes = yolo(image)

# Objects -> doodles
objs = get_objects(classes)

drawing(objs)


