#！/usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s : %s" % (self.name, self.score))

liuy = Student('liuy personal', 44)
liuq = Student('liuq personla', 88)
liuy.print_score()
liuq.print_score()
