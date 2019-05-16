import os
import sys
import random
import math
import numpy as np
from numpy.random import randint
import skimage.io
from skimage import img_as_float, img_as_uint, img_as_int
import matplotlib
import matplotlib.pyplot as plt
import itertools
import logging
import json
import re
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
import matplotlib.image as mpimg
from matplotlib.patches import Polygon
import pickle
import shutil
from IPython.display import clear_output
import csv

sys.path.append('/content/drive/My Drive/project')
from utils_main_project.global_constants import *


def display_image(image):
    _, ax = plt.subplots(1, figsize=(12, 12))
    height, width = image.shape[:2]
    ax.set_ylim(height + 10, -10)
    ax.set_xlim(-10, width + 10)
    ax.axis('off')
    ax.imshow(image)
    plt.show()


def draw_rectangles(background_shape, rectangles):
    rectangles_num = len(rectangles)
    fig,ax = plt.subplots(1)
    
    background = np.full((background_shape[0], background_shape[1], 3), fill_value=0)
    ax.imshow(background)
        
    r_colors = ['red'] * rectangles_num
    for i in range(min(rectangles_num, len(NAMED_COLORS))):
        r_colors[i] = NAMED_COLORS[i]
    
    for ind, rect in enumerate(rectangles):
        i, j = rect[0], rect[1]
        h = rect[2] - rect[0]
        w = rect[3] - rect[1]
        rect_img = patches.Rectangle((j, i), w, h, linewidth=1,edgecolor=r_colors[ind],facecolor='none')
        ax.add_patch(rect_img)
    plt.show()

def print_list(arr):
    format_string = "{: 5}" * len(arr)
    print(format_string.format(*arr))
    
def print_matrix(matrix):
    for row in matrix:
        print_list(row)
