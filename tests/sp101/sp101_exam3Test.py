from checkpy import *
import typing

only("sp101_exam3.py")

######## Q1 ########


fun1_def = (declarative
    .function("normalize")
    .params("numbers")
    .returnType(list)
)

test1_1 = test()(fun1_def.call([0,4,3,5]).returns([-3.0, 1.0, 0.0, 2.0]))


######## Q2 ########

fun2_def = (declarative
    .function("cut")
    .params("text", "cut_words")
    .returnType(str)
)
sentence = "I am not very good at these funny little word games."
@test()
def test2_1():
    state = fun2_def.call(sentence, ["i", "am", "at", "these"])()
    output = state.returned.strip(" ./,';!?'")
    assert output == "not very good funny little word games"


######## Q3 ########


fun3_def = (declarative
    .function("word_stats")
    .params("text")
    .returnType(dict)
)
sentence = "I am not very good at these funny little word games."
test3_1 = test()(fun3_def.call(sentence).returns({1: 1, 2: 2, 3: 1, 4: 3, 5: 3, 6: 1}))
