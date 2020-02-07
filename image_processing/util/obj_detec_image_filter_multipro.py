# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import cv2
import os
import PIL.Image
import piexif
import multiprocessing as mp
from itertools import repeat
import argparse


parser = argparse.ArgumentParser(
    description='This script filters all images for obj_detection models')
parser.add_argument('--dir_path',
                    type=str,
                    required=True,
                    help='State dir contains all images.')
parser.add_argument('--check_dir',
                    type=str,
                    required=True,
                    help="State where to put the unqualified images")
parser.add_argument('--process_num',
                    type=int,
                    default=None,
                    help='State the num of cpu to run, using all as default')
parser.add_argument('--num_images_once',
                    type=int,
                    default=10000,
                    help='State num of images to check every process')

args = parser.parse_args()

dir_path = args.dir_path
check_dir = args.check_dir
process_num = args.process_num
num_images_once = args.num_images_once


def find_all_files_sub(dir_path):
    '''
    find all files included files in subdirtories.
    '''
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_list.append(dirpath + '/' + filename)
    return file_list


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
        except:
            file_name = os.path.basename(file)
            os.rename(os.path.abspath(file),
                      os.path.join(check_dir, file_name))


def multicore(func, func_e, process_num):
    pool = mp.Pool(processes=process_num)
    pool.map(func, func_e)


def chunks(l, n):
    '''Yield successive n-sized chunks from l.'''
    for i in range(0, len(l), n):
        yield l[i:i + n]


def main():
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    file_list = find_all_files_sub(dir_path)
    file_iter = chunks(file_list, num_images_once)
    multicore(check_image_format_convert_2,
              zip(file_iter, repeat(check_dir)),
              process_num)


if __name__ == '__main__':
    main()
