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
from utils_main_project.local_paths import *

def mask_id2filename(id):
    return "mask_" + str(id)

def image_id2filename(id):
    return str(id) + '.jpg'

def image_filename2id(filename):
    return int(filename.split('.')[0])

def image2mask_filename(img_filename):
    return mask_id2filename(image_filename2id(img_filename))

def save_image(image, output_path, filename):
    image_path = os.path.join(output_path, filename)
    skimage.io.imsave(image_path, image)

def image_ids_list(path):
    if os.path.exists(path + '/images'):
        path = os.path.join(path, 'images')
    ids = [image_filename2id(f) for f in get_filenames_list(path)]
    ids.sort()
    return ids

def save_object_pickle(obj, output_path, filename):
    obj_path = os.path.join(output_path, filename)
    with open(obj_path, 'wb') as file:                    
        pickle.dump(obj, file)
        
def load_object_pickle(obj_path):
    with open(obj_path, 'rb') as file:
        return pickle.load(file)

def encode_bboxes(bboxes):
    format_str = '_'.join(['{}-{}-{}-{}'] * bboxes.shape[0])
    bboxes_str = format_str.format(*bboxes.reshape(-1))
    return bboxes_str
    
def save_bboxes(bboxes, output_path, image_id):
    bboxes_path = output_path + '/bboxes.csv'
    file = open(bboxes_path, 'a+')
    w = csv.writer(file)
    bboxes_str = encode_bboxes(bboxes)
    w.writerow([str(image_id), bboxes_str])
    file.close()

def decode_bboxes(str):
    bboxes = [[int(n) for n in s.split('-')] for s in str.split('_')]
    return np.array(bboxes)
    
def load_bboxes(path):
    bboxes_path = os.path.join(path, 'bboxes.csv')
    with open(bboxes_path, mode='r') as file:
        reader = csv.reader(file)
        d = {int(rows[0]) : decode_bboxes(rows[1]) for rows in reader}
    return d


def get_images_n_masks(path, return_val, return_iterator=False, ids=None):
    assert (return_val in ['paths', 'objects'])
    images_path = os.path.join(path, 'images/')
    masks_path = os.path.join(path, 'masks/')
    
    if ids == None:
        ids = image_ids_list(path)
    ids.sort()

    images_paths = [os.path.join(images_path, image_id2filename(id)) for id in ids]
    masks_paths = [os.path.join(masks_path, mask_id2filename(id)) for id in ids]
    
    if return_val == 'paths':
        if return_iterator:
            return zip(images_paths, masks_paths)
        else:
            return images_paths, masks_paths
    
    images = [skimage.io.imread(path) for path in images_paths]
    masks = [load_object_pickle(path) for path in masks_paths]
    if return_iterator:
        return zip(images, masks)
    return images, masks

def get_ids_n_images(path, return_val='paths', ids=None):
    assert (return_val in ['paths', 'objects'])
    images_path = os.path.join(path, 'images')
    
    if ids == None:
        ids = image_ids_list(images_path)
    ids.sort()
    images_paths = [os.path.join(images_path, image_id2filename(id)) for id in ids]
    if return_val == 'paths':
        return zip(ids, images_paths)
    return ((id, skimage.io.imread(img_path)) for (id, img_path) in zip(ids, images_paths))
