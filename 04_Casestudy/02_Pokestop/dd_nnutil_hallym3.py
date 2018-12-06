# developed for Course, Intro. to AI (717005) @ Hallym Univ.
# Seung-Chan Kim
# based on Prof. Andrew Ng's course material

import numpy as np
import math
import glob
import matplotlib.pyplot as plt
import tensorflow as tf
from random import shuffle

from PIL import Image

import os
import errno

# https://stackoverflow.com/a/5032238
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

            
def get_file_lists(folder1, ftypes):
    '''
    dir2test = './test/'
    fnlist1 = get_file_lists(dir2test, ftypes = ('jpg', 'JPG'))
    '''
    listc1=[]
    for ftype in ftypes:
        fnfmt = '{}/*.{}'.format(folder1, ftype)
        listc1.extend(sorted(glob.glob(fnfmt)))
    return listc1


def load_dataset(folder, suffix='_small', nclasses = 6,  test_ratio = 0.3):
    xTrain=[]
    yTrain=[]
    xTest =[]
    yTest =[]
	
    ftypes = ('jpg', 'JPG')
    
    for i in range(nclasses):
        listc1=[]
        for ftype in ftypes:
            fnfmt = '{}/{}{}/*.{}'.format(folder, i, suffix, ftype)
            listc1.extend(sorted(glob.glob(fnfmt)))
       #listc1 = sorted(glob.glob(fnfmt))
        np.array(shuffle(listc1))
        print(fnfmt,'-->', np.shape(listc1))


        for j in range(len(listc1)):
            fn1 = listc1[j]
            X = load_image(fn1)
            X = centered_crop(X, output_side_length=128)

            if j < len(listc1) * (1-test_ratio):
                xTrain.append(X)
                yTrain.append(i)
            else:
                xTest.append(X)
                yTest.append(i)


    return np.array(xTrain), np.array(yTrain), np.array(xTest), np.array(yTest)



def load_image( infilename ) :
    img = Image.open( infilename)
    img.load()

    data = np.asarray( img, dtype="float" )
    data = data / 255.0
    return data

def load_image_test(folder, img_class,  suffix='_small', idx=0):
    
    ftypes = ('jpg', 'JPG')
    listc1=[]
    for ftype in ftypes:
        fnfmt = '{}/{}{}/*.{}'.format(folder, img_class, suffix, ftype)
        #print(fnfmt)
        listc1.extend(sorted(glob.glob(fnfmt)))
    #print(np.shape(listc1))
    fn = listc1[idx]
    #print(fn)
    return load_image(fn), len(listc1)


def centered_crop(img, output_side_length):
	#print(img.shape)
	height, width, depth = img.shape
	new_height = output_side_length
	new_width = output_side_length

	height_offset = (height - output_side_length) // 2
	width_offset = (width - output_side_length) // 2

	#print(height_offset, width_offset)
	cropped_img = img[height_offset:height_offset + output_side_length,
	                          width_offset:width_offset + output_side_length,:]
	return cropped_img

def convert_to_one_hot(Y, C):
    Y = np.array(Y)
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y


def random_mini_batches(X, Y, mini_batch_size=64, seed=0):
    """
    Creates a list of random minibatches from (X, Y)

    Arguments:
    X -- input data, of shape (input size, number of examples) (m, Hi, Wi, Ci)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples) (m, n_y)
    mini_batch_size - size of the mini-batches, integer
    seed -- this is only for the purpose of grading, so that you're "random minibatches are the same as ours.

    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """

    m = X.shape[0]  # number of training examples
    mini_batches = []
    np.random.seed(seed)
    mini_batch_size = int(mini_batch_size)
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[permutation, :, :, :]
    shuffled_Y = Y[permutation, :]

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches = math.floor(m / mini_batch_size)  # number of mini batches of size mini_batch_size in your partitionning
    #num_complete_minibatches = int(m // mini_batch_size)
    #for k in range(0, int(num_complete_minibatches)):
    for k in np.arange(0, num_complete_minibatches):
        k = int(k)
        mini_batch_X = shuffled_X[int(k * mini_batch_size): int(k * mini_batch_size + mini_batch_size), :, :, :]
        mini_batch_Y = shuffled_Y[int(k * mini_batch_size): int(k * mini_batch_size + mini_batch_size), :]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[int(num_complete_minibatches * mini_batch_size): m, :, :, :]
        mini_batch_Y = shuffled_Y[int(num_complete_minibatches * mini_batch_size): m, :]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches
