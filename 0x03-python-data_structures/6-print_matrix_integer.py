#!/usr/bin/python3
# author: sharkawy


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            print("{:d}".format(matrix[row][i]), end="")
            if i != (len(matrix[row]) - 1):
                print(" ", end="")
        print(" ")
