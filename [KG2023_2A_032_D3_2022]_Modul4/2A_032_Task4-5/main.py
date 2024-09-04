import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasiv2
import math
import config
import numpy as np

#print(persegi2)
#kali = primitif.basic.kali(0,0,100)
#lingkaran = primitif.basic.lingkaran(50,50,50)


def setup():
    py5.size(800,600) #ubah size agar lebih besar
    
    py5.rect_mode(py5.CENTER)
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 25, c=[0, 0, 0, 255])
    primitif.basic.draw_kartesian(py5.width, py5.height, 25, c=[0, 0, 0, 255])
    c =[0,0,0,255]

#===================================================================================================================================#
    
#======persegi======#

    x, y = 50, 100
    sisi = 100
    tm =np.zeros(3) #inisiasi matriks
    #convert x dan y ke koordinat kartesian
    xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
    xc,yc = (xo+x, yo-y)
    
    #kuadran1
    persegi = primitif.basic.persegi(xc+100, yc, sisi)
    primitif.basic.draw_bentuk(persegi,0,c)
    
    #kuadran2
    persegi = primitif.basic.persegi(x+105,yc, sisi)
    primitif.basic.draw_bentuk(persegi,1,c)
    
    #kuadran3
    tm_kuadran3 = np.zeros(3)
    
    tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
    print(tm_kuadran3)
    tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
    print(tm_kuadran3)
    tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
    print(tm_kuadran3)
    tm_kuadran3 = primitif.transformasiv2.translate2D(x-150, 2.2*yo, tm_kuadran3)
    print(tm_kuadran3)
    persegi = primitif.transformasiv2.transformPoints2D(persegi, tm_kuadran3)
    primitif.basic.draw_bentuk(persegi,2,c)
    
    #kuadran4
    tm_kuadran4 = np.zeros(3)
    
    tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
    print(tm_kuadran4)
    tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
    print(tm_kuadran4)
    tm_kuadran4 = primitif.transformasiv2.translate2D(xc-200, yo, tm_kuadran4)
    print(tm_kuadran4)
    tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
    persegi = primitif.transformasiv2.transformPoints2D(persegi, tm_kuadran4)
    primitif.basic.draw_bentuk(persegi,3,c)

#===================================================================================================================================#

#======persegi panjang======#

#     x, y = 50, 100
#     panjang = 150
#     lebar = 100
#     tm =np.zeros(3) #inisiasi matriks
#     
#     #convert x dan y ke koordinat kartesian
#     xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
#     xc,yc = (xo+x, yo-y)
#     
#     #kuadran1
#     persegi_panjang = primitif.basic.persegi_panjang(xc+100, yc, panjang, lebar)
#     primitif.basic.draw_bentuk(persegi_panjang,2,c)
#     
#     #kuadran2
#     persegi_panjang = primitif.basic.persegi_panjang(x+105,yc, panjang, lebar)
#     primitif.basic.draw_bentuk(persegi_panjang,1,c)
#     
#     #kuadran3
#     tm_kuadran3 = np.zeros(3)
#     
#     tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.translate2D(x-150, 2.2*yo, tm_kuadran3)
#     print(tm_kuadran3)
#     persegi_panjang = primitif.transformasiv2.transformPoints2D(persegi_panjang, tm_kuadran3)
#     primitif.basic.draw_bentuk(persegi_panjang,0,c)
#     
#     #kuadran4
#     tm_kuadran4 = np.zeros(3)
#     
#     tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.translate2D(xc-200, yo, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
#     persegi_panjang = primitif.transformasiv2.transformPoints2D(persegi_panjang, tm_kuadran4)
#     primitif.basic.draw_bentuk(persegi_panjang,3,c)

#===================================================================================================================================#

#======segitiga siku siku======#

#     x, y = 40, 80   # Ganti dengan koordinat yang diinginkan
#     alas= 100
#     tinggi=100
#     
#     #convert x dan y ke koordinat kartesian
#     xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
#     xc,yc = (xo+x, yo-y)
#     
#     #kuadran1
#     segitiga_siku = primitif.basic.segitiga_siku(xc+100, yc, alas, tinggi)
#     primitif.basic.draw_bentuk(segitiga_siku,2,c)
#     
#     #kuadran2
#     segitiga_siku = primitif.basic.segitiga_siku(x+105,yc, alas, tinggi)
#     primitif.basic.draw_bentuk(segitiga_siku,1,c)
#     
#     #kuadran3
#     tm_kuadran3 = np.zeros(3)
#     
#     tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.translate2D(x-150, 1.2*yo, tm_kuadran3)
#     print(tm_kuadran3)
#     segitiga_siku = primitif.transformasiv2.transformPoints2D(segitiga_siku, tm_kuadran3)
#     primitif.basic.draw_bentuk(segitiga_siku,0,c)
#     
#     #kuadran4
#     tm_kuadran4 = np.zeros(3)
#     
#     tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.translate2D(xc-200, yo, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
#     segitiga_siku = primitif.transformasiv2.transformPoints2D(segitiga_siku, tm_kuadran4)
#     primitif.basic.draw_bentuk(segitiga_siku,3,c)

#===================================================================================================================================#

#======trapesium siku siku======#

#     x, y= 40, 80
#     sisi1=50
#     sisi2=100
#     tinggi=100
#     tm = np.zeros(3) #deklar matriks
#      # Convert x dan y ke koordinat kartesian
#     xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
#     xc,yc = (xo+x, yo-y)
#     
#     #kuadran1
#     trapesium_siku=primitif.basic.trapesium_siku(xc+100, yc, sisi1, sisi2, tinggi)
#     primitif.basic.draw_bentuk(trapesium_siku,0,c)
#     
#     #kuadran 2
#     trapesium_siku=primitif.basic.trapesium_siku(x+105, yc, sisi1, sisi2, tinggi)
#     primitif.basic.draw_bentuk(trapesium_siku,1,c)
#     
#     #kuadran 3a
#     tm_kuadran3 = np.zeros(3)
#     tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.translate2D(x-45, 1.4*yo, tm_kuadran3)
#     print(tm_kuadran3)
#     trapesium_siku = primitif.transformasiv2.transformPoints2D(trapesium_siku, tm_kuadran3)
#     primitif.basic.draw_bentuk(trapesium_siku,2,c)
#     
#     # Kuadran 4
#     tm_kuadran4 = np.zeros(3)
#     tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.translate2D(xc-15, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
#     trapesium_siku = primitif.transformasiv2.transformPoints2D(trapesium_siku, tm_kuadran4)
#     primitif.basic.draw_bentuk(trapesium_siku,3,c)


#===================================================================================================================================#
 
#======lingkaran======#

#     x, y= 100, 80
#     radius=50
# 
#     tm = np.zeros(3) #deklar matriks
#     
#     # Convert x dan y ke koordinat kartesian
#     xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
#     xc,yc = (xo+x, yo-y)
#     
#     #kuadran1
#     lingkaran=primitif.basic.lingkaran(xc+100, yc, radius)
#     primitif.basic.draw_bentuk(lingkaran,3,c)
#     
#     #kuadran 2
#     lingkaran=primitif.basic.lingkaran(x+105, yc, radius)
#     primitif.basic.draw_bentuk(lingkaran,1,c)
#     
#     #kuadran 3
#     tm_kuadran3 = np.zeros(3)
#     tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
#     print(tm_kuadran3)
#     tm_kuadran3 = primitif.transformasiv2.translate2D(x-100, 1.6*yo, tm_kuadran3)
#     print(tm_kuadran3)
#     lingkaran = primitif.transformasiv2.transformPoints2D(lingkaran, tm_kuadran3)
#     primitif.basic.draw_bentuk(lingkaran,2,c)
#     
#     # Kuadran 4
#     tm_kuadran4 = np.zeros(3)
#     tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.translate2D(xc-150, 0, tm_kuadran4)
#     print(tm_kuadran4)
#     tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
#     lingkaran = primitif.transformasiv2.transformPoints2D(lingkaran, tm_kuadran4)
#     primitif.basic.draw_bentuk(lingkaran,0,c)
    
#===================================================================================================================================#

#======ellips======#

    # x, y= 100, 80
    # radiusx=100
    # radiusy=50
    
    # tm = np.zeros(3) #deklar matriks
    
    # # Convert x dan y ke koordinat kartesian
    # xo,yo = primitif.utility.convert_to_cartesian(x,y,py5.width,py5.height,25)
    # xc,yc = (xo+x, yo-y)
    
    # #kuadran1
    # ellips=primitif.basic.ellips(xc+50, yc, radiusx, radiusy)
    # primitif.basic.draw_bentuk(ellips,3,c)
    
    # #kuadran 2
    # ellips=primitif.basic.ellips(x+105, yc, radiusx, radiusy)
    # primitif.basic.draw_bentuk(ellips,1,c)
    
    # #kuadran 3
    # tm_kuadran3 = np.zeros(3)
    # tm_kuadran3 = primitif.transformasiv2.rotate2D(180, 0, yc)
    # print(tm_kuadran3)
    # tm_kuadran3 = primitif.transformasiv2.reflectY2D(tm_kuadran3)
    # print(tm_kuadran3)
    # tm_kuadran3 = primitif.transformasiv2.scale2D(1.5,1.5, 0, 0, tm_kuadran3)
    # print(tm_kuadran3)
    # tm_kuadran3 = primitif.transformasiv2.translate2D(x-200, 1.6*yo, tm_kuadran3)
    # print(tm_kuadran3)
    # ellips = primitif.transformasiv2.transformPoints2D(ellips, tm_kuadran3)
    # primitif.basic.draw_bentuk(ellips,2,c)
    
    # # Kuadran 4
    # tm_kuadran4 = np.zeros(3)
    # tm_kuadran4 = primitif.transformasiv2.rotate2D(0, 0, yc)
    # print(tm_kuadran4)
    # tm_kuadran4 = primitif.transformasiv2.scale2D(0.5, 0.5, 0, 0, tm_kuadran4)
    # print(tm_kuadran4)
    # tm_kuadran4 = primitif.transformasiv2.translate2D(xc-200, 0.5*yo, tm_kuadran4)
    # print(tm_kuadran4)
    # tm_kuadran4 = primitif.transformasiv2.shear2D(0.5, 0.2, tm_kuadran4)
    # ellips = primitif.transformasiv2.transformPoints2D(ellips, tm_kuadran4)
    # primitif.basic.draw_bentuk(ellips,0,c)


#===================================================================================================================================#

def draw():
    #primitif.basic.draw_bentuk(kali)
    #primitif.basic.draw_bentuk(lingkaran)
    pass

py5.run_sketch()
