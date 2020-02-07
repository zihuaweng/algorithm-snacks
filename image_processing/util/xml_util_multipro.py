# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import os
import multiprocessing as mp
from itertools import repeat
import argparse
import re
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser(
    description='This script filters all xml files for obj_detection models')
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
                    default=1000,
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
            file_list.append(os.path.join(dirpath, filename))
    return file_list


def parse_xml(path):
    '''
    parse xml file
    '''
    tree = ET.parse(path)
    root = tree.getroot()
    return tree, root


def filter_xml_all(arg):
    '''
    filter all wrong xml files
    '''
    xml_list, check_dir = arg
    num_remove = 0
    for xml in xml_list:
        file_name = os.path.basename(xml)
        classes = re.match('([a-zA-Z]+)_(\d+)(.*)', file_name).group(2)
        try:
            tree, root = parse_xml(xml)
            # change folder name
            folder = root.find('folder')
            folder.text = 'JPEGImages'
            # change filename
            filename = root.find('filename')
            img_format = filename.text.split('.')[1]
            img_name = file_name.split('.')[0]
            new_name = '.'.join((img_name, img_format))
            filename.text = new_name
            # change path
            path = root.find('path')
            path.text = os.path.join('JPEGImages', new_name)
            # remove empty xml files
            if len(root.findall('object')) == 0:
                os.remove(xml)
                num_remove += 1
                print("rm xml file {}".format(xml))
                continue
            # check file coordinate
            width = int(root.find('size')[0].text)
            height = int(root.find('size')[1].text)
            if width == 0 or height == 0:
                new_name = os.path.join(check_dir, file_name)
                os.rename(xml, new_name)
                continue
            to_rename = 0
            for i in root.findall('object'):
                xmin = int(i.find('bndbox')[0].text)
                ymin = int(i.find('bndbox')[1].text)
                xmax = int(i.find('bndbox')[2].text)
                ymax = int(i.find('bndbox')[3].text)
                if xmax - xmin <= 2 or ymax - ymin <= 2:
                    root.remove(i)
                if xmax > width or xmin > width or ymin > height or ymax > height:
                    to_rename += 1
            if to_rename > 0:
                new_name = os.path.join(check_dir, file_name)
                os.rename(xml, new_name)
                continue
            if len(root.findall('object')) == 0:
                os.remove(xml)
                num_remove += 1
                print("rm xml file {}".format(xml))
                continue
            # change invaild object names
            for i in root.iter('name'):
                # try:
                #     new_name = re.match('(\d+)(.*)', i.text).group(1)
                #     i.text = str(new_name)
                # except:
                #     i.text = classes
                i.text = classes
            tree.write(xml)
        except:
            new_name = os.path.join(check_dir, file_name)
            os.rename(xml, new_name)

    print('remove {} xml files'.format(str(num_remove)))


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
    multicore(filter_xml_all,
              zip(file_iter, repeat(check_dir)),
              process_num)


if __name__ == '__main__':
    main()