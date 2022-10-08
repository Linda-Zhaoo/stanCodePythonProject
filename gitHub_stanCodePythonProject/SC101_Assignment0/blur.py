"""
File: blur.py
Name: Linda Zhao
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original picture
    :return: new_img. the picture get blurred
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x, y)
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= (x+i) < img.width and 0 <= (y+j) < img.height:
                        red_sum += img.get_pixel(x+i, y+j).red
                        green_sum += img.get_pixel(x+i, y+j).green
                        blue_sum += img.get_pixel(x+i, y+j).blue
                        count += 1
            new_img_pixel.red = red_sum / count
            new_img_pixel.green = green_sum / count
            new_img_pixel.blue = blue_sum / count
    return new_img


def main():
    """
    input the original picture, the picture will transfer to function blur to deal with.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
