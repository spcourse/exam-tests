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

fname1 = "integer_sequence"

@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fname1, ['n'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fname1, (10),), [10, 6, 4, 3, 1])

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fname1, (12,), [12, 7, 3, 1])


### Q2

fname2 = "single_space"

sam = "I am Sam.  I am Sam.  Sam I am.  That Sam-I-Am!  That Sam-I-Am!  I do not like that Sam-I-Am! Do would you like green eggs and ham?  I do not like them, Sam-I-Am.  I do not like green eggs and ham."

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fname2, ['text'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fname2, (sam, ), "I am Sam. I am Sam. Sam I am. That Sam-I-Am! That Sam-I-Am! I do not like that Sam-I-Am! Do would you like green eggs and ham? I do not like them, Sam-I-Am. I do not like green eggs and ham.")


### Q3

fname3 = "fibonacci"

@t.test(20)
def containsQ3(test):
    has_function(test, _fileName, fname3, ['n'])

@t.passed(containsQ3)
@t.test(21)
def applyQ3_1(test):
    test_direct_compare_fn(test, _fileName, fname3, (4,), 3)

@t.passed(containsQ3)
@t.test(22)
def applyQ3_2(test):
    test_direct_compare_fn(test, _fileName, fname3, (10, ), 55)


### Q4

fname4 = "total_goals_per_year"

@t.test(30)
def containsQ4(test):
    has_function(test, _fileName, fname4, ['filename'])

@t.passed(containsQ4)
@t.test(31)
def applyQ4_1(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca.txt",), [50, 121, 107, 51])

@t.passed(containsQ4)
@t.test(32)
def applyQ4_2(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca_short.txt",),  [17])
