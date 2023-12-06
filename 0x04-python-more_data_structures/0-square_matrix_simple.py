#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    # Using map and lambda to create a new matrix with squared values
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
