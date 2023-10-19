import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import pandas as pd


def sandbox():
    # https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt
    lib.require("election_results_amsterdam_2022.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/election_results_amsterdam_2022.csv")
    # lib.require("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

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
def containsCalories(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "allowed_calories")
	test.description = lambda : "Defines the function allowed_calories"
	test.timeout = lambda : 10

@t.passed(containsCalories)
@t.test(1)
def testCalories1(test):
    food = {"banana": 88, "apple": 52, "nuts": 606, "chocolate": 545, "salmon": 208, "smoothie": 36, "fries": 322, "sandwich": 265}
    eaten = ["banana", "salmon", "fries"]
    input = (food, eaten, 2000)
    answer = 782
    fn_name = "allowed_calories"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(food, eaten, 2000)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90


@t.passed(containsCalories)
@t.test(2)
def testCalories2(test):
    food = {"banana": 88, "apple": 52, "nuts": 606, "chocolate": 545, "salmon": 208, "smoothie": 36, "fries": 322, "sandwich": 265}
    eaten = ["apple", "nuts", "chocolate"]
    input = (food, eaten, 2300)
    answer = 407
    fn_name = "allowed_calories"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(food, eaten, 2300)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90


@t.passed(containsCalories)
@t.test(3)
def testCalories3(test):
    food = {"banana": 88, "apple": 52, "nuts": 606, "chocolate": 545, "salmon": 208, "smoothie": 36, "fries": 322, "sandwich": 265}
    eaten = []
    input = (food, eaten, 1900)
    answer = 1330
    fn_name = "allowed_calories"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(food, eaten, 1900)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90


@t.test(4)
def containsStartEnd(test):
    has_function(test, _fileName, "starts_and_ends", ["text"])


@t.passed(containsStartEnd)
@t.test(5)
def testStartEnd1(test):
    _input = "I really enjoy eating an apple more than a banana"
    _answer = ['I', 'apple', 'a']
    _fn_name = "starts_and_ends"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.passed(containsStartEnd)
@t.test(6)
def testStartEnd2(test):
    _input = "You make orange houses for a living and your name is Eva"
    _answer = ['orange', 'a', 'Eva']
    _fn_name = "starts_and_ends"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.test(7)
def containsDifferent_ranking(test):
    has_function(test, _fileName, "different_ranking", ['filename', 'party'])

@t.passed(containsDifferent_ranking)
@t.test(8)
def testDiffrank1(test):
    _input = [pd.read_csv('election_results_amsterdam_2022.csv'), 'GROENLINKS']
    _answer = True
    _fn_name = "different_ranking"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(pd.read_csv('election_results_amsterdam_2022.csv'), 'GROENLINKS')
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(election_results, 'GROENLINKS')"
    test.timeout = lambda : 90

@t.passed(containsDifferent_ranking)
@t.test(9)
def testDiffrank2(test):
    _input = [pd.read_csv('election_results_amsterdam_2022.csv'), 'CDA']
    _answer = False
    _fn_name = "different_ranking"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(pd.read_csv('election_results_amsterdam_2022.csv'), 'CDA')
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(election_results, 'CDA')"
    test.timeout = lambda : 90
