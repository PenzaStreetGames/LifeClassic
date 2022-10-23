import pytest

from src.app.game_matrix import Matrix


def test_create_matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            assert len(matrix) == i
            for k in range(0, len(matrix)):
                assert len(matrix[k]) == j
                for m in range(0, len(matrix[k])):
                    assert not matrix[k][m]


def test_set_cell():
    matrix = Matrix.create(10, 10)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix = Matrix.set_cell(matrix, i, j, True)
            for k in range(len(matrix)):
                for m in range(len(matrix[k])):
                    assert (
                        matrix[k][m] and k == i and m == j
                        or
                        not matrix[k][m] and (k != i or m != j)
                    )
            matrix = Matrix.set_cell(matrix, i, j, False)


def test_str_matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            for k in range(0, len(matrix)):
                for m in range(0, len(matrix[k])):
                    if (k + m) % 3 == 0:
                        matrix = Matrix.set_cell(matrix, k, m, True)
            matrix_str = Matrix.str(matrix)
            for k in range(0, len(matrix)):
                for m in range(0, len(matrix[k])):
                    assert (
                        matrix[k][m] and matrix_str[k * (j + 1) + m] == Matrix.ALIVE_CHAR
                        or
                        not matrix[k][m] and matrix_str[k * (j + 1) + m] == Matrix.DEAD_CHAR
                    )
