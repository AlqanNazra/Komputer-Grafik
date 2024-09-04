import py5
import primitif.line
import primitif.basic

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    py5.background(191)
    primitif.basic.draw_margin(py5.width, py5.height, 30, c=[0, 0, 0, 255])
    
    # Membuat garis-garis untuk papan Tic Tac Toe
    for i in range(1, 3):
        py5.points(primitif.line.line_bresenham(py5.width * i / 3, 30, py5.width * i / 3, py5.height - 30))
        py5.points(primitif.line.line_bresenham(30, py5.height * i / 3, py5.width - 30, py5.height * i / 3))
    
    # Menempatkan simbol "X" secara diagonal
    py5.stroke(0)
    py5.stroke_weight(4)
    py5.points(primitif.line.line_bresenham(30, 30, py5.width - 30, py5.height - 30))

def draw():
    pass

py5.run_sketch()
