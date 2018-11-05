import numpy
# Matrix processing module


# Multiply two matrices
def multiply_matrices(x, y):
    new = numpy.dot(x, y)
    return new


# Convert a list to a matrix
def list_to_matrix(list_):
    new = numpy.array(list_)
    return new
