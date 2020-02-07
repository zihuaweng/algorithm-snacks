# /usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xml.etree.ElementTree as ET
import re
import os
import glob
import random
import codecs
import pandas as pd
import cv2


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


def count_num_xml_dir(dir_path, output_file, write=True):
    '''
    count object num, retrun dir_count dict , keys: dir_path, values:count
    '''
    dir_list = [os.path.join(dir_path, i) for i in os.listdir(
        dir_path) if os.path.isdir(os.path.join(dir_path, i))]
    dir_count = {}
    total = 0
    if dir_list:  # for multiply dirs in dir_path
        for dirs in dir_list:
            xml_list = [i for i in glob.glob(dirs + "/*.xml")]
            num_object = 0
            for xml in xml_list:
                tree, root = parse_xml(xml)
                num_object += len(root.findall('object'))
            dir_count[dirs] = num_object
            total += num_object
    else:    # for dir_path contains only xml files
        xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
        num_object = 0
        for xml in xml_list:
            tree, root = parse_xml(xml)
            num_object += len(root.findall('object'))
        dir_count[dir_path] = num_object
        total += num_object

    if write:
        with codecs.open(output_file, "w", "utf-8") as f:
            for key in sorted(dir_count):
                f.write('{}\t{}\n'.format(key, str(dir_count[key])))
            f.write('total\t{}'.format(total))

    return dir_count


def count_num_xml_class(dir_path, output_file, write=True):
    '''
    count object num for all classes, retrun classes_count dict , keys: class, values: count
    '''
    xml_list = [i for i in glob.glob(
        dir_path + '/**/*.xml', recursive=True)]  # /**/ could match none with recursive
    classes_count = {}
    classes_images = {}
    for xml in xml_list:
        c = os.path.basename(xml)
        class_name = re.match('food_(\d+)_.*', c).group(1)

        tree, root = parse_xml(xml)
        num_object = len(root.findall('object'))

        if class_name not in classes_count:
            classes_count[class_name] = 0
            classes_count[class_name] += num_object
            classes_images[class_name] = 0
            classes_images[class_name] += 1
        else:
            classes_count[class_name] += num_object
            classes_images[class_name] += 1

    if write:
        with codecs.open(output_file, "w", "utf-8") as f:
            f.write('Class\tImage_count\tObj_count')
            for key in sorted(classes_count.keys()):
                f.write('\n{}\t{}\t{}'.format(
                    key, str(classes_images[key]), str(classes_count[key])))

    return classes_count, classes_images


def show_names_1_xml(path):
    '''
    iterate all names in xml file
    '''
    tree, root = parse_xml(path)
    for i in root.findall('object'):
        for j in i.findall('name'):
            i.text


def show_names_2_xml(path):
    '''
    iterate all names in xml file
    '''
    tree, root = parse_xml(path)
    for i in root.iter('name'):
        i.text


def modefiy_xml(path):
    '''
    parse xml , modefiy xml and overwirte to the original file.
    '''
    tree, root = parse_xml(path)
    for i in root.iter('name'):
        new_name = re.match('(\d+)(.*)', i.text).group(1)
        i.text = str(new_name)
        tree.write(path)


def read_all_xml(dir_path):
    '''
    parse all xmls in a dir_path and overwirte the original file.
    '''
    #xml_list = [i for i in os.listdir(dir_path) if os.path.splitext(i)[1]=='.xml']
    xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
    for i in xml_list:
        modefiy_xml(i)


def read_labels(file):
    labels = []
    with open(file) as f:
        for line in f.readlines():
            labels.append(line.strip())
    return labels


def create_labels_txt(Annotation_dir, labels_file):
    '''
    create labels_file: file contains all labels which in format:
                    1
                    22
                    33
    - Annotation_dir: path of Annotation
    - lables_file: path to save labels files
    '''
    labels = []
    xml_list = [i for i in glob.glob(Annotation_dir + '' + "/*.xml")]
    for i in xml_list:
        filename = os.path.basename(i)
        classes = re.match('([a-zA-Z]+)_(\d+)(.*)', filename).group(2)
        labels.append(classes)
    labels = set(labels)
    with open(labels_file, 'w') as f:
        for i in labels:
            f.write(i + '\n')


def count_image_xml_name(labels_file, dir_path):
    '''
    count xml name and return dict in format : 
    food_1_224  1:1 2:-1 3:-1 
    food_3_334  1:-1 2:-1 3:1 #-1: abscent 1:
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


def dict_to_file_xml(labels_file, dir_path, new_dir, train_percent=0.8):
    '''
    split images to train and validate sets and save label dict into files.
    - labels_file: file contains all labels which in format:
                    1
                    22
                    33
    - dir_path: dir containes all xml files (Annotations)
    - new_dir: ouput dir (ImageSets/Main)
    - train_percent: 70% for training and 30% for evaluate
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
                f.write('{} {}\n'.format(img, str(image_map[img][label])))
        file_name = os.path.join(new_dir, 'food_' + label + '_val.txt')
        with open(file_name, 'w') as f:
            for img in val_images:
                f.write('{} {}\n'.format(img, str(image_map[img][label])))
    print('finish!')


def filter_xml(dir_path):
    xml_list = [i for i in glob.glob(dir_path + "/*.xml")]
    for xml in xml_list:
        tree, root = parse_xml(xml)
        if len(root.findall('object')) == 0:
            os.remove(xml)
            print("rm xml file {}".format(xml))


def label_map_pbtxt(labels_file, output_file='label_map.pbtxt'):
    '''
    create label file in format: start from id 1
                                item {
                                    id: 1
                                    name: 'raccoon'
                                    }
    - labels_file: apple
                   banana
                   pie
    '''
    labels = read_labels(labels_file)
    n = 1
    with open(output_file, 'w') as f:
        label = labels[0]
        f.write("item {\n")
        f.write("  id: {}\n".format(n))
        f.write("  name: '{}'\n".format(str(label)))
        f.write("}")
        for label in labels[1:]:
            n += 1
            f.write("\n\nitem {\n")
            f.write("  id: {}\n".format(n))
            f.write("  name: '{}'\n".format(str(label)))
            f.write("}")


def xml_to_csv(dir_path, csv_out):
    '''
    convert all info of xml files to csv which in format:
        filename  width  height  class  xmin  ymin  xmax  ymax
        food_284_1579.jpg    256     256    284     1     1   254   256
    - dir_path: dir contains all xml files
    - csv_out: path for new csv file
    '''
    xml_list = []
    for xml in glob.glob(dir_path + "/*.xml"):
        tree, root = parse_xml(xml)
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height',
                   'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv(csv_out, index=None)
    print('Successfully converted xml to csv.')


def move_xml_images(image_dir, xml_csv):
    '''
    generate JPEGimages file according to xml files.
    - image_dir: dir contains all images
    - xml_csv: csv contains all info of xml files in format:
        filename  width  height  class  xmin  ymin  xmax  ymax
        food_284_1579.jpg    256     256    284     1     1   254   256
    '''
    image_dir = os.path.abspath(image_dir)
    xml_info = pd.read_csv(xml_csv)
    xml_group = xml_info.groupby('filename')
    _image_list = [x for x in xml_group.groups]
    # image_list = [xml_group.get_group(x) for x in xml_group.groups]
    # for image_path in glob.glob(image_dir + '/**/*.jpg', recursive=True):
    #     image = os.path.basename(image_path)
    for i in _image_list:
        try:
            os.rename(os.path.join(image_dir, i),
                      os.path.join('JPEGImages_2', i))
        except:
            print('no {} file'.format(i))


def fill_width_height(xml_csv, xml_dir, image_dir):
    '''
    check unqualified xml files which width and height are zero
    - xml_csv: csv contains all info of xml files in format:
        filename  width  height  class  xmin  ymin  xmax  ymax
        food_284_1579.jpg    256     256    284     1     1   254   256
    - xml_dir: dir contains all xml files
    - image_dir: dir contains all images
    '''
    xml_info = pd.read_csv(xml_csv)
    zero_xml = xml_info[xml_info['width'] == 0]
    for image in set(zero_xml['filename']):
        # get image and xml path
        xml_path = os.path.join(xml_dir, image.split('.')[0] + '.xml')
        image_path = os.path.join(image_dir, image)
        # read image size
        img = cv2.imread(image_path)
        height, width, channels = img.shape
        # overwrite xml info
        tree, root = parse_xml(xml_path)
        root.find('size')[0].text = str(width)
        root.find('size')[1].text = str(height)
        root.find('size')[2].text = str(channels)
        tree.write(xml_path)


def check_xml_image(image_dir, xml_dir, log_file):
    '''
    check whether ever xml file has coresponding image
    - image_dir: dir contains all images
    - xml_dir: dir contains all xml files
    - log_file: write xml without images or the reverse case into log_file
    '''
    count_dict = {}
    image_dict = {}
    for i in glob.glob(xml_dir + '/*xml'):
        file = os.path.basename(i)
        file = file.split('.')[0]
        count_dict[file] = 1
    for i in glob.glob(image_dir + '/*jpg'):
        file = os.path.basename(i)
        file = file.split('.')[0]
        if file in count_dict:
            count_dict[file] = 0
        else:
            image_dict[file] = 1
    with codecs.open(log_file, 'w', 'utf-8') as f:
        f.write('xml files without images:\n')
        for i in count_dict:
            if count_dict[i] == 1:
                f.write('{}.xml\n'.format(i))
        f.write('images without xml files:\n')
        for i in image_dict:
            if image_dict[i] == 1:
                f.write('{}.jpg\n'.format(i))


# dir_path = sys.argv[1]
# output_file = sys.argv[2]
# _ = count_num_xml_dir(dir_path, output_file)


# dir_path = sys.argv[1]
# output_file = sys.argv[2]
# _, _ = count_num_xml_class(dir_path, output_file)


# dir_path = sys.argv[1]
# output_file = sys.argv[2]
# xml_to_csv(dir_path, output_file)


# image_dir = sys.argv[1]
# xml_csv = sys.argv[2]
# move_xml_images(image_dir, xml_csv)


# xml_csv = sys.argv[1]
# xml_dir = sys.argv[2]
# image_dir = sys.argv[3]
# fill_width_height(xml_csv, xml_dir, image_dir)


# image_dir = sys.argv[1]
# xml_dir = sys.argv[2]
# log_file = sys.argv[3]
# check_xml_image(image_dir, xml_dir, log_file)