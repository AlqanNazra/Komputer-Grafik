import py5
import primitif.line
import primitif.basic
import primitif.utility
import math
import config

w, h, r = (py5.width, py5.height, 200)
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

turn = 1
game_over = False
mode = 1


def zero_sign(x, y, r):
    primitif.basic.lingkaran(x, y, r / 2)


def x_sign(x, y, r):
    primitif.basic.kali(x, y, r)


def draw_xoxBoard():
    for y in range(3):
        for x in range(3):
            primitif.basic.persegi(r * x, r * y, r)


def draw_player():
    for y in range(3):
        for x in range(3):
            if grid[y][x] == 2:
                zero_sign(x * r + r / 2, y * r + r / 2, r)
            elif grid[y][x] == 1:
                x_sign(x * r, y * r, r)


def switch_turns():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1


def find_winners():
    for y in range(3):
        if grid[y][0] == grid[y][1] == grid[y][2] != 0:
            return grid[y][0]
    for x in range(3):
        if grid[0][x] == grid[1][x] == grid[2][x] != 0:
            return grid[0][x]
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    return None


def find_draw():
    # Cek jika ada pemenang
    if find_winners() is not None:
        return False

    # Cek apakah seluruh grid sudah terisi
    for row in grid:
        if 0 in row:  # Jika ada elemen yang bernilai 0, permainan belum selesai
            return False

    # Jika grid penuh dan tidak ada pemenang, return True sebagai draw
    return True


def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)


def draw():
    global mode
    py5.background(200)

    if mode == 1:
        py5.fill(255)

        draw_xoxBoard()
        draw_player()

        if find_winners() is not None:
            mode = 2
        elif find_draw():  # Periksa apakah permainan seri
            mode = 3

    elif mode == 2:
        py5.fill(100)
        py5.text(f"game over, player {find_winners()} Win", 200, 200)
    elif mode == 3:
        py5.fill(100)
        py5.text("game over, DRAW", 200, 200)


def mouse_pressed():
    global mode, grid
    if mode == 1:
        if py5.mouse_x < 3 * r:
            if grid[py5.mouse_y // 200][py5.mouse_x // 200] == 0:
                grid[py5.mouse_y // 200][py5.mouse_x // 200] = turn
                print(f"({py5.mouse_x // 200}, {py5.mouse_y // 200})")
                switch_turns()
    elif mode in [2, 3]:
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        mode = 1


py5.run_sketch()
