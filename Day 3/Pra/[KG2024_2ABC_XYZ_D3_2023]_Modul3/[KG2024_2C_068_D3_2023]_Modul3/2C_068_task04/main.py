import py5
import primitif.line
import primitif.basic
import primitif.utility
import config

class ShapeDrawer:
    def __init__(self, margin, color):
        self.margin = margin
        self.color = color

    def draw_margin(self, width, height):
        py5.stroke(*self.color)
        self.draw_bentuk(primitif.line.line_dda(self.margin, self.margin, width - self.margin, self.margin))
        self.draw_bentuk(primitif.line.line_dda(self.margin, height - self.margin, width - self.margin, height - self.margin))
        self.draw_bentuk(primitif.line.line_dda(self.margin, self.margin, self.margin, height - self.margin))
        self.draw_bentuk(primitif.line.line_dda(width - self.margin, self.margin, width - self.margin, height - self.margin))

    def draw_grid(self, width, height):
        xa = self.margin
        ya = 2 * self.margin
        xb = width - xa
        yb = height - ya
        y_range = height / self.margin
        
        py5.stroke(*self.color)
        for _ in range(1, int(y_range)):
            self.draw_bentuk(primitif.line.line_dda(xa, ya, xb, ya))
            ya += self.margin

        xa = 2 * self.margin
        ya = self.margin
        xb = width - xa
        yb = height - ya
        x_range = width / self.margin
        for _ in range(1, int(x_range)):
            self.draw_bentuk(primitif.line.line_dda(xa, ya, xa, yb))
            xa += self.margin

    def draw_kartesian(self, width, height):
        py5.stroke(*self.color)
        self.draw_bentuk(primitif.line.line_dda(width / 2, self.margin, width / 2, height - self.margin))
        self.draw_bentuk(primitif.line.line_dda(self.margin, height / 2, width - self.margin, height / 2))

    def draw_bentuk(self, pts):
        for pt in pts:
            py5.point(pt[0], pt[1])

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)

def draw():
    width = 800
    height = 600
    py5.background(191)
    color = [0, 0, 0, 255]
    margin = 25
    drawer = ShapeDrawer(margin, color)
    drawer.draw_margin(width, height)
    drawer.draw_kartesian(width, height)
    
    half_width = width // 2
    half_height = height // 2


    if config.anim <= 3 * config.times:
        primitif.basic.persegi(6 * half_width // 4, half_height // 2, 100, c=[255, 0, 0, 255]) # 1
        primitif.basic.persegi_2(half_width // 2, half_height // 2, 100, c=[255, 0, 0, 255]) # 2
        primitif.basic.persegi_3(half_width // 2, 3 * half_height // 2, 100, c=[255, 0, 0, 255]) # 3
        primitif.basic.persegi_4(6 * half_width // 4, 3 * half_height // 2, 100, c=[255, 0, 0, 255]) # 4
    
    elif config.anim <= 6 * config.times:
        primitif.basic.persegi_panjang(6 * half_width // 4, half_height // 2, 200, 100, c=[255, 0, 0, 255]) # 1
        primitif.basic.persegi_panjang_2(half_width // 2, half_height // 2, 200, 100, c=[255, 0, 0, 255]) # 2
        primitif.basic.persegi_panjang_3(half_width // 2, 3 * half_height // 2, 200, 100, c=[255, 0, 0, 255]) # 3
        primitif.basic.persegi_panjang_4(6 * half_width // 4, 3 * half_height // 2, 200, 100, c=[255, 0, 0, 255]) # 4
    
    elif config.anim <= 9 * config.times:
        primitif.basic.segitiga_siku(6 * half_width // 4, half_height // 2, 50, 100) # Kuadran 1
        primitif.basic.segitiga_siku_2(half_width // 2, half_height // 2, 50, 100) # Kuadran 2
        primitif.basic.segitiga_siku_3(half_width // 2, 3 * half_height // 2, 50, 100) # Kuadran 3
        primitif.basic.segitiga_siku_4(6 * half_width // 4, 3 * half_height // 2, 50, 100) # Kuadran 4
    
    elif config.anim <= 12 * config.times:
        primitif.basic.trapesium_siku(6 * half_width // 4, half_height // 2, 100, 200, 100) # 1
        primitif.basic.trapesium_siku_2(half_width // 2, half_height // 2, 100, 200, 100) # 2
        primitif.basic.trapesium_siku_3(half_width // 2, 3 * half_height // 2, 100, 200, 100) # 3
        primitif.basic.trapesium_siku_4(6 * half_width // 4, 3 * half_height // 2, 100, 200, 100) # 4

    
    if config.anim > 13 * config.times:
        config.anim = 0

    config.anim += 1

py5.run_sketch()
