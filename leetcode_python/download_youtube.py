#!/usr/bin/env python3
# coding: utf-8

from pytube import YouTube
from sys import argv


def download(youtube_link, dir_path, file_name):
    yt = YouTube(youtube_link)
    # except:
    #     print("Connection Error")  # to handle exception

    # filters out all the files with "mp4" extension
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(file_name)


if __name__ == '__main__':
    # youtube_link, dir_path, file_name = argv[1:]
    youtube_link, dir_path, file_name = "https://www.youtube.com/watch?v=s6DKRgtVLGA&t=493s", "./", "japanese_Katakana"
    download(youtube_link, dir_path, file_name)
