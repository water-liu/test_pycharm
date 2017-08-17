#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Myobject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 'adb')
print(getattr(obj, 'y'))
print(hasattr(obj, 'power'))
# print(getattr(obj, 'z'))


