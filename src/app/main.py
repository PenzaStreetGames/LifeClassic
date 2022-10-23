from src.app.game_matrix import *


if __name__ == '__main__':
    game_matrix = Matrix.create(10, 10)
    print("Life Classic")
    Matrix.print(game_matrix)
