import py5
import primitif.line
import primitif.basic
import math
from random import randint

def car(car_topx, car_topy):
    # body
    car_length = 100
    car_height = 40
    roof_height = 20
    tire_size = 20
    py5.fill(250, 0, 0)
    py5.rect(car_topx, car_topy, car_length, car_height)
    py5.quad(
        car_topx+roof_height, car_topy
        , car_topx+(2*roof_height), car_topy-roof_height
        , car_topx+(car_length-roof_height), car_topy-roof_height
        , car_topx+(car_length-roof_height), car_topy
    )
    py5.ellipse(car_topx+20, car_topy+car_height, tire_size, tire_size)
    py5.ellipse(car_topx+car_length-20, car_topy+car_height, tire_size, tire_size)

def drawCars(w):
    for x in range(50, w, 110):
        car(x, 100)

def setup():
    py5.size(750,750)
    w,h,m = (py5.width, py5.height, 10)
    drawCars(w)

def draw():
    pass

py5.run_sketch()


