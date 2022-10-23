def create_matrix(height, width):
    return [[0 for j in range(width)] for i in range(height)]


def print_matrix(matrix):
    symbol_matrix = list(list("*" if cell else "." for cell in line) for line in matrix)
    print("\n".join("".join(line) for line in symbol_matrix))
