#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda num : num**2, r)) for r in matrix]
