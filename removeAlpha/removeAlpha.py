#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import  Image

def removeAlpha(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            removeAlpha(fi_d)
        else:
            pathStr = os.path.join(filepath, fi_d)
            typeStr = pathStr.split('.')[-1]
            if typeStr == 'png':
                #首先检测图片是否正常
                try:
                    img = Image.open(pathStr).convert('RGB')
                    img.save(pathStr, 'PNG')
                except IOError as e:
                    continue

if __name__ == '__main__':
    _path = os.getcwd()
    removeAlpha(_path)
