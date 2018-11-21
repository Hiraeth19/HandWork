from Utilities.imageUtilities import convert_grayscale, open_image
from Utilities.matrixUtilities import list_to_matrix, load_weights, multiply_matrices, convert_string_to_int, sigmoid


# TODO: Back Propagation
# Main function
if __name__ == '__main__':
    # Open the file and create an array with its grayscale values
    image_map = convert_grayscale(open_image('nine.png'))
    # Create the layer 1 neurons using the array
    layer1 = list_to_matrix(image_map)

    # Load the weights from a file and convert into a matrixx
    weights1 = load_weights('Weights/weights1.txt')
    convert_string_to_int(weights1)
    weights1 = list_to_matrix(weights1)

    # Create the second layer activation neurons by multiplying the weights and the activations
    layer2 = multiply_matrices(weights1, layer1)

    # Load the second weights from a file and convert into a matrix
    weights2 = load_weights('Weights/weights2.txt')
    convert_string_to_int(weights2)
    weights2 = list_to_matrix(weights2)

    # Create the third layer activation neurons by multiplying the weights and activation
    layer3 = multiply_matrices(weights2, layer2)

    # Load the third weights from a file and convert into a matrix
    weights3 = load_weights('Weights/weights3.txt')
    convert_string_to_int(weights3)
    weights3 = list_to_matrix(weights3)

    # Create the output layer by multiplying the weights and activations
    output = multiply_matrices(weights3, layer3)

    print(sigmoid(0))
