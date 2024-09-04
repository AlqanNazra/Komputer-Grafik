import py5
import primitif.line
import primitif.basic
# import karya.pertemuan2

import math

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 25, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, 25, c=[0,0,0,255])
    # primitif.basic.persegi(x,y, 100, c=[255,0,0,255])

def draw():
    primitif.basic.persegi_panjang(py5.width * 3 // 4, py5.height // 4, 200, 100)
    primitif.basic.persegi(py5.width // 4, py5.height // 4, 100)
    primitif.basic.segitiga_siku(py5.width // 4, py5.height * 3 // 4, 100,100)
    primitif.basic.trapesium_siku(py5.width * 3 // 4, py5.height * 3 // 4, 100, 200, 100)
    pass

py5.run_sketch()
