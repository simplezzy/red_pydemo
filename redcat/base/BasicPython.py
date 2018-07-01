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

import keyword
import random

# 关键字
print(keyword.kwlist)

# if格式
age = 100;
if age >= 0 & age <= 120:
    print("and 条件0-120")
else:
    print("其他")

# if case：石头剪刀布case
player = int(input("请出拳(1-石头/2-剪刀/3-布):"))
computer = random.randint(1, 3)
print("computer:", computer)
if player == computer:
    print("平手")
elif ((player == 1 and computer == 2) or (player == 2 and computer == 3) or player == 3 and computer == 1):
    print("I win")
else:
    print("I lost")

# 循环
# while
i = 1
while i <= 5:
    print("Hello Python")
    i = i + 1
print("循环后的i = %d" % i)

"""
break 某一条件满足时，退出循环，不再执行后续重复的代码
continue 某一条件满足时，不执行后续重复的代码
"""

# for