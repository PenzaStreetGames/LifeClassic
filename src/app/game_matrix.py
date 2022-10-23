import random


class Matrix:
    ALIVE_CHAR = "O"
    DEAD_CHAR = "."

    @staticmethod
    def create(height, width):
        return [[False for j in range(width)] for i in range(height)]

    @staticmethod
    def set_cell(matrix, row, col, val):
        matrix[row][col] = val
        return matrix

    @staticmethod
    def clear(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix = Matrix.set_cell(matrix, i, j, False)
        return matrix


    @staticmethod
    def print(matrix):
        print(Matrix.str(matrix))

    @staticmethod
    def str(matrix):
        symbol_matrix = list(list(Matrix.ALIVE_CHAR if cell else Matrix.DEAD_CHAR for cell in line) for line in matrix)
        result = "\n".join("".join(line) for line in symbol_matrix)
        return result

    @staticmethod
    def random_fill(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = True if random.random() > 0.5 else False
                Matrix.set_cell(matrix, i, j, val)
        return matrix


