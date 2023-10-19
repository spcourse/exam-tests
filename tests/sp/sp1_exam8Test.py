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

fname1 = "common_elements"

@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fname1, ['list1', 'list2'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fname1, ([1, 2, 3], [3, 4, 2, 8]), [2, 3])

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fname1, ([18], ["a", "b", "c"]), [])


### Q2

fname2 = "right_justify"

test_text = [
    "Right justification is a formatting technique.",
    "It aligns text along the right margin.",
    "Each line starts at the same position.",
    "The rest of the line fills with spaces.",
    "It creates a clean and organized look."
]

right_text = [
    "Right justification is a formatting technique.",
    "        It aligns text along the right margin.",
    "        Each line starts at the same position.",
    "       The rest of the line fills with spaces.",
    "        It creates a clean and organized look."
]

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fname2, ['lines'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fname2, (test_text, ), right_text)


### Q3

fname3 = "simulate_cattle_population"
initial_population = 100
fertility_rate = 0.6
death_rate = 0.3
extra_new_cows_per_year = 5
threshold = 500

@t.test(20)
def containsQ3(test):
    has_function(test, _fileName, fname3, ['initial_population', 'fertility_rate', 'death_rate', 'extra_new_cows_per_year', 'threshold'])

@t.passed(containsQ3)
@t.test(21)
def applyQ3_1(test):
    test_direct_compare_fn(test, _fileName, fname3, (initial_population, fertility_rate, death_rate, extra_new_cows_per_year, threshold), 6)



### Q4

fname4 = "number_of_home_matches_per_year"

@t.test(30)
def containsQ4(test):
    has_function(test, _fileName, fname4, ['filename'])

@t.passed(containsQ4)
@t.test(31)
def applyQ4_1(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca.txt",), [9, 18, 19, 11])

@t.passed(containsQ4)
@t.test(32)
def applyQ4_2(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca_short.txt",), [2])
