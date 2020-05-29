#!/usr/bin/env python3
# coding: utf-8

from pytube import YouTube
from sys import argv


def download(youtube_link, dir_path, file_name):
    yt = YouTube(youtube_link)
    # except:
    #     print("Connection Error")  # to handle exception

    # filters out all the files with "mp4" extension
    mp4files = yt.filter('mp4')

    yt.set_filename(file_name)  # to set the name of the file

    # get the video with the extension and resolution passed in the get() function
    d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        # downloading the video
        d_video.download(dir_path)
    except:
        print("Some Error!")
    print('Task Completed!')


if __name__ == '__main__':
    youtube_link, dir_path, file_name = argv[1:]
    download(youtube_link, dir_path, file_name)