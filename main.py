from PIL import Image

"""This module needs to be a seperate thing from the main because well.... it handles grayscaling images and isn't part
 of the core program"""

# TODO: Port all this code to a new file, create its module and make it work with the actual program


def open_image(path):
    new_image = Image.open(path)
    return new_image


# Save Image
def save_image(image, path):
    image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image


# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


# Create a Grayscale version of the image
def convert_grayscale(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Transform to grayscale
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # Transform to grayscale using the formula (0.3 * R) + (0.59 * G) + (0.11 * B)
            gray = (red * 0.3) + (green * 0.59) + (blue * 0.11)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    # Return new image
    return new


if __name__ == '__main__':
    image_ = convert_grayscale(open_image('Pic0001.jpg'))
    save_image(image_, 'something.png')
