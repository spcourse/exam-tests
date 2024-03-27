from checkpy import *
import typing

only("sp101_exam1.py")

######## Q1 ########

fun1_def = (declarative
    .function("even_sum")
    .params("numbers")
    .returnType(int)
)

test1_1 = test()(fun1_def.call([1, 2, 3, 4, 5, 6, 7]).returns(12))
test1_2 = test()(fun1_def.call([9, 3, 1]).returns(0))
test1_3 = test()(fun1_def.call([2, 4, 3, 6, 7, 12]).returns(24))

######## Q2 ########

fun2_def = (declarative
    .function("remove_long_words")
    .params("text", "max_length")
    .returnType(str)
)

text1 = "Why, sometimes I've believed as many as six impossible things before breakfast."
text2 = "Who in the world am I? Ah, that's the great puzzle!"

@test()
def test2_1():
    state = fun2_def.call(text1, 8)()
    output = state.returned.strip()
    assert output == "Why I've believed as many as six things before"

@test()
def test2_2():
    state = fun2_def.call(text2, 1)()
    output = state.returned.strip(" ?\n")
    assert output == "I"

######## Q4 ########

fun3_def = (declarative
    .function("unique_value_counter")
    .params("lst")
    .returnType(dict)
)

values = ["a", "b", "a", "hello", "hello", "a"]

test3_1 = test()(fun3_def.call(values).returns({'a': 3, 'b': 1, 'hello': 2}))
