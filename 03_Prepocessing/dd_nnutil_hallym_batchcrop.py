# developed for Course, Intro. to AI (717005) @ Hallym Univ.
# Seung-Chan Kim
# based on Prof. Andrew Ng's course material

import numpy as np
import glob
import matplotlib.pyplot as plt

from PIL import Image

import os
import errno

# https://stackoverflow.com/a/5032238

def batch_crop(dirpath, ftypes = ('jpg', 'JPG'), resize_ratio = 1, to_rotate= False, w = 224, h = 224):
    for folder in os.listdir(dirpath):
        print(folder)
        sav_dir = os.path.join(dirpath, folder +'_crop')
        create_dir(sav_dir)
        listc1 = get_file_lists(os.path.join(dirpath,folder), ftypes)
        for img_path in listc1:
            print(img_path)
            img = Image.open(img_path)
            width, height = img.size
                   
            if resize_ratio <1:
                w2 = int(width * resize_ratio)
                h2 = int(height * resize_ratio)                
                img = resize_image(img, w2, h2)
                
            img = center_crop(img, w, h)
            if to_rotate:
                img = img.rotate(-90)
                
            img.save(os.path.join(sav_dir, os.path.split(img_path)[-1]))
                    
def create_dir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)   
        
        
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

            
def get_file_lists(folder1, ftypes):
    listc1=[]
    for ftype in ftypes:
        fnfmt = '{}/*.{}'.format(folder1, ftype)
        listc1.extend(sorted(glob.glob(fnfmt)))
    return listc1

def center_crop(img, new_width, new_height):
    width, height = img.size
    left = int((width - new_width)/2)
    top = int((height - new_height)/2)
    right = int((width + new_width)/2)
    bottom = int((height + new_height)/2)

    return img.crop((left, top, right, bottom))

def load_image_compare(dirpath, img_class, idx = 0):
    img_folder_path = os.path.join(dirpath, str(img_class))
    img_name = os.listdir(img_folder_path)[idx]
    img = Image.open(os.path.join(img_folder_path, img_name))
    
    img_folder_path = os.path.join(dirpath, str(img_class)+'_crop')
    img_name = os.listdir(img_folder_path)[idx]
    img_crop = Image.open(os.path.join(img_folder_path, img_name))
    
    return img, img_crop

def resize_image(img, w, h):
    return img.resize((w,h))