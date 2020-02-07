#/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xml.etree.ElementTree as ET
import re
import os
import glob
import random
import codecs
import sys


def parse_xml(path):
    '''
    parse xml file
    '''
    tree = ET.parse(path)
    root = tree.getroot()
    return tree, root

# Element.findall() finds only elements with a tag which are direct
# children of the current element. Element.find() finds the first child
# with a particular tag, and Element.text accesses the element’s text
# content. Element.get() accesses the element’s attributes:


def count_num_dirs(dir_path, output_file="count.txt", write=True):
    '''
    count object num, retrun dir_count dict , keys: dir_path, values:count
    '''
    dir_list = [os.path.join(dir_path, i) for i in os.listdir(
        dir_path) if os.path.isdir(os.path.join(dir_path, i))]
    dir_count = {}
    if len(dir_list) > 0:  # for multiply dirs in dir_path
        for dirs in dir_list:
            xml_list = [i for i in glob.glob(dirs + "/*.xml")]
            num_object = 0
            for xml in xml_list:
                tree, root = parse_xml(xml)
                num_object += len(root.findall('object'))
            dir_count[dirs] = num_object
    else:    # for dir_path contains only xml files
        xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
        num_object = 0
        for xml in xml_list:
            tree, root = parse_xml(xml)
            num_object += len(root.findall('object'))
        dir_count[dir_path] = num_object

    if write:
        #
        #     print(key+' '+str(dir_count[key])+'\n')
        with codecs.open(output_file, "w", "utf-8-sig") as f:
            for key in dir_count.keys():
                f.write(key + "\t" + str(dir_count[key]) + "\n")
                # out.write(key.encode('gbk')+"\t"+str(dir_count[key]).encode('gbk')+'\n')
    return dir_count


def count_num_classes(dir_path, output_file="count.txt", write=True):
    '''
    count num of xml files and num of objects for each class
    - dir_path: dir_path containes all xml files or multiply folders contain xml files
    '''
    def _xml_count(dir_path):
        '''
        count num of xml files and num of objects for each class
        - count_dict: xml_count dict to store info
        - dir_path: folder contains xml files
        '''
        count_dict = {}
        xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
        for xml in xml_list:
            xml_name = os.path.basename(xml)
            classes = re.match('([a-zA-Z]+)_(\d+)(.*)', xml_name).group(2)
            # define elements to count
            if classes not in count_dict:
                count_dict[classes] = {}
                count_dict[classes]['num_xml'] = 0
                count_dict[classes]['num_object'] = 0

            # read xml files
            tree, root = parse_xml(xml)
            count_dict[classes]['num_object'] += len(root.findall('object'))
            count_dict[classes]['num_xml'] += 1

        return count_dict

    dir_list = [os.path.join(dir_path, i) for i in os.listdir(
        dir_path) if os.path.isdir(os.path.join(dir_path, i))]
    if len(dir_list) > 0:  # for multiply dirs in dir_path
        for dirs in dir_list:
            xml_count = _xml_count(dirs)
    else:    # for dir_path contains only xml files
        xml_count = _xml_count(dir_path)

    if write:
        # define total counts
        total = {}
        total['num_xml'] = 0
        total['num_object'] = 0
        #     print(key+' '+str(dir_count[key])+'\n')
        with codecs.open(output_file, "w", "utf-8-sig") as f:
            f.write('xml file count:')
            fmt = '\n{}\t{}\t{}'
            f.write(fmt.format('class', 'xml_count', 'object_count'))
            total['num_classes'] = len(xml_count.keys())
            for key in sorted(xml_count.keys()):
                f.write(fmt.format(key, str(xml_count[key]['num_xml']), str(
                    xml_count[key]['num_object'])))
                total['num_xml'] += xml_count[key]['num_xml']
                total['num_object'] += xml_count[key]['num_object']
                # out.write(key.encode('gbk')+"\t"+str(dir_count[key]).encode('gbk')+'\n')
            f.write(fmt.format('total_classes', 'xml_count', 'object_count'))
            f.write(fmt.format(total['num_classes'], total['num_xml'], total['num_object']))

    print('finish counting!')
    return xml_count


def show_names_1(path):
    '''
    iterate all names in xml file
    '''
    tree, root = parse_xml(path)
    for i in root.findall('object'):
        for j in i.findall('name'):
            i.text


def show_names_2(path):
    '''
    iterate all names in xml file
    '''
    tree, root = parse_xml(path)
    for i in root.iter('name'):
        i.text


def modefiy_xml_name(path):
    '''
    parse xml , modefiy xml and overwirte to the original file.
    - path: xml path
    change name from 1111abc to 1111
    '''
    tree, root = parse_xml(path)
    for i in root.iter('name'):
        new_name = re.match('(\d+)(.*)', i.text).group(1)
        i.text = str(new_name)
        tree.write(path)


def modefiy_xml_filename(path):
    '''
    parse xml , modefiy xml and overwirte to the original file.
    - path: xml path
    '''
    filename = os.path.basename(path).split('.')[0]
    tree, root = parse_xml(path)
    for i in root.iter('filename'):
        img_format = i.text.split('.')[1]
        new_name = str(filename + '.' + img_format)
        i.text = str(new_name)
        tree.write(path)


def read_all_xml(dir_path):
    '''
    parse all xmls in a dir_path and overwirte the original file.
    '''
    # xml_list = [i for i in os.listdir(dir_path) if
    # os.path.splitext(i)[1]=='.xml']
    xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
    return xml_list


def read_labels(file):
    labels = []
    with open(file) as f:
        for line in f.readlines():
            labels.append(line.strip())
    return labels


def count_image_xml_name(labels_file, dir_path):
    '''
    count xml name and return dict in format :
    food_1_224  1:1  3:-1
    food_3_334  1:-1  3:1 #-1: abscent 1:
    '''
    labels = read_labels(labels_file)
    xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
    image_map = {}
    for xml in xml_list:
        img = os.path.splitext(os.path.basename(xml))[0]
        image_map[img] = {}
        tree, root = parse_xml(xml)
        for i in root.iter('name'):
            image_map[img][i.text] = 1
        for j in labels:
            if j not in image_map[img].keys():
                image_map[img][j] = -1
    return image_map, labels


def dict_to_file(labels_file, dir_path, new_dir, train_percent=0.7):
    '''
    split images to train and validate sets and save label dict into files.
    '''
    image_map, labels = count_image_xml_name(labels_file, dir_path)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    images_list = [i for i in image_map.keys()]
    random.shuffle(images_list)  # shuffle image list
    num_images = len(images_list)
    print('{} images total'.format(num_images))
    train_images = images_list[:int(train_percent * num_images)]
    print('{} train images'.format(len(train_images)))
    val_images = images_list[int(train_percent * num_images):]
    print('{} val images'.format(len(val_images)))
    for label in labels:
        file_name = os.path.join(new_dir, 'food_' + label + '_train.txt')
        with open(file_name, 'w') as f:
            for img in train_images:
                f.write(img + ' ' + str(image_map[img][label]) + '\n')
        file_name = os.path.join(new_dir, 'food_' + label + '_val.txt')
        with open(file_name, 'w') as f:
            for img in val_images:
                f.write(img + ' ' + str(image_map[img][label]) + '\n')
    print('finish!')


def filter_xml_object(dir_path):
    xml_list = read_all_xml(dir_path)
    for xml in xml_list:
        tree, root = parse_xml(xml)
        if len(root.findall('object')) == 0:
            os.remove(xml)
            print("rm xml file {}".format(xml))


def filter_xml_all(dir_path, check_dir):
    '''
    xmax < width
    '''
    xml_list = read_all_xml(dir_path)
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
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


# dir_path=sys.argv[1]
# check_dir=sys.argv[2]
# filter_xml_all(dir_path, check_dir)


dir_path = sys.argv[1]
count_num_classes(dir_path, output_file="count.txt", write=True)
