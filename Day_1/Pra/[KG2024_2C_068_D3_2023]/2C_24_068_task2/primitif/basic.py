import primitif.line
import py5

def draw_margin(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(10,10,790,10))
    py5.points(primitif.line.line_dda(10,10,10,590))
    py5.points(primitif.line.line_dda(10,590,790,590))
    py5.points(primitif.line.line_dda(790,590,790,10))

def draw_kartesian(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(10,300,790,300))
    py5.points(primitif.line.line_dda(400,10,400,590))
    
def draw_HP(width, height, margin,c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    
    py5.fill(0,113,45)
    py5.square(620, 150, 200)
    py5.rect(620,275, 130,50)
    
    py5.no_stroke()
    py5.fill(30,32,30)
    py5.square(570, 100, 50)
    py5.square(670, 100, 50)
    
    py5.fill(30,32,30)
    py5.rect(578, 210, 35, 81)
    py5.rect(662, 210, 35, 81)
    py5.rect(620,175, 50,100)
    

def draw_bob(width, height, margin, c=[0,0,0,255]):
    py5.fill(255, 255, 0) 
    py5.rect(200, 450, 150, 150)
    
    py5.fill(165, 42, 42)
    py5.rect(200, 500, 150, 50)
    
    py5.fill(255)
    py5.circle(150, 400, 35)
    py5.circle(250, 400, 35)
    
    py5.fill(255)
    py5.ellipse(200, 450, 55, 35)
    
    py5.fill(255, 0, 0)
    py5.triangle(175, 475, 200, 525, 225, 475)
    
    
def draw_freddy_fnaf(width, height, margin, c=[0,0,0,255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.no_stroke()
    py5.fill(145, 79, 30)
    py5.ellipse(200, 150, 250, 150)
    
    py5.fill(222, 172, 128)
    py5.circle(100, 75, 55)
    py5.circle(300, 75, 55)
    
    py5.fill(247, 220, 185)
    py5.circle(140, 125, 55)
    py5.circle(260, 125, 55)
    
    py5.fill(60, 61, 55)
    py5.triangle(170, 140, 230, 140, 200, 190)
    
    py5.fill(145, 79, 30)
    py5.ellipse(200, 260, 120, 70)