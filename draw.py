import struct
from struct import unpack
import numpy as np
import gizeh as gz

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

i = 0

for drawing in unpack_drawings('dataset/nose.bin'):
    # do something with the drawing
    #print(np.array(drawing['image'][0]).shape)

    if(i==10):
        x = drawing['image']
    i+=1

lines_list = []

surface = gz.Surface(width=720, height=560) # in pixels

rect = gz.rectangle(lx=720, ly=560, xy=(360,280), fill=(1,1,1))

rect.draw(surface)


for stroke in x:
    x, y = stroke
    points = list(zip(x, y))
    line = gz.polyline(points=points, stroke=[0,0,0], stroke_width=2)
    lines_list.append(line)


lines = gz.Group(lines_list)

lines.draw(surface)



surface.write_to_png("circle.png")



def position():
    pass
