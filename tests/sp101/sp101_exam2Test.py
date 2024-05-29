from checkpy import *
import typing

only("sp101_exam2.py")

######## Q1 ########


fun1_def = (declarative
    .function("sub_min")
    .params("numbers")
    .returnType(list)
)

test1_1 = test()(fun1_def.call([3,6,2,4]).returns([1, 4, 0, 2]))


######## Q2 ########

fun2_def = (declarative
    .function("increasing_word_length")
    .params("text")
    .returnType(list)
)
sentence = "I am not very good at these funny little word games."

test2_1 = test()(fun2_def.call(sentence).returns(['I', 'am', 'not', 'very', 'these', 'little', 'games']))

######## Q3 ########


fun3_def = (declarative
    .function("bad_translator")
    .params("text", "translation")
    .returnType(str)
)


english_french_dict = {
    "i": "je",
    "ran": "courait",
    "into": "dans",
    "a": "un",
    "the": "le",
    "vague": "vague",
    "wave": "vague"
}

@test()
def test3_1():
    state = fun3_def.call("The vague wave", english_french_dict)()
    output = state.returned.strip(" ./,';!?'")
    assert output == "Le vague vague"

@test()
def test3_2():
    state = fun3_def.call("I ran into a problem", english_french_dict)()
    output = state.returned.strip(" ./,';!'")
    assert output == "Je courait dans un ???"
