from Utilities.imageUtilities import convert_grayscale, open_image
from Utilities.matrixUtilities import list_to_matrix


# TODO: The entire program needs to be tied together with the weights and biases
if __name__ == '__main__':
    image = convert_grayscale(open_image('nine.png'))
    print(len(image))
    matrix = list_to_matrix(image)
    print(matrix)
