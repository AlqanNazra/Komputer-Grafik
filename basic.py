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
    x = xa - (panjang // 2)
    y = ya - (panjang // 2)
    
    py5.points(primitif.line.line_bresenham(x,y,x+panjang,y))
    py5.points(primitif.line.line_bresenham(x+panjang,y,x+panjang,y+panjang))
    py5.points(primitif.line.line_bresenham(x+panjang,y+panjang,x,y+panjang))
    py5.points(primitif.line.line_bresenham(x,y+panjang,x,y))
    pass

def persegi_panjang(xa, ya, panjang, lebar, c=[0,0,0,255]):
    x = xa - (panjang // 2)
    y = ya - (lebar // 2)
    
    py5.points(primitif.line.line_bresenham(x,y,x+panjang,y))
    py5.points(primitif.line.line_bresenham(x+panjang,y,x+panjang,y+lebar))
    py5.points(primitif.line.line_bresenham(x+panjang,y+lebar,x,y+lebar))
    py5.points(primitif.line.line_bresenham(x,y+lebar,x,y))
    pass

def segitiga_siku(xa, ya, alas, tinggi, c=[0,0,0,255]):
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    py5.points(primitif.line.line_bresenham(x,y,x+alas,y+tinggi))
    py5.points(primitif.line.line_bresenham(x+alas,y+tinggi,x,y+tinggi))
    py5.points(primitif.line.line_bresenham(x,y+tinggi,x,y))
    pass

def segitiga_siku_titik(xa, ya, alas, tinggi,dash_length, gap_length,c=[0,0,0,255]):
    x = xa - alas // 2
    y = ya - tinggi // 2
    
    py5.points(primitif.line.line_bresenham(x,y,x+alas,y+tinggi))
    py5.points(primitif.line.line_bresenham(x+alas,y+tinggi,x,y+tinggi))
    py5.points(primitif.line.line_bresenham(x,y+tinggi,x,y))
    dash_capstyle='round'

def trapesium_siku(xa, ya, aa, ab, tinggi, c=[0,0,0,255]):
    x = xa - ab // 2
    y = ya - tinggi // 2
    
    py5.points(primitif.line.line_bresenham(x,y,x+aa,y))
    py5.points(primitif.line.line_bresenham(x+aa,y,x+ab,y+tinggi))
    py5.points(primitif.line.line_bresenham(x+ab,y+tinggi,x,y+tinggi))
    py5.points(primitif.line.line_bresenham(x,y+tinggi,x,y))
    pass

def kali(xa, ya, panjang, c=[0,0,0,255]):
    
    pass


def draw_styled_line(xa, y1, x2, y2, dash_length, gap_length):
    # Menghitung panjang total garis
    total_length = py5.dist(xa, y1, x2, y2)
    # Menghitung jumlah segmen
    segment_count = int(total_length / (dash_length + gap_length))
    
    # Menghitung posisi tiap segmen
    for i in range(segment_count):
        start_x = py5.lerp(xa, x2, i * (dash_length + gap_length) / total_length)
        start_y = py5.lerp(y1, y2, i * (dash_length + gap_length) / total_length)
        end_x = py5.lerp(xa, x2, (i * (dash_length + gap_length) + dash_length) / total_length)
        end_y = py5.lerp(y1, y2, (i * (dash_length + gap_length) + dash_length) / total_length)
        py5.line(start_x, start_y, end_x, end_y)