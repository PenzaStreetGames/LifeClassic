from src.app.game_matrix import *


if __name__ == '__main__':
    game_matrix = Matrix.create(10, 10)
    game_matrix = Matrix.random_fill(game_matrix)
    print("Life Classic")
    Matrix.print(game_matrix)
