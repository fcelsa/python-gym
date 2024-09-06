#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
testing some conditional statements 
output valid special 
because all if statement are evaluated and are true
"""

level = 5

if level > 0 and level < 11:
    print("valid", end=" ")


if level == 5 or level == 7:
    print("special")


"""
testing list, how python treat variables in memory, function are entire executed before print
"""

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
list4 = extendList('pippo', [])
list5 = extendList('pippo')

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

if list1 == list5:
    print("le liste sono uguali")

