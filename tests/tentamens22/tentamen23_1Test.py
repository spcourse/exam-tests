import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import os, sys
parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)
from helpers import has_function, test_direct_compare_fn

def sandbox():
    # https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt
    lib.require("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
    lib.require("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")


### Q1

fname1 = "sum_divisors"

@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fname1, ['n'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fname1, (6,), 12)

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fname1, (12,), 28)


### Q2

fname2 = "count_vowels"

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fname2, ['text'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fname2, ("Hello, world!",), 3)

@t.passed(containsQ2)
@t.test(12)
def applyQ2_2(test):
    test_direct_compare_fn(test, _fileName, fname2, ("Exclent eggs!",), 3)



### Q3

fname3 = "gcd"

@t.test(20)
def containsQ3(test):
    has_function(test, _fileName, fname3, ['a', 'b'])

@t.passed(containsQ3)
@t.test(21)
def applyQ3_1(test):
    test_direct_compare_fn(test, _fileName, fname3, (24, 60), 12)

@t.passed(containsQ3)
@t.test(22)
def applyQ3_2(test):
    test_direct_compare_fn(test, _fileName, fname3, (10, 25), 5)

### Q4

fname4 = "home_again"

@t.test(30)
def containsQ4(test):
    has_function(test, _fileName, fname4, ['filename'])

@t.passed(containsQ4)
@t.test(31)
def applyQ4_1(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca.txt",), ['22/10/11', '03/12/11', '05/05/12', '17/03/13', '18/08/13', '01/02/14'])
