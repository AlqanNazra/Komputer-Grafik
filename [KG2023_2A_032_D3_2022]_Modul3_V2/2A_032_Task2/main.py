import py5
import primitif.line
import primitif.basic
import karya.task3

import math

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 25, c=[0,0,0,255])
    primitif.basic.draw_kartesian(py5.width, py5.height, 25, c=[0,0,0,255])
    
#     #persegi
#     # Ukuran dan posisi persegi
#     sisi = 100
#     x, y = 100, 100  #Koordinat yang diinginkan
# 
#     # Convert x and y to cartesian coordinates
#     cartesian_coords = primitif.utility.convert_to_cartesian(x, y, py5.width, py5.height, 25)
#     #kuadran 1
#     primitif.basic.persegi(cartesian_coords[0], cartesian_coords[1], sisi, c=[255, 0, 0, 255])
#     #kuadran 2
#     primitif.basic.persegi(cartesian_coords[1], cartesian_coords[1], sisi, c=[255, 0, 0, 255])
#     #kuadran 3
#     primitif.basic.persegi(cartesian_coords[1], cartesian_coords[0], sisi, c=[255, 0, 0, 255])
#     #kuadran 4
#     primitif.basic.persegi(cartesian_coords[0], cartesian_coords[0], sisi, c=[255, 0, 0, 255])
#     
#     #persegi panjang
#     # Ukuran dan posisi persegi panjang
#     panjang = 150
#     lebar = 100
#     x, y = 100, 150  #koordinat yang diinginkan
#     # Convert x and y ke koordinat kartesian
#     cartesian_coords = primitif.utility.convert_to_cartesian(x, y, py5.width, py5.height, 25)
#     #Kuadran 1
#     primitif.basic.persegi_panjang(cartesian_coords[0], cartesian_coords[1], panjang, lebar)
#     #Kuadran 2
#     primitif.basic.persegi_panjang(cartesian_coords[1], cartesian_coords[1], panjang, lebar)
#     #Kuadran 3
#     primitif.basic.persegi_panjang(cartesian_coords[1], cartesian_coords[0], panjang, lebar)
#     #Kuadran 4
#     primitif.basic.persegi_panjang(cartesian_coords[0], cartesian_coords[0], panjang, lebar)
#      
    #segitiga siku siku
    x, y = 40, 80   # Ganti dengan koordinat yang diinginkan

    # Convert x dan y ke koordinat kartesian
    cartesian_coords = primitif.utility.convert_to_cartesian(x, y, py5.width, py5.height, 25)

    # Gambar segitiga siku kuadran 1
    primitif.basic.segitiga_siku(cartesian_coords[0], cartesian_coords[1], 100, 100)
    # Gambar segitiga siku kuadran 2
    primitif.basic.segitiga_siku(cartesian_coords[1], cartesian_coords[1], -100, 100)
    # Gambar segitiga siku kuadran 3
    primitif.basic.segitiga_siku(cartesian_coords[1], cartesian_coords[0], -100, -100)
    # Gambar segitiga siku kuadran 4
    primitif.basic.segitiga_siku(cartesian_coords[0], cartesian_coords[0], 100, -100)

     #trampesium
    a = [130, 600]
    b = [130, 400]
    for x in a:
         for y in b:
             primitif.basic.trapesium_siku(x, y, 50, 100, 100, c=[0,0,0,255])
     
    
def draw():
    pass

py5.run_sketch()
