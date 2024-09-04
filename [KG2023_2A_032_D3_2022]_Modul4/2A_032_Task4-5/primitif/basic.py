import primitif.line
import py5
import numpy as np

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin,margin,width-margin,margin))
    py5.points(primitif.line.line_dda(margin,height-margin,width-margin,height-margin))
    py5.points(primitif.line.line_bresenham(margin,margin,margin,height-margin))
    py5.points(primitif.line.line_bresenham(width-margin,margin,width-margin,height-margin))

def draw_grid(width, height, margin, c=[0,0,0,255]):
    # Sumbu Y
    xa = margin;
    ya = 2*margin;
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)
    
    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa,ya,xb,ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa,ya,xa,yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2,margin,width/2,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/2,width-margin,height/2))


def draw_bentuk(pts, line_type, c):
    py5.stroke(c[0], c[1], c[2], c[3])
    fill_true = True
    j = 0
    
    if line_type == 0:
            py5.points(pts)
    elif line_type == 1:
        for x, y in pts:
            if j == 8:
                if fill_true:
                    fill_true = False
                else:
                    fill_true = True
                j = 0
            if fill_true:
                py5.point(x, y)
            j += 1
    elif line_type == 2:
        for x, y in pts:
            if x % 2 == 0 and y % 2 == 0:
                py5.point(x, y)
    elif line_type == 3:
        j = 10
        i = 1
        for x, y in pts:
            if j == 0:
                if fill_true:
                    fill_true = False
                    j = 7
                    if i == 1:
                        i = 2
                    else:
                        i = 1
                else:
                    fill_true = True
                    if i == 1:
                        j = 10
                    else:
                        j = 2
            if fill_true:
                py5.point(x, y)
            j -= 1

def persegi(xa, ya, panjang):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya,xa+panjang,ya)
            , primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya+panjang)
            , primitif.line.line_bresenham(xa,ya,xa,ya+panjang)
            , primitif.line.line_bresenham(xa+panjang,ya, xa+panjang,ya+panjang)
            ),
        axis=0
    )

def persegi_panjang(xa, ya, panjang, lebar):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya,xa+panjang,ya)
            , primitif.line.line_bresenham(xa+panjang,ya,xa+panjang,ya+lebar)
            , primitif.line.line_bresenham(xa+panjang,ya+lebar,xa,ya+lebar)
            , primitif.line.line_bresenham(xa,ya+lebar,xa,ya)
            ),
        axis=0
        )

def segitiga_siku(xa, ya, alas, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya,xa+alas,ya)
            , primitif.line.line_bresenham(xa+alas,ya,xa,ya-tinggi)
            , primitif.line.line_bresenham(xa,ya-tinggi,xa,ya)
            ),
        axis=0
        )


def trapesium_siku(xa, ya, aa, ab, tinggi):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya,xa,ya-tinggi)
            , primitif.line.line_bresenham(xa,ya-tinggi,xa+aa,ya-tinggi)
            , primitif.line.line_bresenham(xa+aa,ya-tinggi,xa+ab,ya)
            , primitif.line.line_bresenham(xa+ab,ya,xa,ya)
            ),
        axis=0
        )

def kali(xa, ya, panjang):
    return np.concatenate(
        (
            primitif.line.line_bresenham(xa,ya,xa+panjang,ya+panjang)
            , primitif.line.line_bresenham(xa,ya+panjang,xa+panjang,ya)
            ),
        axis=0
    )

def circlePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        [xc + y, yc + x],
        [xc - y, yc + x],
        [xc + y, yc - x],
        [xc - y, yc - x],
        ]
    return res

def lingkaran(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius
    res = circlePlotPoints(xc, yc, x, y) 
    while(x < y):
        x+=1
        if (p < 0):
            p+= 2*x + 1
        else:
            y-=1
            p+= 2*(x-y) + 1
        
        res = np.concatenate(
            (
                res
                , circlePlotPoints(xc, yc, x, y)
            ), axis=0)
        
    
    return res
        
def ellipsePlotPoints(xc, yc, x, y):
    
    res = [
        [xc+x,yc+y],
        [xc-x,yc+y],
        [xc+x,yc-y],
        [xc-x,yc-y],
        ]
    
    return res

def ellips(xc, yc, Rx, Ry):
    Rx2 = Rx * Rx
    Ry2 = Ry * Ry
    twoRx2 = 2 * Rx2
    twoRy2 = 2 * Ry2
    p = 0
    x = 0
    y = Ry
    px = 0
    py = twoRx2 * y

    res = ellipsePlotPoints(xc, yc, x, y)

    p = round(Ry2 - (Rx2 * Ry) + (0.25 * Rx2))
    while px < py:
        x += 1
        px += twoRy2
        if p < 0:
            p += Ry2 + px
        else:
            y -= 1
            py -= twoRx2
            p += Ry2 + px - py
        res = np.concatenate(
            (
                res
                , ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)

    p = round(Ry2 * (x + 0.5) * (x + 0.5) + Rx2 * (y - 1) * (y - 1) - Rx2 * Ry2)
    while y > 0:
        y -= 1
        py -= twoRx2
        if p > 0:
            p += Rx2 - py
        else:
            x += 1
            px += twoRy2
            p += Rx2 - py + px
        res = np.concatenate(
            (
                res
                , ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)

    return res