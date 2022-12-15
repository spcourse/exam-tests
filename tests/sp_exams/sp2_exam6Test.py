import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import os, sys
parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)
from helpers import has_function, test_direct_compare_fn


@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, "n_intersection", ['sets'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, "n_intersection", ([{5, 9, 6}, {9, 2, 6}, {6, 5, 9}],), {9, 6})

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, "n_intersection", ([
                          {"kerfuffle", "hullaballoo", "ragamuffin", "flummox"},
                          {"kerfuffle", "ragamuffin", "gobbledygook", "flummox"},
                          {"hullaballoo", "ragamuffin", "gobbledygook", "flummox"},
                          {"hullaballoo", "ragamuffin", "ragamuffin", "gobbledygook", "flummox"}],),
                          {'ragamuffin', 'flummox'})

@t.passed(containsQ1)
@t.test(3)
def applyQ1_3(test):
    test_direct_compare_fn(test, _fileName, "n_intersection", ([],), set())


@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, "calculate_distribution", ['grades'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, "calculate_distribution", ({'Albert': 7, 'Marie': 9, 'Olivier': 7, 'Tom': 9, 'Elio': 7},), {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 3, 8: 0, 9: 2, 10: 0})

@t.passed(containsQ2)
@t.test(12)
def applyQ2_2(test):
    test_direct_compare_fn(test, _fileName, "calculate_distribution", ({'Albert': 3, 'Marie': 8, 'Olivier': 8, 'Tom': 8, 'Elio': 9},),
                          {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 3, 9: 1, 10: 0})
