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
def containsFizzy(test):
    # has_function(test, _fileName, "fizzy", ['n'])
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "fizzy")
	test.description = lambda : "defines the function fizzy"
	test.timeout = lambda : 10

@t.passed(containsFizzy)
@t.test(1)
def testFizzy1(test):
    input = 100
    answer = [15, 21, 30, 42, 45, 60, 63, 75, 84, 90]
    fn_name = "fizzy"

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

#
@t.passed(containsFizzy)
@t.test(2)
def testFizzy2(test):
    _input = 50
    _answer = [15, 21, 30, 42, 45]
    _fn_name = "fizzy"

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
def containsPrint_decomposition(test):
    has_function(test, _fileName, "print_decomposition", ['n'])

@t.test(6)
def containsFilter_words_starting_with(test):
    has_function(test, _fileName, "filter_words_starting_with", ['text', 'letter'])

@t.passed(containsFilter_words_starting_with)
@t.test(7)
def testFilter_words_starting_with1(test):
    _input = "David Donald Doo dreamed a dozen doughnuts and a duck-dog, too.", 'd'
    _answer = ['David', 'Donald', 'Doo', 'dreamed', 'dozen', 'doughnuts', 'duck-dog']
    _fn_name = "filter_words_starting_with"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(*_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.passed(containsFilter_words_starting_with)
@t.test(8)
def testFilter_words_starting_with2(test):
    _input = "Those lazy lizards are lying like lumps in the leaves.", 'l'
    _answer = ['lazy', 'lizards', 'lying', 'like', 'lumps', 'leaves']
    _fn_name = "filter_words_starting_with"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn(*_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.test(9)
def containsLongest_streak(test):
    has_function(test, _fileName, "longest_streak", ['filename'])

@t.passed(containsLongest_streak)
@t.test(10)
def testLongest_streak1(test):
    _input = 'barca.txt'
    _answer = 13
    _fn_name = "longest_streak"

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

@t.passed(containsLongest_streak)
@t.test(11)
def testLongest_streak2(test):
    _input = 'barca_short.txt'
    _answer = 1
    _fn_name = "longest_streak"

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
