import random

class Cell:
  def __init__(catur, x, y):
    catur.x = x
    catur.y = y
    catur.value = 0  

class Caturjawir:
  def __init__(catur):
    catur.grid = [[Cell(x, y) for x in range(3)] for y in range(3)]
    catur.turn = 1  
    catur.game_over = False
    catur.mode = 1  

  def Caturjawir(catur):
    for row in catur.grid:
      for cell in row:
        print(cell.value, end=" ")
      print()

  def is_valid_move(catur, x, y):
    return catur.grid[y][x].value == 0

  def make_move(catur, x, y):
    if catur.is_valid_move(x, y):
      catur.grid[y][x].value = catur.turn
      catur.switch_turns()

  def switch_turns(catur):
    catur.turn = 3 - catur.turn

  def check_winner(catur):
    for i in range(3):
      if catur.grid[i][0].value == catur.grid[i][1].value == catur.grid[i][2].value != 0:
        return catur.grid[i][0].value
      if catur.grid[0][i].value == catur.grid[1][i].value == catur.grid[2][i].value != 0:
        return catur.grid[0][i].value
    if catur.grid[0][0].value == catur.grid[1][1].value == catur.grid[2][2].value != 0:
      return catur.grid[0][0].value
    if catur.grid[0][2].value == catur.grid[1][1].value == catur.grid[2][0].value != 0:
      return catur.grid[0][2].value
    return None

  def is_draw(catur):
    for row in catur.grid:
      for cell in row:
        if cell.value == 0:
          return False
    return True

  def ai_move(catur):

    empty_cells = []
    for y in range(3):
      for x in range(3):
        if catur.grid[y][x].value == 0:
          empty_cells.append((x, y))  
    if empty_cells:
      print("\n^^^ Pergerakan AI ^^^")
      index = random.randint(0, len(empty_cells) - 1)
      x, y = empty_cells[index]  
      catur.make_move(x, y)
      

  def play_game(catur):
    while not catur.game_over:
      catur.Caturjawir()
      if catur.turn == 1:
        print("\nPastikan mengisian memiliki range dari 0-2 bila lebih maka akan error")
        print("\nKamu itu 1 dan AI adalah 2")
        x, y = map(int, input("Masukkan Koordinat Catur Jawa (x, y): ").split())
        if catur.is_valid_move(x, y):
          catur.make_move(x, y)
        else:
          print("Input salah. Coba lagi.")
      else:
        catur.ai_move()

      winner = catur.check_winner()
      if winner:
        catur.game_over = True
        print(f"Player {winner} Wins!")
      elif catur.is_draw():
        catur.game_over = True
        print("Game Draw!")

game = Caturjawir()
game.play_game()