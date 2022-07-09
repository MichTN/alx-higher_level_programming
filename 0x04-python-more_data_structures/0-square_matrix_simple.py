#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = []  
    for i in matrix:
        matrix.append(list(map(lambda x: x ** 2, i)))
    return matrix
