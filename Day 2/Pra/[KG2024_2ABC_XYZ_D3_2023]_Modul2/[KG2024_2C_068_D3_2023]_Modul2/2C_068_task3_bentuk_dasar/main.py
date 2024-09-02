import py5
import primitif.line
import primitif.basic
import math

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 25, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, 25, c=[0,0,0,255])
    

def draw():
    pass
    primitif.basic.persegi(py5.width, py5.height, 25,c=[0,0,0,255])
    primitif.basic.persegi_panjang(py5.width, py5.height, 25,c=[0,0,0,255])

    

py5.run_sketch()
