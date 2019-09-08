#!/usr/bin/env python3

# parse file to count the number of space, tab and line
# author: mlgc4869
# date: 2019-09-08

import os
import sys

def parse_file(path):
    """
    分析给定的文本文件，返回其空格、制表符、行的相关信息
    :arg path: 要分析的文本文件的路径
    :return: 包含空格数、制表符数、行数的元祖
    """

    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()

    return spaces, tabs, i+1

def main(path):
    """
    函数用于打印文件的分析结果
    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则返回True，否则返回False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("spaces:{} tabs:{} lines:{}".format(spaces, tabs, lines))
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Wrong parameter,[Usage: ./parsefile.py filename]")
        sys.exit(-1)
    sys.exit(0)


