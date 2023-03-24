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
    has_function(test, _fileName, "count_lemmas", ['text', 'lemmas'])


test_text = "He is, was and will be a runner. And runners ran, run and will always run. This is their nature."

lemmas = {
    "runners": "runner",
    "ran": "run",
    "was": "be",
    "is": "be"
}

@t.passed(containsQ1)
@t.test(1)
def applyQ1_1(test):
    test_direct_compare_fn(test, _fileName, "count_lemmas", (test_text, lemmas), {'he': 1, 'be': 4, 'and': 3, 'will': 2, 'a': 1, 'runner': 2, 'run': 3, 'always': 1, 'this': 1, 'their': 1, 'nature': 1})


lemma_counts = {'he': 1, 'be': 4, 'and': 3, 'will': 2, 'a': 1, 'runner': 2, 'run': 3, 'always': 1, 'this': 1, 'their': 1, 'nature': 1}
nouns = {'runner', 'nature', 'building'}
verbs = {'walk', 'run', 'be'}
determiners = {'the', 'a', 'this', 'their'}


@t.test(10)
def containsQ2(test):
    has_function(test, _fileName, "count_category", ['grades'])

@t.passed(containsQ2)
@t.test(11)
def applyQ2_1(test):
    test_direct_compare_fn(test, _fileName, "count_category", (lemma_counts, nouns), 3)

@t.passed(containsQ2)
@t.test(12)
def applyQ2_2(test):
    test_direct_compare_fn(test, _fileName, "count_category", (lemma_counts, verbs), 7)

@t.passed(containsQ2)
@t.test(13)
def applyQ2_3(test):
    test_direct_compare_fn(test, _fileName, "count_category", (lemma_counts, determiners), 3)
