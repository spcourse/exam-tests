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
def containsFibonacci(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "fibonacci")
	test.description = lambda : "Defines the function fibonacci"
	test.timeout = lambda : 10

@t.passed(containsFibonacci)
@t.test(1)
def testFibonacci1(test):
    input = 12
    answer = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    fn_name = "fibonacci"

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
@t.passed(containsFibonacci)
@t.test(2)
def testFibonacci2(test):
    _input = 1
    _answer = [1]
    _fn_name = "fibonacci"

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
def containsCount_elements(test):
    has_function(test, _fileName, "count_elements", ["text"])


@t.passed(containsCount_elements)
@t.test(7)
def testCount_elements1(test):
    _input = "Bananas, oranges, apples, strawberries, grapes."
    _answer = 2
    _fn_name = "count_elements"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn("Bananas, oranges, apples, strawberries, grapes.")
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.passed(containsCount_elements)
@t.test(8)
def testCount_elements2(test):
    _input = "Giraffe, monkey, Orang oetang, Elephant, Zebra, Lizzard, owl, 123."
    _answer = 3
    _fn_name = "count_elements"

    def testMethod():
        _fn = lib.getFunction(_fn_name, _fileName)
        _output = _fn("Giraffe, monkey, Orang oetang, Elephant, Zebra, Lizzard, owl, 123.")
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.test(9)
def containsShutouts(test):
    has_function(test, _fileName, "shutouts", ['filename'])

@t.passed(containsShutouts)
@t.test(10)
def testLongest_streak1(test):
    _input = 'barca.txt'
    _answer = 40
    _fn_name = "shutouts"

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

@t.passed(containsShutouts)
@t.test(11)
def testShutouts2(test):
    _input = 'barca_short.txt'
    _answer = 2
    _fn_name = "shutouts"

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
