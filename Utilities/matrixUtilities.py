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


# Load weights from a file
def load_weights(file):
    with open(file, 'r') as weights:
        weight_list = []
        for line in weights:
            weight_list.append(line.rstrip().split(','))

        return weight_list


# Convert a list of strings to list of ints
def convert_string_to_int(list_):
    for i in range(0, len(list_), 1):
        for j in range(0, len(list_[i]), 1):
            list_[i][j] = int(list_[i][j])
