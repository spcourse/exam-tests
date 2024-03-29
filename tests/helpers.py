from collections.abc import Iterable
import checkpy.assertlib as assertlib
import checkpy.lib as lib

class InvalidFunctionApplication(Exception):
    def __init__(self, message):
        self.message = message

ORDINALS = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
            '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
            '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th',
            '29th', '30th', '31st']


def test_direct_compare_fn(test, file_name, function_name, input, output, atol = None):
    def testMethod():
        try:
            _fn = lib.getFunction(function_name, file_name)
            _output = apply_function(_fn, input, [type(output)])
        except InvalidFunctionApplication as e:
            return False, e.message
        except Exception as e:
            return False, f"An error occured while running the function: \n {type(e).__name__}: {str(e)}"
        if atol == None:
            if _output != output:
                return False, f"Expected output: {output}, not {_output}"
        else:
            if not similar(_output,output,atol):
                return False, f"Expected output: {output}, not {_output}"


        return True, ""


    test.test = testMethod
    test.description = lambda : f"Test {function_name} with {input}"
    test.timeout = lambda : 90

def apply_function(fn, input, output_descr, check_none=True):
    number_of_return_values = len(output_descr)
    _output = fn(*input)
    if len(output_descr) == 1:
        if number_of_return_values != 1:
            raise InvalidFunctionApplication("Make sure to return only one value.")
        if check_none and _output == None:
            raise InvalidFunctionApplication("Function returns None. Tips: Does your function have a return? Do you try to return a print statement?")
        if type(_output) != output_descr[0]:
            raise InvalidFunctionApplication(f"Make sure the function {fname} returns a value of type {output_descr[0].__name__}.")
    else:
        if (type(_output) != tuple) or len(_output) != number_of_return_values:
            raise InvalidFunctionApplication(f"Make sure to return exactly {number_of_return_values} values.")
        for i, (expected_type, actual_value) in enumerate(zip(output_descr, _output)):
            if check_none and actual_value == None:
                raise InvalidFunctionApplication(f"The {ORDINALS[i]} return value is None.")
            if type(actual_value) != expected_type:
                raise InvalidFunctionApplication(f"Make sure the {ORDINALS[i]} return value is of type {expected_type.__name__}")

    return _output


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



def similar(v1, v2, atol):
    upper, lower =  (v2 + atol), (v2 - atol)
    return v1 < upper and v1 >= lower
