[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 

# cartoonify_reality_doodles

The aim is to convert images into doodles using the google quickdraw dataset. This is different from your usual conversion that uses images processing algorithms like K Means Clustering. Firstly, the original image is taken and object detection performed. The yolo model in OpenCV is used to perform the following. Each object i.e. cars, humans are extracted with their positions and colors. The objects in question are extracted from the google quickdraw dataset in the form of doodles. These doodles are placed respectively to form the new image.

**Algorithms**- Object Detection, grouping

### Prerequisites

What things you need to install the software and how to install them.

```
os 
numpy 
cv2
gizeh
struct
six 
pathlib
argparse
time
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above. Run cartoonify.py file to convert input images to doodles. The paths are according to the repositories setting. 

```        
$cartoonify.py
```
## Original Image
![The input Image to cartoonify.py](https://github.com/Shaashwat05/cartoonify_reality_doodles/blob/master/gallery/image1.png)

## After Object Detection
![The Output Image of object detection](https://github.com/Shaashwat05/cartoonify_reality_doodles/blob/master/gallery/object1.png)

## Doodled Image 
(Unfinished Output - Working on color and position accuracy)
![The Output Image of cartoonify.py](https://github.com/Shaashwat05/cartoonify_reality_doodles/blob/master/gallery/circle.png)

## Built With

* [python](https://www.python.org/) - The software used
## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) 


## Acknowledgments

* [Google Quickdraw dataset](https://quickdraw.withgoogle.com/data)
*  [Draw This](https://danmacnish.com/drawthis/) by [Dan Macnish](https://danmacnish.com/)

<!--## Documentation--->

<!----The entire documentation and explanation of code as well as concepts can be found in this article: https://iot4beginners.com/cartoonize-reality-with-opencv-and-raspberry-pi/--->



