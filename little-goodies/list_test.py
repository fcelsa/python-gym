#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
some test with list and his memory occupancy
"""

# list init ...same list ...same results ?
list1 = [0] * 3
list2 = [0, 0, 0]
list3 = [0 for i in range(3)]

print(list1, list2, list3)

size_list1 = sys.getsizeof(list1)
size_list2 = sys.getsizeof(list2)
size_list3 = sys.getsizeof(list3)

print(size_list1, size_list2, size_list3)

