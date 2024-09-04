import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config

margin = 25
x, y = (50, 50)

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)

def draw():
    width = 800
    heigth = 600
    py5.background(191)
    c = [0, 0, 0, 255]
    primitif.basic.draw_margin(py5.width, py5.height, margin, c)
    primitif.basic.draw_kartesian(py5.width, py5.height, margin, c)
    xo, yo = primitif.utility.convert_to_cartesian(x, y, py5.width, py5.height, margin)
    half_width = width // 2  # 400
    half_heigth = heigth // 2  # 300
    xc, yc = (xo + x, yo - y)

    if config.anim <= 2 * config.times:
        primitif.basic.persegi(6 * half_width // 4, half_heigth // 2, 100, c=[255, 0, 0, 255]) # 1
        primitif.basic.persegi_2(half_width // 2, half_heigth // 2, 100, c=[255, 0, 0, 255]) # 2
        primitif.basic.persegi_3(half_width // 2, 3 * half_heigth // 2, 100, c=[255, 0, 0, 255]) # 3
        primitif.basic.persegi_4(6 * half_width // 4, 3 * half_heigth // 2, 100, c=[255, 0, 0, 255]) # 4
    
    elif config.anim <= 4 * config.times:
        primitif.basic.persegi_panjang(6 * half_width // 4, half_heigth // 2, 200, 100, c=[255, 0, 0, 255]) # 1
        primitif.basic.persegi_panjang_2(half_width // 2, half_heigth // 2, 200, 100, c=[255, 0, 0, 255]) # 2
        primitif.basic.persegi_panjang_3(half_width // 2, 3 * half_heigth // 2, 200, 100, c=[255, 0, 0, 255]) # 3
        primitif.basic.persegi_panjang_4(6 * half_width // 4, 3 * half_heigth // 2, 200, 100, c=[255, 0, 0, 255]) # 4
    
    elif config.anim <= 6 * config.times:
        primitif.basic.segitiga_siku(6 * half_width // 4, half_heigth // 2, 50, 100) # Kuadran 1
        primitif.basic.segitiga_siku_2(half_width // 2, half_heigth // 2, 50, 100) # Kuadran 2
        primitif.basic.segitiga_siku_3(half_width // 2, 3 * half_heigth // 2, 50, 100) # Kuadran 3
        primitif.basic.segitiga_siku_4(6 * half_width // 4, 3 * half_heigth // 2, 50, 100) # Kuadran 4
    
    elif config.anim <= 8 * config.times:
        primitif.basic.trapesium_siku(6 * half_width // 4, half_heigth // 2, 100, 200, 100) # 1
        primitif.basic.trapesium_siku_2(half_width // 2, half_heigth // 2, 100, 200, 100) # 2
        primitif.basic.trapesium_siku_3(half_width // 2, 3 * half_heigth // 2, 100, 200, 100) # 3
        primitif.basic.trapesium_siku_4(6 * half_width // 4, 3 * half_heigth // 2, 100, 200, 100) # 4

    
    if config.anim > 9 * config.times:
        config.anim = 0

    config.anim += 1

py5.run_sketch()


buat program ini menggnuakan class dan objcet