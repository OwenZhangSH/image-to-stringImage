# -*- coding: utf-8 -*-
#
#
# 
"""
文件说明：

File   : image.py

Authors: zhangshuhao01@baidu.com
Date   : 2016/11/23
Comment: 
"""
# 标准库
from PIL import Image
import argparse
# 第三方库

# 自有库

# 全局变量
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    # 获得字符总数
    length = len(ascii_char)
    # 每个字符占几个灰度
    unit_length = 256 / length + 1
    gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 计算该灰度位于那个区间
    unit_num = gary / unit_length
    return ascii_char[unit_num]


if __name__ == '__main__':
    # 命令行参数处理
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')  # 输入img文件
    parser.add_argument('-o', '--output')  # 输出的文本文件
    parser.add_argument('--width', type=int, default=80)  # 输出字符画的宽度
    parser.add_argument('--height', type=int, default=80)  # 输出字符画的高度

    # 参数获取
    args = parser.parse_args()

    # 变量赋值
    img = args.file
    output = args.output
    width = args.width
    height = args.height

    # 图片文件解析
    img = Image.open(img)
    img = img.resize((width, height), Image.NEAREST)
    # img.save('./pixel.png')


    txt = ''
    for i in range(height):
        for j in range(width):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'

    if output:
        with open(output, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
