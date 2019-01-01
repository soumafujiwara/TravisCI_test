#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calc: 

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def seki(self):
        return self.a*self.b

    def shou(self):
        return self.a/self.b