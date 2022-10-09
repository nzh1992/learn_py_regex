# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/10/9
Last Modified: 2022/10/9
Description: 
"""
import re


test_s = "this is a string that this is very long"

# 定义一个分组
reg = r"(?P<sub1>this)"


# 在正则表达式中，引用一个分组
reg2 = r"(?P<sub1>this).*(?P=sub1)"
