#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Animal(object):

    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Dog is eating')


class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('Cat is eating')


class Mat(object):
    def run(self):
        print('mat is running')


def run_twice(animal):
    animal.run()
    animal.run()

dog1 = Dog()
dog1.run()
cat1 = Cat()
cat1.run()
run_twice(cat1)
run_twice(Animal())
run_twice(Mat())

