import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import pandas as pd


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
def containsGroup_titles_by_genre(test):
    has_function(test, _fileName, "group_titles_by_genre", ['expenses'])


@t.passed(containsGroup_titles_by_genre)
@t.test(1)
def testGroup_titles_by_genre(test):
    input = {"Life of Pi": "Adventure",
             "One World The Water Dancer": "Fantasy",
             "The Three Musketeers": "Adventure",
             "To Kill a Mockingbird": "Classics",
             "Circe": "Fantasy",
             "The Call of the Wild": "Adventure",
             "Little Women": "Classics"}
    answer = {'Adventure': ['Life of Pi', 'The Three Musketeers', 'The Call of the Wild'],
              'Fantasy': ['One World The Water Dancer', 'Circe'],
              'Classics': ['To Kill a Mockingbird', 'Little Women']}
    fn_name = "group_titles_by_genre"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)
        if output == answer:
            return True, f"Correct answer!"
        else:
            return False, f"Incorrect answer for input {input}."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(...)"
    test.timeout = lambda : 90


@t.test(6)
def containsNo_vowel(test):
    has_function(test, _fileName, "no_vowel", ['my_list'])

@t.passed(containsNo_vowel)
@t.test(7)
def testNo_vowel(test):
    input = "I do not like words that end in vowels"
    answer = ['not', 'words', 'that', 'end', 'in', 'vowels']
    fn_name = "no_vowel"

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

@t.test(9)
def containsCompute_area(test):
    has_function(test, _fileName, "compute_area", ['election_results'])

@t.passed(containsCompute_area)
@t.test(10)
def testCompute_area(test):
    input = pd.read_csv('iris.csv')
    sepal_area = [14.01, 11.54, 11.81, 11.19, 14.13, 16.53, 12.28, 13.34, 10.02, 11.92, 15.68, 12.81, 11.3, 10.13, 18.21, 19.69, 16.53, 14.01, 17.0, 15.21, 14.41, 14.81, 13.0, 13.21, 12.81, 11.78, 13.34, 14.29, 13.88, 11.81, 11.68, 14.41, 16.74, 18.13, 11.92, 12.56, 15.11, 13.85, 10.36, 13.61, 13.74, 8.12, 11.05, 13.74, 15.21, 11.3, 15.21, 11.56, 15.39, 12.95, 17.58, 16.08, 16.79, 9.93, 14.29, 12.53, 16.32, 9.23, 15.02, 11.02, 7.85, 13.89, 10.36, 13.89, 12.75, 16.3, 13.19, 12.29, 10.71, 10.99, 14.82, 13.41, 12.36, 13.41, 14.57, 15.54, 14.95, 15.78, 13.66, 11.63, 10.36, 10.36, 12.29, 12.72, 12.72, 16.01, 16.3, 11.37, 13.19, 10.79, 11.23, 14.37, 11.84, 9.03, 11.87, 13.42, 12.98, 14.11, 10.01, 12.53, 16.32, 12.29, 16.72, 14.34, 15.31, 17.9, 9.62, 16.62, 13.15, 20.35, 16.33, 13.56, 16.01, 11.19, 12.75, 16.08, 15.31, 22.97, 15.72, 10.36, 17.33, 12.31, 16.92, 13.35, 17.36, 18.09, 13.63, 14.37, 14.07, 16.96, 16.27, 23.57, 14.07, 13.85, 12.45, 18.13, 16.81, 15.57, 14.13, 16.79, 16.3, 16.79, 12.29, 17.08, 17.36, 15.78, 12.36, 15.31, 16.55, 13.89]
    petal_area = [0.22, 0.22, 0.2, 0.24, 0.22, 0.53, 0.33, 0.24, 0.22, 0.12, 0.24, 0.25, 0.11, 0.09, 0.19, 0.47, 0.41, 0.33, 0.4, 0.35, 0.27, 0.47, 0.16, 0.67, 0.3, 0.25, 0.5, 0.24, 0.22, 0.25, 0.25, 0.47, 0.12, 0.22, 0.24, 0.19, 0.2, 0.11, 0.2, 0.24, 0.31, 0.31, 0.2, 0.75, 0.6, 0.33, 0.25, 0.22, 0.24, 0.22, 5.17, 5.3, 5.77, 4.08, 5.42, 4.59, 5.9, 2.59, 4.69, 4.29, 2.75, 4.95, 3.14, 5.17, 3.67, 4.84, 5.3, 3.22, 5.3, 3.37, 6.78, 4.08, 5.77, 4.43, 4.39, 4.84, 5.28, 6.67, 5.3, 2.75, 3.28, 2.9, 3.67, 6.41, 5.3, 5.65, 5.53, 4.49, 4.18, 4.08, 4.14, 5.06, 3.77, 2.59, 4.29, 3.96, 4.29, 4.39, 2.59, 4.18, 11.78, 7.61, 9.73, 7.91, 10.02, 10.88, 6.01, 8.9, 8.2, 11.97, 8.01, 7.9, 9.07, 7.85, 9.61, 9.57, 7.77, 11.57, 12.46, 5.89, 10.29, 7.69, 10.52, 6.92, 9.4, 8.48, 6.78, 6.92, 9.23, 7.28, 9.1, 10.05, 9.67, 6.01, 6.15, 11.01, 10.55, 7.77, 6.78, 8.9, 10.55, 9.21, 7.61, 10.65, 11.19, 9.39, 7.46, 8.16, 9.75, 7.21]

    candidate_nrs = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    fn_name = "compute_area"

    def testMethod():
        fn = lib.getFunction(fn_name, _fileName)
        output = fn(input)

        outp_petal_area = output['petal_area'].round(2).to_list()
        outp_sepal_area = output['sepal_area'].round(2).to_list()

        if sepal_area == outp_sepal_area and petal_area == outp_petal_area:
            return True, f"Correct answer!"
        else:
            return False, f"Incorrect answer."


    test.test = testMethod
    test.description = lambda : f"Testing {fn_name}(...)"
    test.timeout = lambda : 90
