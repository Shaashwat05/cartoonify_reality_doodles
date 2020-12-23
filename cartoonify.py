import cv2
from yolo import yolo
from draw

image = cv2.imread("gallery/image1.png")

boxes, classes = yolo(image)

