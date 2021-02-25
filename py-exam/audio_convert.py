#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
音频格式转换 ffmpeg
"""
import os


def convert_audio(ffmpeg_path, source_path, save_path, old_format, new_format):
    source_file = os.listdir(source_path)
    print(source_file)
    for source in source_file:

        # 将音频格式A转换成格式B

        if old_format in source:
            new_name = source.replace(old_format, new_format)  # 新音频名字,替换后缀名

            print('正在转换音频:{}'.format(new_name))
            cmd = ffmpeg_path + ' -i ' + source_path + source + ' ' + save_path + new_name
            os.system(cmd)

        # 将所有音频转换成新格式

        # new_name = source.split('.')[0] + new_format  # 新音频名字,替换后缀名
        #
        # print('正在转换音频:{}'.format(new_name))
        # cmd = ffmpeg_path + ' -i ' + source_path + source + ' ' + save_path + new_name
        # os.system(cmd)

    print('所有音频转换完毕!')


sourcePath = 'E:/Audios/Audio/'
savePath = 'E:/Audios/convertAudio/'
ffmpegPath = 'D:/ffmpeg/bin/ffmpeg.exe'

oldFormat = '.amr'
newFormat = '.wav'
convert_audio(ffmpegPath, sourcePath, savePath, oldFormat, newFormat)
