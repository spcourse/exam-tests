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
def containsCollatz(test):
    has_function(test, _fileName, 'collatz', ['number'])

@t.passed(containsCollatz)
@t.test(1)
def testCollatz(test):
    inputs = [3, 16]
    answers = [[10, 5, 16, 8, 4, 2, 1], [8, 4, 2, 1]]
    fn_name = 'collatz'

    def testMethod():
        for inp, ans in zip(inputs, answers):
            fn = lib.getFunction(fn_name, _fileName)
            out = fn(inp)

            if out == ans:
                continue
            else:
                return False, f"Incorrect answer for input {inp}"

        return True, f"Correct answer for inputs {inputs}"

    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({inputs[0]}) and {fn_name}({inputs[1]})"
    test.timeout = lambda : 90

@t.test(2)
def containsPasswords(test):
    has_function(test, _fileName, 'check_passwords', ['passwords'])

@t.passed(containsPasswords)
@t.test(3)
def testPasswords(test):
    inp = ["secret", "strawberry", "sinkhole234", "1bigbeard", "butterknife", "abcdefg8", "aabbccdd18", "1two"]
    answer = [False, False, True, True, False, True, False, False]
    fn_name = 'check_passwords'

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
def containsBTTS(test):
    has_function(test, _fileName, 'both_teams_to_score', ['filename'])

@t.passed(containsBTTS)
@t.test(5)
def testBTTS(test):
    inputs = ['barca_short.txt', 'barca.txt']
    answers = [0.5, 0.57]
    fn_name = 'both_teams_to_score'

    def testMethod():
        for inp, ans in zip(inputs, answers):
            fn = lib.getFunction(fn_name, _fileName)
            out = fn(inp)

            if out == ans:
                continue
            else:
                return False, f"Incorrect answer for input {inp}"

        return True, f"Correct answer for inputs {inputs}"

    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({inputs[0]}) and {fn_name}({inputs[1]})"
    test.timeout = lambda : 90
