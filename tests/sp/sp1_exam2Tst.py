import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib


def sandbox():
    # https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt
    lib.require("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
    lib.require("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

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
def containsCumulative(test):
    has_function(test, _fileName, "cumulative", ['distances'])

@t.passed(containsCumulative)
@t.test(1)
def testCumulative(test):
    input = [19, 32, 7, 1, 5, 1]
    answer = [19, 51, 58, 59, 64, 65]
    fn_name = "cumulative"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90


@t.test(6)
def containsLongest_word_length(test):
    has_function(test, _fileName, "longest_word_length", ['text'])

@t.passed(containsLongest_word_length)
@t.test(7)
def testLongest_word_length(test):
    input = "The word 'longer', is not the longest in this sentence."
    answer = 8
    fn_name = "longest_word_length"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(\"{input}\")"
    test.timeout = lambda : 90

@t.test(9)
def containsHome_advantage(test):
    has_function(test, _fileName, "home_advantage", ['filename'])

@t.passed(containsHome_advantage)
@t.test(10)
def testHome_advantage(test):
    input = 'barca.txt'
    answer = 15
    fn_name = "home_advantage"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(\"{input}\")"
    test.timeout = lambda : 90
