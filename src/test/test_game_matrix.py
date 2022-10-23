from src.app.game_matrix import create_matrix


def test_create_matrix():
    for i in range(1, 10):
        for j in range(1, 10):
            matrix = create_matrix(i, j)
            assert len(matrix) == i
            for k in range(0, len(matrix)):
                assert len(matrix[k]) == j
                for m in range(0, len(matrix[k])):
                    assert not matrix[k][m]
