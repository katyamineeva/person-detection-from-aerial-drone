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


def split_top_bottom(bg):
    h = bg.shape[0]
    w = bg.shape[1]
    h_mid = h // 2

    full_mask = np.full((h, w), True)

    top_mask = full_mask * (np.arange(h) < h_mid).reshape(h, -1)
    bottom_mask = full_mask * (np.arange(h) >= h_mid).reshape(h, -1)

    bg_top = bg[top_mask].reshape(h_mid, w, 3)
    bg_bottom = bg[bottom_mask].reshape(h - h_mid, w, 3)
    
    return [bg_top, bg_bottom]

def split_left_right(bg):
    h = bg.shape[0]
    w = bg.shape[1]
    w_mid = w // 2

    full_mask = np.full((h, w), True)

    left_mask = (full_mask.T * (np.arange(w) < w_mid).reshape(w, -1)).T
    right_mask = (full_mask.T * (np.arange(w) >= w_mid).reshape(w, -1)).T

    bg_left = bg[left_mask].reshape(h, w_mid, 3)
    bg_right = bg[right_mask].reshape(h, w - w_mid, 3)
    
    return [bg_left, bg_right]


def split_in_quarters(bg_path, output_path, bg_num):
    bg = skimage.io.imread(bg_path)[0]
    halfs = split_top_bottom(bg)
    quarters = split_left_right(halfs[0]) + split_left_right(halfs[1])
    for img in quarters:
        save_image(img, output_path, image_id2filename(bg_num))
        bg_num += 1
    return bg_num
