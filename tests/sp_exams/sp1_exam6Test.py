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

fname1 = "jump"

@t.test(0)
def containsQ1(test):
    has_function(test, _fileName, fname1, ['n'])

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, fname1, (4,), [1, 2, 3, 6])

@t.passed(containsQ1)
@t.test(2)
def applyQ1_2(test):
    test_direct_compare_fn(test, _fileName, fname1, (10,), [1, 2, 3, 6, 7, 14, 15, 30, 31, 62])


### Q2

fname2 = "silly_abridge"

alice = """Oh, how I wish I could shut up like a telescope! \
I think I could, if only I knew how to begin."""

@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, fname2, ['text', 'step'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, fname2, (alice, 4), "Oh, how I I could shut like a telescope! think I could, only I knew to begin.")

@t.passed(containsQ2)
@t.test(12)
def applyQ2_2(test):
    test_direct_compare_fn(test, _fileName, fname2, (alice, 2), "Oh, I I shut like telescope! think could, only knew to")



### Q3

fname3 = "longest_sequence"

@t.test(20)
def containsQ3(test):
    has_function(test, _fileName, fname3, ['lst'])

@t.passed(containsQ3)
@t.test(21)
def applyQ3_1(test):
    test_direct_compare_fn(test, _fileName, fname3, (['a', 'b', 'b', 0],), 2)

@t.passed(containsQ3)
@t.test(22)
def applyQ3_2(test):
    test_direct_compare_fn(test, _fileName, fname3, (['a', 'b', 'b', 0, 0, 0],), 3)

@t.passed(containsQ3)
@t.test(23)
def applyQ3_3(test):
    test_direct_compare_fn(test, _fileName, fname3, ([1, 1, 1, 1, 2, 3],), 4)


### Q4

fname4 = "dates_first_match_of_the_month"

@t.test(30)
def containsQ4(test):
    has_function(test, _fileName, fname4, ['filename'])

@t.passed(containsQ4)
@t.test(31)
def applyQ4_1(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca.txt",), ['29/08/11', '10/09/11', '02/10/11', '06/11/11', '03/12/11', '08/01/12', '04/02/12', '03/03/12', '07/04/12', '02/05/12', '19/08/12', '02/09/12', '07/10/12', '03/11/12', '01/12/12', '06/01/13', '03/02/13', '02/03/13', '06/04/13', '05/05/13', '01/06/13', '18/08/13', '01/09/13', '05/10/13', '01/11/13', '01/12/13', '05/01/14', '01/02/14', '02/03/14', '05/04/14', '03/05/14'])

@t.passed(containsQ4)
@t.test(32)
def applyQ4_2(test):
    test_direct_compare_fn(test, _fileName, fname4, ("barca_short.txt",),  ['29/08/11', '10/09/11'])
