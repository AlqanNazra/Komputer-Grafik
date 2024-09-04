import primitif.line
import py5

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
    
def persegi(xa, ya, panjang, c=[0,0,0,255]):
    pass

def persegi_panjang(xa, ya, panjang, lebar, c=[0,0,0,255]):
    pass

def segitiga_siku(xa, ya, alas, tinggi, c=[0,0,0,255]):
    pass

def trapesium_siku(xa, ya, aa, ab, tinggi, c=[0,0,0,255]):
    pass

def kali(xa, ya, panjang, c=[0,0,0,255]):
    pass

def circleMidpoint(xCenter, yCenter, radius):
    x = 0
    y = radius
    p = 1 - radius

    circlePlotPoints(xCenter, yCenter, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        circlePlotPoints(xCenter, yCenter, x, y)

def circlePlotPoints(xCenter, yCenter, x, y):
    py5.point(xCenter + x, yCenter + y)
    py5.point(xCenter - x, yCenter + y)
    py5.point(xCenter + x, yCenter - y)
    py5.point(xCenter - x, yCenter - y)
    py5.point(xCenter + y, yCenter + x)
    py5.point(xCenter - y, yCenter + x)
    py5.point(xCenter + y, yCenter - x)
    py5.point(xCenter - y, yCenter - x)

def ellipse_midpoint(xCenter, yCenter, Rx, Ry):
    def ellipse_plot_points(xCenter, yCenter, x, y):
        py5.point(xCenter + x, yCenter + y)
        py5.point(xCenter - x, yCenter + y)
        py5.point(xCenter + x, yCenter - y)
        py5.point(xCenter - x, yCenter - y)
    Rx2 = Rx * Rx
    Ry2 = Ry * Ry
    twoRx2 = 2 * Rx2
    twoRy2 = 2 * Ry2
    p = 0
    x = 0
    y = Ry
    px = 0
    py = twoRx2 * y

    # Plot the first set of points
    ellipse_plot_points(xCenter, yCenter, x, y)

    # Region 1
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
        ellipse_plot_points(xCenter, yCenter, x, y)

    # Region 2
    p = round(Ry2 * (x + 0.5) ** 2 + Rx2 * (y - 1) ** 2 - Rx2 * Ry2)
    while y > 0:
        y -= 1
        py -= twoRx2
        if p > 0:
            p += Rx2 - py
        else:
            x += 1
            px += twoRy2
            p += Rx2 - py + px
        ellipse_plot_points(xCenter, yCenter, x, y)
