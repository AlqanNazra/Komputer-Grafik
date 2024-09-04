import py5
import primitif.line
import primitif.basic
from primitif.basic import circleMidpoint

import math

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 30, c=[0,0,0,255])
    
    py5.points(primitif.line.line_bresenham(py5.width*33/100, 30, py5.width*33/100, py5.height-30))
    py5.points(primitif.line.line_bresenham(py5.width*66/100, 30, py5.width*66/100, py5.height-30))
    py5.points(primitif.line.line_bresenham(30, py5.height*33/100, py5.width-30, py5.height*33/100))
    py5.points(primitif.line.line_bresenham(30, py5.height*66/100, py5.width-30, py5.height*66/100))
    #pemain 1 menang
    primitif.basic.kali(25, 25, 175, c=[0,0,0,255])
    primitif.basic.kali(267, 200, 200, c=[0,0,0,255])
    primitif.basic.kali(534, 400, 175, c=[0,0,0,255])
    
    circleMidpoint(py5.width / 2, 30 + py5.height * 38 / 50, 80)
    circleMidpoint(py5.width / 4.5, 90 + py5.height * 18 / 50, 80)

#     #tidak ada pemenang
#     circleMidpoint(py5.width / 2, 30 + py5.height * 38 / 50, 80)
#     circleMidpoint(py5.width / 1.2, 15 + py5.height * 8 / 50, 80)
#     circleMidpoint(py5.width / 4.5, 90 + py5.height * 18 / 50, 80)
#     circleMidpoint(py5.width / 5, 90 + py5.height * 2 / 50, 80)
#     
#     primitif.basic.kali(25, 400, 175, c=[0,0,0,255])
#     primitif.basic.kali(534, 200, 175, c=[0,0,0,255])
#     primitif.basic.kali(267, 200, 200, c=[0,0,0,255])
#     primitif.basic.kali(534, 400, 175, c=[0,0,0,255])
#     primitif.basic.kali(267, 35, 175, c=[0,0,0,255])
    
def draw():
    pass

py5.run_sketch()

