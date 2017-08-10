#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s : %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.__score > 90:
            print('A')
        elif self.__score > 60:
            print('B')
        else:
            print('C')

    def set__score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

liuy = Student('liuy personal', 44)
liuq = Student('liuq personal', 88)
#liuy.set__score(101)
liuy.print_score()
liuq.print_score()
liuy.get_grade()
print(liuy.get_name())
print(liuy._Student__name)
liuy.__name = 'liuy'
print(liuy.__name)
print(liuy.get_name())
