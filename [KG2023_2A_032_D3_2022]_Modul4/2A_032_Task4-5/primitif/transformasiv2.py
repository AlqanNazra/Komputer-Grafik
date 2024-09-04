import math
import numpy as np

def translate2D(tx, ty, tm = np.zeros(3)):
    # Matriks transformasi translasi
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    
    # Mengalikan matriks transformasi dengan matriks transformasi sebelumnya
    tm = np.dot(translation_matrix, tm)
    
    return tm

def reflectY2D(tm = np.zeros(3)):
    m = np.identity(3)
    m[0][0] =-1
    
    if(tm==0).all():
        return m
    return np.matmul(m,tm)

def scale2D(sx, sy, refx, refy, tm=np.zeros(3)):  
    # Matriks transformasi scaling
    scaling_matrix = np.array([[sx, 0, (1-sx) * refx],
                               [0, sy, (1-sy) * refy],
                               [0, 0, 1]])
    tm = np.dot(tm, scaling_matrix)
    return tm

def rotate2D(a, refx, refy):
    # Menghitung sudut dalam radian
    angle_rad = math.radians(a)
    rotation_matrix = np.array([[math.cos(angle_rad), -math.sin(angle_rad), refx * (1-math.cos(angle_rad)) + refy * math.sin(angle_rad)],
                                [math.sin(angle_rad), math.cos(angle_rad), refy * (1-math.cos(angle_rad)) - refx * math.sin(angle_rad)],
                                [0, 0, 1]])
    tm = rotation_matrix
    return tm


def transformPoints2D(pts, tm = np.zeros(3)):
    
    i, _ = pts.shape
    
    for k in range (i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp
    return pts

def shear2D(shx, shy, tm = np.zeros(3)):
    shear_matrix = np.array([[1, shx, 0],
                             [shy, 1, 0],
                             [0, 0, 1]])
    
    return np.dot(shear_matrix, tm)

def transformWithCenter(pts, a, b, transformation_func):
    # Translasi titik pusat ke (0, 0)
    tm = translate2D(-a, -b)
    
    # Terapkan transformasi
    tm = transformation_func(tm)
    
    # Translasi kembali ke titik semula
    tm = translate2D(a, b, tm)
    
    # Transformasikan titik-titik
    return transformPoints2D(pts, tm)