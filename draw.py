import struct
from struct import unpack
import numpy as np
import gizeh as gz
from os import path


def unpack_drawing(file_handle):
    key_id, = unpack('Q', file_handle.read(8))
    country_code, = unpack('2s', file_handle.read(2))
    recognized, = unpack('b', file_handle.read(1))
    timestamp, = unpack('I', file_handle.read(4))
    n_strokes, = unpack('H', file_handle.read(2))
    image = []
    for i in range(n_strokes):
        n_points, = unpack('H', file_handle.read(2))
        fmt = str(n_points) + 'B'
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        'key_id': key_id,
        'country_code': country_code,
        'recognized': recognized,
        'timestamp': timestamp,
        'image': image
    }


def unpack_drawings(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break



def get_objects(boxes, classes):

    objs = []
    LABELS =open("yolo/coco.names").read().strip().split("\n")
    boxes2 = []

    i=-1
    for y_class in classes:
        i+=1
        try:
            arr = unpack_drawings('dataset/'+str(LABELS[y_class])+'.bin')
            if(path.exists('dataset/'+str(LABELS[y_class])+'.bin')):
                boxes2.append(boxes[i])
            num = np.random.randint(0,50)
            for drawing in arr:
                objs.append(drawing)
                break
        except:
            continue
    
    return boxes2, objs


def drawing(boxes, objs):

    surface = gz.Surface(width=720, height=560) # in pixels
    rect = gz.rectangle(lx=720, ly=560, xy=(360,280), fill=(1,1,1))
    rect.draw(surface)

    i=0
    for strokes in objs:
        lines_list = []
        for stroke in strokes['image']:
            x, y = stroke

            x = tuple([(z*boxes[i][2])//255 for z in x])
            y = tuple([(z*boxes[i][3])//255 for z in y])

            x = tuple([z+boxes[i][0] for z in x])
            y = tuple([z+boxes[i][1] for z in y])

            points = list(zip(x, y))
            line = gz.polyline(points=points, stroke=[0,0,0], stroke_width=2)
            lines_list.append(line)

        lines = gz.Group(lines_list)
        lines.draw(surface)
        i+=1

    surface.write_to_png("gallery/circle.png")



    
    
