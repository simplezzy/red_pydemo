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

# 模块
"""
模块是 Python 程序架构的一个核心概念
模块 就好比是 工具包，要想使用这个工具包中的工具，就需要 导入 import 这个模块
每一个以扩展名 py 结尾的 Python 源代码文件都是一个 模块
在模块中定义的 全局变量 、 函数 都是模块能够提供给外界直接使用的工具
>>>>
可以 在一个 Python 文件 中 定义 变量 或者 函数
然后在 另外一个文件中 使用 import 导入这个模块
导入之后，就可以使用 模块名.变量 / 模块名.函数 的方式，使用这个模块中定义的变量或者函数
"""
from redcat.base import printModule

printModule.print_lines("**", 5)
print(printModule.name)

# Pyc文件
"""
C 是 compiled 编译过 的意思
浏览程序目录会发现一个 __pycache__ 的目录
目录下会有一个 .pyc 文件，cpython-35 表示 Python 解释器的版本
这个 pyc 文件是由 Python 解释器将 模块的源码 转换为 字节码
Python 这样保存 字节码 是作为一种启动 速度的优化
>>>>
优化启动原理：
有了模块的字节码文件之后，下一次运行程序时，如果在 上次保存字节码之后 没有修改过源代码，Python 将会加载 .pyc 文件并跳过编译这个步骤
当 Python 重编译时，它会自动检查源文件和字节码文件的时间戳
如果你又修改了源代码，下次程序运行时，字节码将自动重新创建
"""
