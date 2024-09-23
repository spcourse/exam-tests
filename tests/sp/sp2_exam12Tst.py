from checkpy import *
import typing

only("sp2_exam12.py")
download("films.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/films.csv")


######## Q1 ########

fun1_def = (declarative
    .function("count_unique_words")
    .params("text")
    .returnType(dict)
)

text = "It was a place where up is down, and down is up."

test1_1 = test()(fun1_def.call(text).returns({'it': 1, 'was': 1, 'a': 1, 'place': 1, 'where': 1, 'up': 2, 'is': 2, 'down': 2, 'and': 1}))


######## Q2 ########

fun2a_def = (declarative
    .function("rename_keys")
    .params("dict", "key_mapping")
    .returnType(dict)
)

original_dict = {'apple': 5, 'banana': 3, 'orange': 8}
key_mapping = {'apple': 'red_apple', 'banana': 'yellow_banana'}

test2_1 = test()(fun2a_def.call(original_dict, key_mapping).returns({'red_apple': 5, 'yellow_banana': 3, 'orange': 8}))


######## Q3 ########

fun3_def = (declarative
    .function("years_with_seven_awards")
    .params("filename")
    .returnType(list)
)

test3_1 = test()(fun3_def.call("films.csv").returns([1974, 1982, 1985]))
