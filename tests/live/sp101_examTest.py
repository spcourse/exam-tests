from checkpy import *
import typing

only("sp101_exam.py")


######## Q2 ########

fun1_def = (declarative
    .function("remove_words_with_letter")
    .params("text", "forbidden_letter")
    .returnType(str)
)
sentence = "I am not very good at these funny little word games."

@test()
def test1_1():
    state = fun1_def.call(sentence, "e")()
    output = state.returned.strip(" ./,';!?'")
    assert output == "I am not good at funny word"

@test()
def test1_2():
    state = fun1_def.call(sentence, "a")()
    output = state.returned.strip(" ./,';!?'")
    assert output == "I not very good these funny little word"

######## Q2 ########


fun2_def = (declarative
    .function("longest_repetition")
    .params("numbers")
    .returnType(int)
)

test2_1 = test()(fun2_def
    .call([1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1])
    .returns(6)
)

test2_2 = test()(fun2_def
    .call([1, 1, 3, 3, 3, 3, 4, 4, 4])
    .returns(4)
)




######## Q3 ########


fun3_def = (declarative
    .function("hatcolor_frequency")
    .params("peoples_hatcolor")
    .returnType(dict)
)

peoples_hatcolor = {
    "Janeth":"black",
    "Berto":"green",
    "Gulnaz":"purple",
    "Frey":"pink",
    "Suman":"green",
    "Rabi":"red",
    "Jayesh":"green",
    "Callan":"pink",
    "Dzenan":"yellow",
    "Leonardo":"pink"
}

test3_1 = test()(fun3_def
    .call(peoples_hatcolor)
    .returns({'black': 1, 'green': 3, 'purple': 1, 'pink': 3, 'red': 1, 'yellow': 1})
)
