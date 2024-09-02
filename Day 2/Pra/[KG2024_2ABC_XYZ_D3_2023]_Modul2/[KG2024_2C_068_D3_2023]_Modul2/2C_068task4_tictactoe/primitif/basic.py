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
    py5.points(primitif.line.line_dda(2 * width/3,margin,2 * width/3,height-margin))
    py5.points(primitif.line.line_dda(width/3,margin,width/3,height-margin))
    py5.points(primitif.line.line_bresenham(margin,height/3,width - margin,height/3))
    py5.points(primitif.line.line_bresenham(margin,2 * height/3,width,2 * height/3))
    
def draw_X(width, height, margin, c=[0,0,0,255]):
    yok = height/2
    koy = width/2
    
    toy = width/3
    woy = height/3 
    
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_bresenham(9 * koy/5,6 * yok/10,6 * koy/4,2 * yok/10))
    py5.points(primitif.line.line_bresenham(6 * koy/4,6 * yok/10,9 * koy/5,2 * yok/10))
    
    py5.points(primitif.line.line_bresenham(50 + toy,(2 * woy) - 50 ,(2* toy)- 50 ,50 + woy))
    py5.points(primitif.line.line_bresenham((2* toy)- 50,(2 * woy) - 50 ,50 + toy,50 + woy))
    
    py5.points(primitif.line.line_bresenham(width/8,50+(5 * yok/3),width/4,3 * yok/2))
    py5.points(primitif.line.line_bresenham(width/8,3 * yok/2,width/4,50+(5 * yok/3)))
    
    
def draw_kotaktengah(width, height, margin, c=[0,0,0,255]):
    yok = height/2
    koy = width/2
    
    toy = width/3
    woy = height/3 
    
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda((2* toy)- 50,6 * yok/10,50 + toy,6 * yok/10))
    py5.points(primitif.line.line_dda((2* toy)- 50,2 * yok/10,50 + toy,2 * yok/10))
    py5.points(primitif.line.line_dda((2* toy)- 50,2 * yok/10,(2* toy)- 50,6 * yok/10))
    py5.points(primitif.line.line_dda(50 + toy,2 * yok/10,50 + toy,6 * yok/10))
    
    py5.points(primitif.line.line_dda((2* toy)- 50,3 * yok/2,50 + toy,3 * yok/2))
    py5.points(primitif.line.line_dda((2* toy)- 50,50 + (5 * yok/3),50 + toy,50 + (5 * yok/3)))
    py5.points(primitif.line.line_dda((2* toy)- 50,3 * yok/2,(2* toy)- 50,50 + (5 * yok/3)))
    py5.points(primitif.line.line_dda(50 + toy,50 + (5 * yok/3),50 + toy,3 * yok/2))

def draw_kotakakhir(width, height, margin, c=[0,0,0,255]):
    yok = height/2
    koy = width/2
    
    toy = width/3
    woy = height/3 
    
    py5.stroke(c[0], c[1], c[2], c[3])
    
    py5.points(primitif.line.line_bresenham(50 + toy,(2 * woy) - 50 ,(2* toy)- 50 ,50 + woy))
    py5.points(primitif.line.line_bresenham((2* toy)- 50,(2 * woy) - 50 ,50 + toy,50 + woy))
    
    py5.points(primitif.line.line_dda(9 * koy/5,(2 * woy) - 50 ,9 * koy/5,50 + woy))
    py5.points(primitif.line.line_dda(9 * koy/5,50 + woy,6  * koy/4,50 + woy))
    py5.points(primitif.line.line_dda(6  * koy/4,(2 * woy) - 50 ,6  * koy/4,50 + woy))
    py5.points(primitif.line.line_dda(9 * koy/5,(2 * woy) - 50,6  * koy/4,(2 * woy) - 50))
    
    
    py5.points(primitif.line.line_dda(9 * koy/5,50 + (5 * yok/3),9 * koy/5,3 * yok/2))
    py5.points(primitif.line.line_dda(9 * koy/5,50+(5 * yok/3),6  * koy/4,50+(5 * yok/3)))
    py5.points(primitif.line.line_dda(6  * koy/4,50 + (5 * yok/3),6  * koy/4,3 * yok/2))
    py5.points(primitif.line.line_dda(9 * koy/5,3 * yok/2,6  * koy/4,3 * yok/2))
    
def draw_kotakawal(width, height, margin, c=[0,0,0,255]):
    yok = height/2
    koy = width/2
    
    toy = width/3
    woy = height/3 
    
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/4,6 * yok/10,width/8,6 * yok/10))
    py5.points(primitif.line.line_dda(width/8,2 * yok/10,width/4,2 * yok/10))
    py5.points(primitif.line.line_dda(width/8,2 * yok/10,width/8,6 * yok/10))
    py5.points(primitif.line.line_dda(width/4,2 * yok/10,width/4,6 * yok/10))
    
    py5.points(primitif.line.line_dda(width/4,(2 * woy) - 50 ,width/4,50 + woy))
    py5.points(primitif.line.line_dda(width/4,50 + woy,width/8,50 + woy))
    py5.points(primitif.line.line_dda(width/8,(2 * woy) - 50 ,width/8,50 + woy))
    py5.points(primitif.line.line_dda(width/4,(2 * woy) - 50,width/8,(2 * woy) - 50))
    
    
