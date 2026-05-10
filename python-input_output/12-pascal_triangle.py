#!/usr/bin/python3
"""create Pascal's Triangle"""


def pascal_triangle(n):
    """create pascal's Triangle"""
    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            row = [1]

            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)
            triangle.append(row)
    return triangle
