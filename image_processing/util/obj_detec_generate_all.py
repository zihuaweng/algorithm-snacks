# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import obj_detec_util
import os
import argparse

parser = argparse.ArgumentParser(
    description='This script generates all required data for Google object\
                 detection API in format just as PASCAL VOC 2012 dataset')
parser.add_argument('--dir_path',
                    type=str,
                    required=True,
                    help='State root dir contains info including\
                     Annotations and JPEGImages.')

args = parser.parse_args()

dir_path = args.dir_path


# create label files: labels.txt & label_map.pbtxt
labels_dir = os.path.join(dir_path, 'labels')
if not os.path.exists(labels_dir):
    os.mkdir(labels_dir)


# labels.txt:
Annotation_dir = os.path.join(dir_path, 'Annotations')
labels_file = os.path.join(labels_dir, 'labels.txt')
obj_detec_util.create_labels_txt(Annotation_dir, labels_file)


# label_map.pbtxt:
label_map_file = os.path.join(labels_dir, 'label_map.pbtxt')
obj_detec_util.label_map_pbtxt(labels_file, label_map_file)


# create all files in ImageSets/Main
new_dir = os.path.join(dir_path, 'ImageSets', 'Main')
obj_detec_util.dict_to_file_xml(labels_file, Annotation_dir,
                                new_dir, train_percent=0.8)
