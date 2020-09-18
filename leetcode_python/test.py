#!/usr/bin/env python3
# coding: utf-8
import abc

class A(abc.ABC):
    def __init__(self):
        self.a = 1

    @abc.abstractmethod
    def test(self):
        raise Exception("need to valida")

class B(A):
    def func(self):
        print("aaaa")

    def test(self):
        print('bbbb')


b = B().func()