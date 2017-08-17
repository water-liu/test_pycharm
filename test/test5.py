#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from types import MethodType


# class Student(object):
#     __slots__ = ('name', 'age', 'set_age')
#
#
# def set_age(self, age):
#     self.age = age
#
# s = Student()
# s.name = 'liuy'
# s2 = Student()
# print(s.name)
# # s2.set_age(23)
# s.set_age = MethodType(set_age, s)
# s.set_age(33)
# print(s.age)
# Student.set_age = set_age
# s2.set_age(24)
# print(s2.age)
# # s2.score = 99
# # print(s2.score)
# try:
#     s.score = 99
# except AttributeError as e:
#     print('AttributeError:', e)

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score need int')
        if value > 100 or value < 0:
            raise ValueError('score need 0<score<100')
        self._score = value


s = Student()
s.set_score(98)
print(s.get_score())
# try:
#     s.set_score(888)
# except AttributeError as e:
#     print('AttributeError:', e)





