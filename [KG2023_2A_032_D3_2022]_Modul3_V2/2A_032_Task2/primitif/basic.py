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
    
def persegi(xa, ya, sisi, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.begin_shape()
    py5.vertex(xa, ya)
    py5.vertex(xa + sisi, ya)
    py5.vertex(xa + sisi, ya - sisi)
    py5.vertex(xa, ya - sisi)
    py5.end_shape(py5.CLOSE)

def persegi_panjang(xa, ya, panjang, lebar):
    c=[0,0,0,255]
    # Hitung koordinat akhir (xb, yb) berdasarkan panjang dan lebar
    xb = xa + panjang
    yb = ya - lebar

    # Gambar sisi atas
    py5.points(primitif.line.line_bresenham(xa, ya, xb, ya))
    
    # Gambar sisi kanan
    py5.points(primitif.line.line_bresenham(xb, ya, xb, yb))
    
    # Gambar sisi bawah
    py5.points(primitif.line.line_bresenham(xb, yb, xa, yb))
    
    # Gambar sisi kiri
    py5.points(primitif.line.line_bresenham(xa, yb, xa, ya))

    pass

def segitiga_siku(xa, ya, alas, tinggi):

    py5.points(primitif.line.line_bresenham(xa, ya, xa + alas, ya))  # Sisi bawah
    py5.points(primitif.line.line_bresenham(xa, ya, xa, ya - tinggi))  # Sisi kiri
    py5.points(primitif.line.line_bresenham(xa, ya - tinggi, xa + alas, ya))  # Hypotenuse
    pass

def trapesium_siku(xa, ya, aa, ab, tinggi, c=[0,0,0,255]):
    xb = xa + aa
    xc = xa + ab
    yb = ya + tinggi
    py5.points(primitif.line.line_bresenham(xa, ya, xb, ya))
    py5.points(primitif.line.line_bresenham(xa, yb, xc, yb))
    py5.points(primitif.line.line_bresenham(xc, yb, xb, ya))
    py5.points(primitif.line.line_bresenham(xa, ya, xa, yb))
    pass

def kali(xa, ya, panjang, c=[0,0,0,255]):
    pass
