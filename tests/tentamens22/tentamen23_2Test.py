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

fname1 = "triangular"

@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fname1, ['n'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fname1, (3,), [1, 3])

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fname1, (15,), [1, 3, 6, 10])

@t.passed(containsQ1)
@t.test(3)
def applyQ1_3(test):
    test_direct_compare_fn(test, _fileName, fname1, (16,), [1, 3, 6, 10, 15])


### Q2

fname2 = "classified"

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fname2, ['text', 'censor_word'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fname2, ("We're all mad here.", "mad"), "We're all ### here.")

@t.passed(containsQ2)
@t.test(12)
def applyQ2_2(test):
    test_direct_compare_fn(test, _fileName, fname2, ("Why, sometimes I've believed as many as six impossible things before breakfast.", "AS"), "Why, sometimes I've believed ## many ## six impossible things before breakfast.")



### Q3

fname3 = "collatz"

@t.test(20)
def containsQ3(test):
    has_function(test, _fileName, fname3, ['n'])

@t.passed(containsQ3)
@t.test(21)
def applyQ3_1(test):
    test_direct_compare_fn(test, _fileName, fname3, (12,), [12, 6, 3, 10, 5, 16, 8, 4, 2, 1])

@t.passed(containsQ3)
@t.test(22)
def applyQ3_2(test):
    test_direct_compare_fn(test, _fileName, fname3, (3,), [3, 10, 5, 16, 8, 4, 2, 1])

### Q4

fname4 = "average_goals_per_game"

@t.test(30)
def containsQ4(test):
    has_function(test, _fileName, fname4, ['filename'])

@t.passed(containsQ4)
@t.test(31)
def applyQ4_1(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca.txt",), 2.8, atol=0.1)

@t.passed(containsQ4)
@t.test(32)
def applyQ4_2(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca_short.txt",), 4.25, atol=0.1)
