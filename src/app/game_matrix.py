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

    @staticmethod
    def alive_neighbours_count(matrix, row, col):
        height, width = len(matrix), len(matrix[0])
        height_from = max(row - 1, 0)
        height_to = min(row + 1, height - 1)
        width_from = max(col - 1, 0)
        width_to = min(col + 1, width - 1)
        result = 0
        for i in range(height_from, height_to + 1):
            for j in range(width_from, width_to + 1):
                if i != row or j != col:
                    result += matrix[i][j]
        return result

    @staticmethod
    def next_epoch_cell(matrix, row, col):
        n = Matrix.alive_neighbours_count(matrix, row, col)
        result = False
        if matrix[row][col]:
            if n in {2, 3}:
                result = True
        else:
            if n == 3:
                result = True
        return result

    @staticmethod
    def next_epoch(matrix):
        width, height = len(matrix), len(matrix[0])
        new_matrix = Matrix.create(width, height)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                alive = Matrix.next_epoch_cell(matrix, i, j)
                new_matrix[i][j] = alive
        return new_matrix


