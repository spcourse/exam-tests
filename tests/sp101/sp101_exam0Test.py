from checkpy import *
import typing

only("sp101_exam0.py")

######## Q1 ########

fun1_def = (declarative
    .function("cumulative")
    .params("distances")
    .returnType(list)
)

distances = [19, 32, 7, 1, 5, 1]

test1_1 = test()(fun1_def.call(distances).returns([19, 51, 58, 59, 64, 65]))

######## Q2 ########

fun2_def = (declarative
    .function("filter_words_starting_with")
    .params("text", "letter")
    .returnType(list)
)

text1 = "David Donald Doo dreamed a dozen doughnuts and a duck-dog, too."
result1 = ['David', 'Donald', 'Doo', 'dreamed', 'dozen', 'doughnuts', 'duck-dog']
text2 = "Those lazy lizards are lying like lumps in the leaves."
result2 = ['lazy', 'lizards', 'lying', 'like', 'lumps', 'leaves']

test2_1 = test()(fun2_def.call(text1, "d").returns(result1))
test2_2 = test()(fun2_def.call(text2, "l").returns(result2))


######## Q4 ########

fun3_def = (declarative
    .function("euros_to_percentage")
    .params("expenses")
    .returnType(dict)
)

expenses = {'rent': 100, 'utlities': 150,
            'food': 50, 'social activities': 100,
            'internet + netflix + spotify': 40, 'phone': 60}
result = {'rent': 20.0, 'utlities': 30.0, 'food': 10.0, 'social activities': 20.0,
          'internet + netflix + spotify': 8.0, 'phone': 12.0}

test3_1 = test()(fun3_def.call(expenses).returns(result))
