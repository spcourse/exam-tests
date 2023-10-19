import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import os, sys
parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)
from helpers import has_function, test_direct_compare_fn

fn1 =  "letter_frequency"
@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fn1, ['text'])


test_text1 = "Hello, world"
test_return1 = {'h': 0.1, 'e': 0.1, 'l': 0.3, 'o': 0.2, 'w': 0.1, 'r': 0.1, 'd': 0.1}

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fn1, (test_text1,), test_return1)

test_text2 = "Glowing unicorns great."
test_return2 = {'g': 0.15, 'l': 0.05, 'o': 0.1, 'w': 0.05, 'i': 0.1, 'n': 0.15, 'u': 0.05,
                'c': 0.05, 'r': 0.1, 's': 0.05, 'e': 0.05, 'a': 0.05, 't': 0.05}

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fn1, (test_text2,), test_return2)



fn2 = "find_common_elements"

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fn2, ['list1', 'list2'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fn2, ([1, 2, 3, 4, 5], [4, 5, 5, 7, 8]), {4: 2, 5: 3})
