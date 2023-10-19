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


@t.test(0)
def containsTwoish(test):
    has_function(test, _fileName, "twoish", ['n'])

@t.passed(containsTwoish)
@t.test(1)
def applyTwoish1(test):
    test_direct_compare_fn(test, _fileName, "twoish", (2,), 1.5, atol = 0.01)

@t.passed(containsTwoish)
@t.test(2)
def applyTwoish2(test):
    test_direct_compare_fn(test, _fileName, "twoish", (10,), 1.998046875, atol = 0.01)


@t.test(3)
def containsHamming_distance(test):
    has_function(test, _fileName, "hamming_distance", ['text1', 'text2'])

@t.passed(containsHamming_distance)
@t.test(4)
def applyHamming_distance1(test):
    test_direct_compare_fn(test, _fileName, "hamming_distance", ("Norwegian Wood", "Norwegian Fjord"), 1)

@t.passed(containsHamming_distance)
@t.test(5)
def applyHamming_distance2(test):
    test_direct_compare_fn(test, _fileName, "hamming_distance",
    ("I love deadlines. I love the whooshing noise they make as they go by.",
     "I LOVE pizza. I love the round shape they have."), 6)


@t.test(6)
def containsBiggest_improvement(test):
    has_function(test, _fileName, "biggest_improvement", ['filename'])

@t.passed(containsBiggest_improvement)
@t.test(7)
def applyBiggest_improvement1(test):
    test_direct_compare_fn(test, _fileName, "biggest_improvement", ('barca.txt',), '16/03/14')

@t.passed(containsBiggest_improvement)
@t.test(8)
def applyBiggest_improvement2(test):
    test_direct_compare_fn(test, _fileName, "biggest_improvement", ('barca_short.txt',), '17/09/11')


@t.test(9)
def containsPopulation(test):
    has_function(test, _fileName, "population", ['start_size', 'end_size'])

@t.passed(containsPopulation)
@t.test(10)
def applyPopulation1(test):
    test_direct_compare_fn(test, _fileName, "population", (1200,1300), 1)

@t.passed(containsPopulation)
@t.test(11)
def applyPopulation2(test):
    test_direct_compare_fn(test, _fileName, "population", (600, 3000), 21)
