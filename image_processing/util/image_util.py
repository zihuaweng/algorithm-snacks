# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import base64
import urllib
import cv2
import glob
import numpy as np
import tensorflow as tf
import sys
import os
import PIL.Image
import piexif
import re
import multiprocessing as mp
from itertools import repeat

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = ""


def find_all_files(dir_path):
    file_list = [os.path.abspath(i) for i in os.listdir(
        dir_path) if os.path.isfile(i)]
    return file_list


def find_all_files_sub(dir_path):
    '''
    find all files included files in subdirtories.
    '''
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_list.append(dirpath + '/' + filename)
    return file_list


def check_image(dir_path):
    file_list = find_all_files_sub(dir_path)
    for file in file_list:
        img = PIL.Image.open(file)
        # if img.format != 'JPEG':
        print(file)
        print(img.format)


def check_image_format_mv(dir_path, check_dir):
    '''
    check image format. Move images not in jpeg to a new folder. 
    '''
    img_format = ['JPEG', 'PNG']
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    file_list = find_all_files_sub(dir_path)
    for file in file_list:
        try:
            img = PIL.Image.open(file)
            if img.format not in img_format:
                print(file, img.format)
                file_name = os.path.basename(file)
                os.rename(os.path.abspath(file),
                          os.path.join(check_dir, file_name))
        except:
            file_name = os.path.basename(file)
            os.rename(os.path.abspath(file),
                      os.path.join(check_dir, file_name))


def remove_all_exif_data(dir_path):
    '''
    remove currept exif warning.
    '''
    file_list = find_all_files_sub(dir_path)
    for file in file_list:
        piexif.remove(file)  # first to  clear out all the exif data


def check_corrupt_images(dir_path, warning_dir):
    '''
    Check corrupt iamges and mv to a check dir.
    '''
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    cmd = 'find {} -iname "*.jpg" -print0 | xargs -0 jpeginfo -c | grep -e WARNING -e ERROR'.format(
        dir_path)
    jpeginfo = os.popen(cmd)
    with open('jpeginfo.log', 'w') as out:
        for line in jpeginfo.readlines():
            out.write(line)
            if re.search('WARNING', line):
                img = line.strip().split(' ')[0]
                img_name = os.path.basename(img)
                os.rename(img, os.path.join(check_dir, img_name))


def check_image_tf_format_2(dir_path, check_dir):
    '''
    Check tfrecord format.
    '''
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    file_list = find_all_files_sub(dir_path)
    for file in file_list:
        try:
            with tf.Graph().as_default():
                image_contents = tf.read_file(file)
                image = tf.image.decode_image(image_contents, channels=3)
                init_op = tf.tables_initializer()
                with tf.Session() as sess:
                    sess.run(init_op)
                    tmp = sess.run(image)
        except:
            file_name = os.path.basename(file)
            os.rename(os.path.abspath(file),
                      os.path.join(check_dir, file_name))


def check_image_tf_format(file):
    '''
    check tfrecord format.
    '''
    with tf.Graph().as_default():
        image_contents = tf.read_file(file)
        image = tf.image.decode_image(image_contents, channels=3)
        init_op = tf.tables_initializer()
        with tf.Session() as sess:
            sess.run(init_op)
            tmp = sess.run(image)


def check_image_format_convert(dir_path, check_dir):
    '''
    1. check image format and convert images in png to jpeg.
    2. check image for tfrecord.
    '''
    img_format = ['JPEG']
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    file_list = find_all_files_sub(dir_path)
    for file in file_list:
        try:
            try:
                img = PIL.Image.open(file)
            except:
                img = cv2.imread(file)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                im_pil = PIL.Image.fromarray(img)
                im_pil.save(file)
                img = PIL.Image.open(file)
            # check img mode
            if img.format in img_format:
                piexif.remove(file)  # clear out all the exif data
            else:
                new_img = os.path.abspath(file)
                img.convert('RGB').save(new_img, "JPEG")
                piexif.remove(new_img)  # clear out all the exif data
            # check_image_tf_format(file)
        except:
            file_name = os.path.basename(file)
            os.rename(os.path.abspath(file),
                      os.path.join(check_dir, file_name))


def load_image_base64(image_file, image_size):
    """Read images from base 64 transfered image_file to be classified.
       return one image numpy_array_shape = [1, image_size, image_size, 3].
    """
    with open(image_file, "rb") as image_file:
        encode_string = base64.b64encode(image_file.read())
    nparr = np.fromstring(base64.b64decode(encode_string), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_resize = cv2.resize(img, (image_size, image_size))
    img_expanded = np.expand_dims(img_resize, axis=0)
    return img_expanded


def load_image_file(image_file, image_size):
    """Read images from image_file to be classified.
       return one image numpy_array_shape = [1, image_size, image_size, 3].
    """
    img = cv2.imread(image_file)
    img_resize = cv2.resize(img, (image_size, image_size))
    img_expanded = np.expand_dims(img_resize, axis=0)
    return img_expanded


def load_image_url(image_url, image_size):
    """Read images from image_url to be classified.
       return one image numpy_array_shape = [1, image_size, image_size, 3].
    """
    # resp = urllib.request.urlopen(image_url)  # for python3.xx
    resp = urllib.urlopen(image_url)  # for python2.xx
    img = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img_resize = cv2.resize(img, (image_size, image_size))
    img_expanded = np.expand_dims(img_resize, axis=0)
    return img_expanded


def load_image_file_from_dir(image_dir, image_size):
    """Read images from dir contains images.jpg to be classified.
       return n images numpy_array_shape = [n, image_size, image_size, 3].
    """
    images = []
    for image in glob.glob(image_dir + '/*.jpg'):
        img_expanded = load_image_file(image, image_size)
        images.append(img_expanded)
    return np.asarray(images, np.float32)


def load_image_file_from_dir_dict(image_dir, image_size):
    """Read images from dir contains images.jpg to be classified.
       return n images numpy_array_shape = [n, image_size, image_size, 3].
    """
    images = {}
    for image in glob.glob(image_dir + '/*.jpg'):
        img_expanded = load_image_file(image, image_size)
        img_expanded = np.asarray(img_expanded, np.float32)
        images[image] = img_expanded
    return images


def load_graph(pd_path):
    """Unpersists graph from file as default graph."""
    with tf.gfile.FastGFile(pd_path, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')


def load_graph2(pd_path):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(pd_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    return detection_graph


def check_image_format_convert_2(arg):
    '''
    1. check image format and convert images in png to jpeg.
    2. check image for tfrecord.
    '''
    file_list, check_dir = arg
    img_format = ['JPEG']
    for file in file_list:
        try:
            try:
                img = PIL.Image.open(file)
            except:
                img = cv2.imread(file)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                im_pil = PIL.Image.fromarray(img)
                im_pil.save(file)
                img = PIL.Image.open(file)
            # check img mode
            if img.format in img_format:
                piexif.remove(file)  # clear out all the exif data
            else:
                new_img = os.path.abspath(file)
                img.convert('RGB').save(new_img, "JPEG")
                piexif.remove(new_img)  # clear out all the exif data
            # check_image_tf_format(file)
        except:
            file_name = os.path.basename(file)
            os.rename(os.path.abspath(file),
                      os.path.join(check_dir, file_name))


def multicore(func, func_e):
    pool = mp.Pool(processes=None)
    pool.map(func, func_e)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    dir_path = sys.argv[1]
    check_dir = sys.argv[2]
    # if not os.path.exists(check_dir):
    #     os.makedirs(check_dir)
    # file_list = find_all_files_sub(dir_path)
    # file_iter = chunks(file_list, 10000)
    # multicore(check_image_format_convert_2, zip(file_iter, repeat(check_dir)))

    # check_image_tf_format_2(dir_path, check_dir)
    check_corrupt_images(dir_path, check_dir)
    # check_image_format_mv(dir_path, check_dir)
    # check_image_format_convert(dir_path, check_dir)

    # dir_path = sys.argv[1]
    # check_image(dir_path)

    # dir_path = sys.argv[1]
    # remove_all_exif_data(dir_path)
