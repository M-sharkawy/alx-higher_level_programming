#!/usr/bin/python3

"""this module  divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    this function adds two integer or float numbers

    Args:
        matrix (int, float) : list of lists
        div (int, float) : number

    Returns:
        new matrix

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats") 

    for row in matrix:
        if type(row) != list or len(row) == 0:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")
            new_row.append(round(i / div, 2))

        new_matrix.append(new_row)

    return (new_matrix)
