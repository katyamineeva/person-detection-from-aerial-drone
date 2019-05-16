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


def get_subdirs_list(dir_path):
    return next(os.walk(dir_path))[1]

def get_subdirs_paths_list(dir_path):
    return [os.path.join(dir_path, subdir_name) for subdir_name in get_subdirs_list(dir_path)]

def get_filenames_list(dir_path):
    return next(os.walk(dir_path))[2]

def get_files_paths_list(dir_path):
    return [os.path.join(dir_path, filename) for filename in get_filenames_list(dir_path)]

def get_paths_list_by_filenames(dir_path, filenames):
    return [os.path.join(dir_path, filename) for filename in filenames]


def add_subdirs_paths_to_list(l, dir_path):
    def get_key_n_path(subdir_name):
        path =  os.path.join(dir_path, subdir_name)
        return (subdir_name, path)
    l += [get_key_n_path(subdir_name) for subdir_name in get_subdirs_list(dir_path)]

def add_subsubdirs_paths_to_list(l, dir_path):
    for subdir_name in get_subdirs_list(dir_path):
        subdir_path = os.path.join(dir_path, subdir_name)
        def get_key_n_path(subsubdir_name):
            key = subdir_name + '_' + subsubdir_name
            path = os.path.join(subdir_path, subsubdir_name)
            return (key, path)
        l += [get_key_n_path(ssdir_name) for ssdir_name in get_subdirs_list(subdir_path)]
    
def add_subdirs_paths_to_dict(d, dir_path):
    for subdir_name in get_subdirs_list(dir_path):
        d[subdir_name] = os.path.join(dir_path, subdir_name)
        
def get_sample_data_paths():
    d = dict()
    d['sample_data'] = os.path.join(paths['project'], 'sample_data')
    add_subdirs_paths_to_dict(d, d['sample_data'])
    return d

# def get_paths_old():
#     paths_list = []
    
#     project_root = '/content/drive/My Drive/project/'
    
#     datasets_root = os.path.join(project_root, 'datasets/')
#     models_root = os.path.join(project_root, 'models')
#     metrics_root = os.path.join(models_root, 'metrics')
#     mrcnn_root = os.path.join(models_root, 'mask-rcnn-tf/')
#     retinanet_root = os.path.join(models_root, 'retinanet-tf/')
    
#     paths_list.append(('project_root', project_root))
#     paths_list.append(('datasets_root', datasets_root))
#     paths_list.append(('metrics_root', metrics_root))

#     paths_list.append(('mrcnn_root', mrcnn_root))

#     # add_subdirs_paths_to_list(project_root)
#     add_subdirs_paths_to_list(paths_list, datasets_root)
#     # add_subsubdirs_paths_to_list(paths_list, datasets_root)

    
    
#     paths_list.append(('mrcnn_logs', os.path.join(mrcnn_root, 'logs')))
#     paths_list.append(('mrcnn_coco_weights', os.path.join(mrcnn_root, 'mask_rcnn_coco.h5')))
    
#     paths = dict(paths_list)
#     if len(paths_list) != len(paths):
#         print("Keys for some paths coincide:")
#         paths_list.sort()
#         for i in range(len(paths_list) - 1):
#             if (paths_list[i][0] == paths_list[i + 1][0]) and (paths_list[i][1] != paths_list[i + 1][1]):
#                 print('paths\n', paths_list[i][1], '\nand\n', paths_list[i + 1][1], '\nhas the same key', paths_list[i][0])
#     return paths


def get_paths():
    paths = dict()
    
    paths['project'] = '/content/drive/My Drive/project/'
    add_subdirs_paths_to_dict(paths, paths['project'])
    add_subdirs_paths_to_dict(paths, paths['datasets'])
    add_subdirs_paths_to_dict(paths, paths['models'])
    
    keys = ['project']
    keys += get_subdirs_list(paths['project'])
    keys += get_subdirs_list(paths['datasets'])
    keys += get_subdirs_list(paths['models'])
    
    if len(keys) != len(paths):
        keys.sort()
        for i in range(len(keys) - 1):
            if (keys[i] == keys[i + 1]):
                print("key", keys[i], "corresponds to distinct paths")
    return paths

def print_paths_dict(d, dict_name):
    print("\nDictionary {} contains following paths:\n".format(dict_name))
    list_tmp = np.array([[key, d[key]] for key in d.keys()]).reshape(-1)
    print(('\n {:<35} {} \n' *  len(d)).format(*list_tmp))
    print()

paths = get_paths()
# sample_data_paths = get_sample_data_paths()
