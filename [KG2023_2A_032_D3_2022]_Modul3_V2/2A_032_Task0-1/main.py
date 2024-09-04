import py5
import primitif.line
import primitif.basic
from primitif.basic import circleMidpoint
from primitif.basic import ellipse_midpoint
from random import randint

import math
    
def setup():
    py5.size(400, 400)
    py5.background(255)
    py5.stroke(0)
    py5.no_fill()

def draw():
    #lingkaran
    circleMidpoint(py5.width / 2, py5.height / 2, 100)

    #ellipse
#     ellipse_midpoint(py5.width / 2, py5.height / 2, 100, 150)    
#     py5.stroke(randint(0,255),randint(0,255),randint(0,255),255)

py5.run_sketch()