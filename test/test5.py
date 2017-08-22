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

# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score need int')
#         if value > 100 or value < 0:
#             raise ValueError('score need 0<score<100')
#         self._score = value
#
#
# s = Student()
# s.set_score(98)
# print(s.get_score())
# try:
#     s.set_score(888)
# except AttributeError as e:
#     print('AttributeError:', e)

# class Student(object):
#
#     @property  # 相当于getter
#     def score(self):
#         return self._score
#
#     @score.setter # 相当于setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must be between 0-99')
#         self._score = value
#
# s1 = Student()
# s1.score = 90
# print(s1.score)


# class People(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2017 - self._birth
#
# p1 = People()
# p1.birth = 1991
# print(p1.birth)
# print(p1.age)

# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# class Student(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object,(name %s)' % self.name
#
#     __repr__ = __str__
#
# print(Student('michal'))
# Student('liuy')
#
#
# class Fib(object):
#
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a
#
# for i in Fib():
#     print(i)

class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if n.start is None:
                start = 0
            a, b = 1, 1
            l = []
            for i in range(stop):
                if i >= start:
                    l.append(a)
                a, b = b, a + b
            return l

f = Fib()
print(f[3:10])



