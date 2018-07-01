#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide configure file management service in i18n environment.

Authors: zhouzhiyu
Date:    2018/7/1
"""
name = "redcat"


def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    row = 1
    while row < 5:
        print(char, times)
        row += 1
