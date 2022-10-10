import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import os, sys
parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)
from helpers import has_function, test_direct_compare_fn


@t.test(0)
def containsSymmetric_difference(test):
    has_function(test, _fileName, "symmetric_difference", ['list1', 'list2'])

@t.passed(containsSymmetric_difference)
@t.test(1)
def applySymmetric_difference1(test):
    test_direct_compare_fn(test, _fileName, "symmetric_difference", ({5, 9}, {9, 2}), {2, 5})

@t.passed(containsSymmetric_difference)
@t.test(2)
def applySymmetric_difference2(test):
    test_direct_compare_fn(test, _fileName, "symmetric_difference", ({1, 4, 2, 6, 12}, {4, 1, 8, 6, 3}), {8, 2, 3, 12})


@t.test(3)
def containsCombine_ingredient_dictionaries(test):
    has_function(test, _fileName, "combine_ingredient_dictionaries", ['dictionary1', 'dictionary2'])

@t.passed(containsCombine_ingredient_dictionaries)
@t.test(4)
def applyCombine_ingredient_dictionaries1(test):
    test_direct_compare_fn(test, _fileName, "combine_ingredient_dictionaries",
    ({"banana (pcs)": 3, "butter (g)": 80, "baking soda (tsp)": 0.5, "sugar (g)": 150, "egg (pcs)": 1, "flour (g)": 200},
     {"butter (g)": 225, "sugar (g)": 450, "egg (pcs)": 5, "flour (g)": 110, "chocolate (g)": 140, "cocoa powder (g)": 55}),
    {'banana (pcs)': 3, 'butter (g)': 305, 'baking soda (tsp)': 0.5, 'sugar (g)': 600, 'egg (pcs)': 6, 'flour (g)': 310, 'chocolate (g)': 140, 'cocoa powder (g)': 55})
