#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# calc.pyのパスを指定
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts/'))
from calc import Calc

def test_add_01():
    assert Calc(9,2).add() == 11

def test_add_02():
    assert Calc(-9,2).add() == -7

def test_dif_01():
    assert Calc(9,2).dif() == 7

def test_dif_02():
    assert Calc(-9,2).dif() == -11

def test_seki_01():
    assert Calc(9,2).seki() == 18

def test_seki_02():
    assert Calc(-9,2).seki() == -18

def test_shou_01():
#    assert Calc(9,2).shou() == 4.5
    assert Calc(9,2).shou() == 4

def test_shou_02():
#    assert Calc(-9,2).shou() == -4.5
    assert Calc(-9,2).shou() == -5
