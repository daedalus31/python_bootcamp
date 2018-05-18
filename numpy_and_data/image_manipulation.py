import scipy.ndimage.interpolation

import numpy as np

import bmp


# image from: http://www.partow.net/programming/bitmap/images/tiger.bmp

def cut_out_image(pixel_matrix):
    pixels = pixel_matrix[120:354, 140:430]
    bmp.write_bmp('tiger_cut_out.bmp', pixels)


def single_color(pixel_matrix, color_index):
    mask = np.zeros(3)
    mask[color_index] = 1
    bmp.write_bmp('single_color.bmp', pixel_matrix * mask)


def rotate_image(pixel_matrix, degrees: float):
    bmp.write_bmp('rotated_tiger.bmp',
                  scipy.ndimage.interpolation.rotate(pixel_matrix, degrees, order=1))


def black_and_white(pixel_matrix):
    # can use also: scipy.ndimage.filters.gaussian_filter (see sigma param)
    sum_array = pixel_matrix.sum(axis=2, keepdims=True) / 3
    bmp.write_bmp('black_and_white_tiger.bmp', np.ones(3) * sum_array)


if __name__ == '__main__':
    pixels = bmp.read_bmp('tiger.bmp')

    cut_out_image(pixels)
    single_color(pixels, 1)
    rotate_image(pixels, -34.0)
    black_and_white(pixels)
