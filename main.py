from Utilities.imageUtilities import convert_grayscale, open_image
from Utilities.matrixUtilities import list_to_matrix, load_weights, multiply_matrices, convert_string_to_int
import numpy


# TODO: The entire program needs to be tied together with the weights and biases
if __name__ == '__main__':
    image_map = convert_grayscale(open_image('nine.png'))
    matrix = list_to_matrix(image_map)

    weights1 = load_weights('weights1.txt')
    convert_string_to_int(weights1)
    weights1 = list_to_matrix(weights1)

    layer2 = multiply_matrices(weights1, matrix)

    print(len(layer2))
