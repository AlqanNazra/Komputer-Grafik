# https://processing.org/tutorials/coordinatesystemandshapes
import py5
import numpy

def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.rect(100,100,20,100)
    py5.ellipse(100,70,60,60)
    py5.ellipse(81,70,16,32)
    py5.ellipse(119,70,16,32)
    py5.line(90,150,80,160)
    py5.line(110,150,120,160)
    
py5.run_sketch()