import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config

margin = 25
x, y = (50,50)

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, margin, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c=[0,0,0,255])
    xo, yo = primitif.utility.convert_to_cartesian(x,y, py5.width, py5.height, margin)
    xc,yc = (xo+x, yo-y)
    
    if config.anim <= config.times:
        primitif.basic.persegi(xo,yo, 100, c=[255,0,0,255])
    elif config.anim <= 2*config.times:
        primitif.basic.persegi_panjang(xo,yo, 200, 100, c=[255,0,0,255])
    elif config.anim <= 3*config.times:
        primitif.basic.kali(xo,yo, 100, c=[255,0,0,255])
    elif config.anim <= 4*config.times:
        primitif.basic.segitiga_siku(xo,yo, 50,100)
    elif config.anim <= 5*config.times:
        primitif.basic.trapesium_siku(xo,yo, 100, 200, 100)
    elif config.anim <= 6*config.times:
        primitif.basic.lingkaran(xc,yc, 50)
    elif config.anim <= 7*config.times:
        primitif.basic.ellips(xc,yc, 50, 100)
    
    if config.anim > 7*config.times:
        config.anim = 0
        
    config.anim += 1

py5.run_sketch()
