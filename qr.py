#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
需要安装的库
qrcode
PIL
"""
import sys
import os
import subprocess
import time
import datetime
import hashlib
import qrcode
from PIL import Image


# 文件名
def qrcode_file_name(input_text):
    # create file name, time + qrcode content
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
    hash1 = hashlib.md5()
    hash1.update(input_text.encode("UTF-8"))
    md5_string = hash1.hexdigest()
    return timestamp + '__' + md5_string + '.png'


# 存储地址
def qrcode_file_path(text):
    cmd = 'echo $TMPDIR'
    mac_temp_folder = subprocess.getstatusoutput(cmd)
    qr_code_folder = mkdir_qrcode_folder(mac_temp_folder[1] + 'alfred_qr_code/')
    return qr_code_folder + qrcode_file_name(text)


# 存储目录，没有则创建
def mkdir_qrcode_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        return folder
    return folder


# 获取二维码
def getQRcode(data, file_name, icon=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )

    # 添加数据
    qr.add_data(data)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white")
    if icon:
        img = paste_icon(img, icon)
    # 保存img
    img.save(file_name)
    return img


# 二维码中间加图片，只需传icon为True
def paste_icon(img, icon):
    # 添加logo，打开logo照片
    icon = Image.open("1.png")
    # 获取图片的宽高
    img_w, img_h = img.size
    # 参数设置logo的大小
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到画图的x，y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    # 黏贴logo照
    img.paste(icon, (w, h), mask=None)
    return img


# 批量创建
def batch_qr(data_list):
    for e, i in enumerate(data_list):
        file_path = qrcode_file_path(str(e))
        getQRcode(i, file_path)
    return "ok"


if __name__ == '__main__':
    # 批量获取二维码
    batch_qr(["k", "v", "c", "b", "d"])
