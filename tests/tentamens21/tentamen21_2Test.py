import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib


def sandbox():
	lib.require("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")

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
def containsDivisors(test):
    has_function(test, _fileName, "divisors", ['n'])

@t.passed(containsDivisors)
@t.test(1)
def testDivisors1(test):
    _input = 80
    _answer = [1, 2, 4, 5, 8, 10, 16, 20, 40, 80]
    _fn_name = "divisors"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.passed(containsDivisors)
@t.test(2)
def testDivisors2(test):
    _input = 1000
    _answer = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]
    _fn_name = "divisors"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90


@t.test(3)
def containsPerfectList(test):
    has_function(test, _fileName, "perfect_list", ['n'])

@t.passed(containsPerfectList)
@t.test(4)
def testPerfect1(test):
    _input = 29
    _answer = [0, 6, 28]
    _fn_name = "perfect_list"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.passed(containsPerfectList)
@t.test(5)
def testPerfect1(test):
    _input = 497
    _answer = [0, 6, 28, 496]
    _fn_name = "perfect_list"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}({_input})"
    test.timeout = lambda : 90

@t.test(6)
def containsAutocorrect(test):
    has_function(test, _fileName, "autocorrect", ['text'])

@t.passed(containsAutocorrect)
@t.test(7)
def testAutocorrect1(test):
    _input = "Fuzzy Wuzzy was a bear . Fuzzy Wuzzy had no hair.Fuzzy Wuzzy wasn’t fuzzy , was he ?"
    _answer = "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?"
    _fn_name = "autocorrect"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output.strip() == _answer.strip():
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.passed(containsAutocorrect)
@t.test(8)
def testAutocorrect2(test):
    _input = "My first program:Hello , world !"
    _answer = "My first program: Hello, world!"
    _fn_name = "autocorrect"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output.strip() == _answer.strip():
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90


@t.test(9)
def containsTotal_away_goals(test):
    has_function(test, _fileName, "total_away_goals", ['filename'])

@t.passed(containsTotal_away_goals)
@t.test(10)
def testTotal_away_goals1(test):
    _input = 'barca.txt'
    _answer = 200
    _fn_name = "total_away_goals"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90

@t.passed(containsTotal_away_goals)
@t.test(11)
def testTotal_away_goals2(test):
    _input = 'barca_short.txt'
    _answer = 13
    _fn_name = "total_away_goals"

    _fn = lib.getFunction(_fn_name, _fileName)
    def testMethod():
        _output = _fn(_input)
        if _output == _answer:
            return True, f"Correct answer for input {_input}!"
        else:
            return False, f"Incorrect answer for input {_input}."


    test.test = testMethod
    test.description = lambda : f"Testing {_fn_name}(\"{_input}\")"
    test.timeout = lambda : 90
