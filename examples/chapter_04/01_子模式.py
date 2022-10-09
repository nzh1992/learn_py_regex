# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2022/10/9
Last Modified: 2022/10/9
Description: 
"""
import re


test_str = "their"

reg = r"[tT]h(eir)"
result = re.search(reg, test_str)
print(result)