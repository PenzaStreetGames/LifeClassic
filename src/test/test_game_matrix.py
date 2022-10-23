import random

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
            for k in range(len(matrix)):
                for m in range(len(matrix[k])):
                    if (k + m) % 3 == 0:
                        matrix = Matrix.set_cell(matrix, k, m, True)
            matrix_str = Matrix.str(matrix)
            for k in range(len(matrix)):
                for m in range(len(matrix[k])):
                    assert (
                        matrix[k][m] and matrix_str[k * (j + 1) + m] == Matrix.ALIVE_CHAR
                        or
                        not matrix[k][m] and matrix_str[k * (j + 1) + m] == Matrix.DEAD_CHAR
                    )


def test_random_fill():
    correct_values = {True, False}
    for i in range(1, 10):
        for j in range(1, 10):
            matrix_1 = Matrix.create(i, j)
            matrix_2 = Matrix.create(i, j)
            random.seed(42)
            matrix_1 = Matrix.random_fill(matrix_1)
            random.seed(42)
            matrix_2 = Matrix.random_fill(matrix_2)
            for k in range(i):
                for m in range(j):
                    assert matrix_1[k][m] == matrix_2[k][m]
                    assert matrix_1[k][m] in correct_values


def test_clear_matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            matrix = Matrix.random_fill(matrix)
            matrix = Matrix.clear(matrix)
            for k in range(i):
                for m in range(j):
                    assert not matrix[k][m]


def test_alive_neighbours_count():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            for k in range(i):
                for m in range(j):
                    assert Matrix.alive_neighbours_count(matrix, k, m) == 0
            for k in range(i):
                for m in range(j):
                    matrix = Matrix.set_cell(matrix, k, m, True)
            corners = {(0, 0), (0, j - 1), (i - 1, 0), (i - 1, j - 1)}
            borders = {
                (y, 0) for y in range(1, i - 1)
            } | {
                (0, x) for x in range(1, j - 1)
            } | {
                (y, j - 1) for y in range(1, i - 1)
            } | {
                (i - 1, x) for x in range(1, j - 1)
            }
            center = {*((y, x) for y in range(1, i - 1) for x in range(1, j - 1))}
            for k in range(i):
                for m in range(j):
                    n = Matrix.alive_neighbours_count(matrix, k, m)
                    cell = (k, m)
                    assert cell in (corners | borders | center)
                    if i == 1 and j == 1:
                        assert n == 0
                    elif i == 1 or j == 1:
                        assert cell in (corners | borders)
                        if cell in corners:
                            assert n == 1
                        elif cell in borders:
                            assert n == 2
                    elif cell in corners:
                        assert n == 3
                    elif cell in borders:
                        assert n == 5
                    elif cell in center:
                        assert n == 8


def test_next_epoch_cell():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            for k in range(i):
                for m in range(j):
                    n = Matrix.alive_neighbours_count(matrix, k, m)
                    alive = Matrix.next_epoch_cell(matrix, k, m)
                    assert (
                            (2 <= n <= 3) and alive
                            or
                            (n < 2 or n > 3) and not alive
                    )


def test_next_epoch():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = Matrix.create(i, j)
            next_matrix = Matrix.next_epoch(matrix)
            for k in range(i):
                for m in range(j):
                    alive = Matrix.next_epoch_cell(matrix, k, m)
                    assert alive == next_matrix[k][m]
