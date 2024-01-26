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
def containsBiggest_divisor(test):
    has_function(test, _fileName, "biggest_divisor", ['n'])

@t.passed(containsBiggest_divisor)
@t.test(1)
def testBiggest_divisor1(test):
    _input = 80
    _answer = 40
    _fn_name = "biggest_divisor"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.passed(containsBiggest_divisor)
@t.test(2)
def testBiggest_divisor2(test):
    _input = 15
    _answer = 5
    _fn_name = "biggest_divisor"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90


@t.test(3)
def containsMost_divisors(test):
    has_function(test, _fileName, "most_divisors", ['n'])

@t.passed(containsMost_divisors)
@t.test(4)
def testMost_divisors1(test):
    _input = 29
    _answer = 24
    _fn_name = "most_divisors"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.passed(containsMost_divisors)
@t.test(5)
def testMost_divisors1(test):
    _input = 20
    _answer = 12
    _fn_name = "most_divisors"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.test(6)
def containsRepeated_length_count(test):
    has_function(test, _fileName, "repetition_count", ['text'])

@t.passed(containsRepeated_length_count)
@t.test(7)
def testRepeated_length_count2(test):
    _input = "x aa aa aa y bb bb"
    _answer = 3
    _fn_name = "repetition_count"

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

@t.passed(containsRepeated_length_count)
@t.test(8)
def testRepeated_length_count2(test):
    _input = "x aa l aa aa y bb bb"
    _answer = 2
    _fn_name = "repetition_count"

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

@t.test(10)
def containsAverage_goal_difference(test):
    has_function(test, _fileName, "average_goal_difference", ['filename'])

@t.passed(containsAverage_goal_difference)
@t.test(11)
def testAverage_goal_difference1(test):
    _input = 'barca.txt'
    _fn_name = "average_goal_difference"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if round(_output, 3) == 1.991:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90

@t.passed(containsAverage_goal_difference)
@t.test(12)
def testAverage_goal_difference2(test):
    _input = 'barca_short.txt'
    _fn_name = "average_goal_difference"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(_input)
        if round(_output,3) == 3.250:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90
