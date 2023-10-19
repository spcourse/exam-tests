from checkpy import *
import typing

######## Q1 ########

# Only PDP

######## Q2 ########

fun2_def = (declarative
    .function("is_palindrome")
    .params("word")
    .returnType(bool)
)

test2_1 = test()(fun2_def.call("racecar").returns(True))
test2_2 = test()(fun2_def.call("hello").returns(False))
test2_3 = test()(fun2_def.call("level").returns(True))


######## Q3 ########

fun3_def = (declarative
    .function("calculate_growth")
    .params("population_1", "population_2")
    .returnType(dict)
)

population_1 = {
    'New York': 8500000,
    'Los Angeles': 3900000,
    'Chicago': 2700000,
    'Houston': 2400000,
    'Phoenix': 1700000
}

population_2 = {
    'New York': 8700000,
    'Los Angeles': 4000000,
    'Chicago': 2800000,
    'Houston': 2300000,
    'Dallas': 1500000
}

expected = {'Houston': -100000, 'Chicago': 100000, 'Los Angeles': 100000, 'New York': 200000}

test3_1 = test()(fun3_def.call(population_1, population_2).returns(expected))
