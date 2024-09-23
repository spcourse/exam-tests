import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import pandas as pd
import numpy as np


def sandbox():
    lib.require("iris.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/iris.csv")

def fn_string(fname, args):
    return f"{fname}({', '.join(args)})"

def has_function(test, file_name, function_name, expected_args):
    def testMethod():
        if assertlib.fileContainsFunctionDefinitions(file_name, function_name):
            fn = lib.getFunction(function_name, file_name)
            provided_args = fn.arguments
            if len(provided_args) == len(expected_args):
                return True, ""
            else:
                if len(expected_args) == 1:
                    m1 = f"Expected a single argument: {fn_string(function_name, expected_args)}"
                else:
                    m1 = f"Expected {len(expected_args)} arguments: {fn_string(function_name, expected_args)}"
                if len(provided_args) == 1:
                    m2 = f"Your function takes a single argument: {fn_string(function_name, provided_args)}"
                else:
                    m2 = f"Your function takes {len(provided_args)} arguments: {fn_string(function_name, provided_args)}"

                return False, f"Incorrect number of arguments:\n\t{m1}\n\t{m2}"
        else:
            return False, "Function not defined"

    test.test = testMethod
    test.description = lambda : f"Defines the function `{function_name}()`"

@t.test(0)
def containsCount_pages(test):
    has_function(test, _fileName, "count_pages", ['books_page_count', 'read_books'])

@t.passed(containsCount_pages)
@t.test(1)
def testCount_pages(test):
    inp = [{'Nineteen Eighty-Four': 328, 'The Very Hungry Catterpillar': 22, 'Gulliver\'s Travels': 352, 'Frankenstein': 280, 'David Copperfield': 624, 'Moby-Dick': 736, 'Ulysses': 730, 'Lord of the Flies': 224, 'To Kill a Mockingbird': 281, 'The Picture of Dorian Gray': 272,'The Hobbit': 310},  ['The Very Hungry Catterpillar', 'The Hobbit', 'Frankenstein', 'Lord of the Flies']]
    answer = 836
    fn_name = 'count_pages'

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        out = fn(*inp)

        if out == answer:
            return True, f"Correct answer!"
        else:
            return False, f"Incorrect answer!"

    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(...)"
    test.timeout = lambda : 90

@t.test(2)
def containsDecrypt(test):
    has_function(test, _fileName, "decrypt", ['text'])

@t.passed(containsDecrypt)
@t.test(3)
def testDecrypt(test):
    inp = "So, that door is the nearest Exit? Correct. Used Rarely? Exactly. Terrific!"
    answer = ['S', 'E', 'C', 'R', 'E', 'T']
    fn_name = 'decrypt'

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        out = fn(inp)

        if out == answer:
            return True, f"Correct answer for input {inp}"
        else:
            return False, f"Incorrect answer for input {inp}"

    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({inp})"
    test.timeout = lambda : 90

@t.test(4)
def containsCompute_average_per_species(test):
    has_function(test, _fileName, "compute_average_per_species", ['iris_dataframe', 'column'])

@t.passed(containsCompute_average_per_species)
@t.test(5)
def testCompute_average_per_species(test):
    inp = [pd.read_csv('iris.csv'), 'petal_width']
    answer = pd.Series({'setosa': 0.246, 'versicolor': 1.326, 'virginica': 2.026})
    fn_name = 'compute_average_per_species'

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        out = fn(*inp)

        if np.allclose(out, answer):
            return True, f"Correct answer!"
        else:
            return False, f"Incorrect answer!"

    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(...)"
    test.timeout = lambda : 90
