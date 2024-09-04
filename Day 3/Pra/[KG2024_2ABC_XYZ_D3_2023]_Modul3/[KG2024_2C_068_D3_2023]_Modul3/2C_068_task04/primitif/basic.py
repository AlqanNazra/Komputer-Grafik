import primitif.line
import py5
import numpy as np

def draw_margin(width, height, margin, c=[0,0,0,255], line_type=0):
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_dda(margin, margin, width - margin, margin), line_type)
    draw_bentuk(primitif.line.line_dda(margin, height - margin, width - margin, height - margin), line_type)
    draw_bentuk(primitif.line.line_dda(margin, margin, margin, height - margin), line_type)
    draw_bentuk(primitif.line.line_dda(width - margin, margin, width - margin, height - margin), line_type)

def draw_grid(width, height, margin, c=[0,0,0,255], line_type=0):
    xa = margin
    ya = 2 * margin
    xb = width - xa
    yb = height - ya
    y_range = height / margin
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        draw_bentuk(primitif.line.line_dda(xa, ya, xb, ya), line_type)
        ya = ya + margin

    xa = 2 * margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = width / margin
    for count in range(1, int(x_range)):
        draw_bentuk(primitif.line.line_dda(xa, ya, xa, yb), line_type)
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0,0,0,255], line_type=0):
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_dda(width / 2, margin, width / 2, height - margin), line_type)
    draw_bentuk(primitif.line.line_dda(margin, height / 2, width - margin, height / 2), line_type)

def persegi(xa, ya, panjang, c=[0,0,0,255], line_type=0):
    x = xa - (panjang // 2)
    y = ya - (panjang // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + panjang, x, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + panjang, x, y), line_type)


def persegi_2(xa, ya, panjang, c=[0,0,0,255], line_type=1):
    x = xa - (panjang // 2)
    y = ya - (panjang // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + panjang, x, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + panjang, x, y), line_type)


def persegi_3(xa, ya, panjang, c=[0,0,0,255], line_type=2):
    x = xa - (panjang // 2)
    y = ya - (panjang // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + panjang, x, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + panjang, x, y), line_type)


def persegi_4(xa, ya, panjang, c=[0,0,0,255], line_type=3):
    x = xa - (panjang // 2)
    y = ya - (panjang // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + panjang, x, y + panjang), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + panjang, x, y), line_type)

def persegi_panjang(xa, ya, panjang, lebar, c=[0,0,0,255], line_type=0):
    x = xa - (panjang // 2)
    y = ya - (lebar // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + lebar, x, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + lebar, x, y), line_type)

def persegi_panjang_2(xa, ya, panjang, lebar, c=[0,0,0,255], line_type=1):
    x = xa - (panjang // 2)
    y = ya - (lebar // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + lebar, x, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + lebar, x, y), line_type)

def persegi_panjang_3(xa, ya, panjang, lebar, c=[0,0,0,255], line_type=2):
    x = xa - (panjang // 2)
    y = ya - (lebar // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + lebar, x, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + lebar, x, y), line_type)

def persegi_panjang_4(xa, ya, panjang, lebar, c=[0,0,0,255], line_type=3):
    x = xa - (panjang // 2)
    y = ya - (lebar // 2)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    draw_bentuk(primitif.line.line_bresenham(x, y, x + panjang, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y, x + panjang, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + panjang, y + lebar, x, y + lebar), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + lebar, x, y), line_type)

def segitiga_siku(xa, ya, alas, tinggi, c=[255,0,0,255], line_type=0):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + alas, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + alas, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def segitiga_siku_2(xa, ya, alas, tinggi, c=[255,0,0,255], line_type=1):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + alas, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + alas, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def segitiga_siku_3(xa, ya, alas, tinggi, c=[255,0,0,255], line_type=2):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + alas, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + alas, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def segitiga_siku_4(xa, ya, alas, tinggi, c=[255,0,0,255], line_type=3):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + alas, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + alas, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def trapesium_siku(xa, ya, aa, ab, tinggi, c=[255,0,0,255], line_type=0):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - ab // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + aa, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + aa, y, x + ab, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + ab, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def trapesium_siku_2(xa, ya, aa, ab, tinggi, c=[255,0,0,255], line_type=1):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - ab // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + aa, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + aa, y, x + ab, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + ab, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def trapesium_siku_3(xa, ya, aa, ab, tinggi, c=[255,0,0,255], line_type=2):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - ab // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + aa, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + aa, y, x + ab, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + ab, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)

def trapesium_siku_4(xa, ya, aa, ab, tinggi, c=[255,0,0,255], line_type=3):
    py5.stroke(c[0], c[1], c[2], c[3])
    x = xa - ab // 2
    y = ya - tinggi // 2
    
    draw_bentuk(primitif.line.line_bresenham(x, y, x + aa, y), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + aa, y, x + ab, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x + ab, y + tinggi, x, y + tinggi), line_type)
    draw_bentuk(primitif.line.line_bresenham(x, y + tinggi, x, y), line_type)


def draw_bentuk(pts, line_type):
    if line_type == 0:
        for x, y in pts:
            py5.point(x, y)
    
    elif line_type == 1:
        dash_length = 8
        for i, (x, y) in enumerate(pts):
            if (i // dash_length) % 2 == 0:  
                py5.point(x, y)
    
    elif line_type == 2:
        # Dotted line
        dot_interval = 5
        for i, (x, y) in enumerate(pts):
            if i % dot_interval == 0:  
                py5.point(x, y)
    
    elif line_type == 3:
        # Dashed and dotted line
        dash_length = 8
        dot_interval = 5
        for i, (x, y) in enumerate(pts):
            if (i // dash_length) % 2 == 0:  
                if i % dot_interval == 0:
                    py5.point(x, y)

