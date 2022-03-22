import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import pandas as pd


def sandbox():
    lib.require("election_results_amsterdam_2022.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/election_results_amsterdam_2022.txt")

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
def containsEuros_to_percentage(test):
    has_function(test, _fileName, "euros_to_percentage", ['expenses'])


@t.passed(containsEuros_to_percentage)
@t.test(1)
def testFizzy1(test):
    input = {'rent': 735, 'utlities': 221,
             'food': 167, 'social activities': 185,
             'internet + netflix + spotify': 58, 'phone': 25}
    answer = {'rent': 52.83968368080517, 'utlities': 15.88785046728972,
              'food': 12.005751258087706, 'social activities': 13.299784327821712,
              'internet + netflix + spotify': 4.169662113587347, 'phone': 1.7972681524083394}
    fn_name = "euros_to_percentage"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)
        if {key:round(value) for key, value in output.items()} == {key:round(value) for key, value in answer.items()}:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90


@t.test(6)
def containsHalf_double(test):
    has_function(test, _fileName, "half_double", ['my_list'])

@t.passed(containsHalf_double)
@t.test(7)
def testFilter_words_starting_with1(test):
    input = [1, 2, 3, 4, 5]
    answer = [2, 1, 6, 2, 10]
    fn_name = "half_double"

    def testMethod():
        fn = lib.getFunction(fn_name, fileName)
        output = fn(input)
        if output == answer:
            return True, f"Correct answer for input {input}!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90

@t.test(9)
def containsTop_candidates(test):
    has_function(test, _fileName, "top_candidates", ['election_results'])

@t.passed(containsTop_candidates)
@t.test(10)
def testFilter_words_starting_with1(test):
    input = pd.read_csv('election_results_amsterdam_2022.csv')
    print(input)
    parties = ['1 GROENLINKS', '1 GROENLINKS',
               '13 JA21', '2 D66', '2 D66', '25 Volt',
               '3 VVD', '4 Partij van de Arbeid (P.v.d.A.)',
               '5 SP (Socialistische Partij)',
               '6 Partij voor de Dieren']
    candidate_nrs = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    fn_name = "top_candidates"

    def testMethod():
        fn = lib.getFunction(fn_name, fileName)
        output = fn(input)
        parties_outp = sorted(output['party'].to_list())
        candidate_nrs_outp = sorted(top['candidate_number'].to_list())
        if parties_outp == parties and candidate_nrs_outp == candidate_nrs:
            return True, f"Correct answer!"
        else:
            return False, f"Incorrect answer."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}({input})"
    test.timeout = lambda : 90
