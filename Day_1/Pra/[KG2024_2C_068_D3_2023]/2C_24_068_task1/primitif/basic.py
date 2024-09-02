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