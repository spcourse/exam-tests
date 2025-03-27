from checkpy import *
import typing

only("sp1_exam3.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")

######## Q1 ########

fun1_def = (declarative
    .function("approximate_ln_2")
    .params("n")
    .returnType(float)
)

test1_1 = test()(fun1_def
    .call(10)
    .returns(approx(0.64563, abs=1e-3)))

test1_2 = test()(fun1_def
    .call(1000)
    .returns(approx(0.69265, abs=1e-3)))

######## Q2 ########

fun2_def = (declarative
    .function("find_capitalized_words")
    .params("text", "n")
    .returnType(list[str])
)

input_text = """TILL Elizabeth entered the drawing-room at Netherfield, and looked
in vain for Mr. Wickham among the cluster of red coats there assembled, a doubt of
his being present had never occurred to her."""

test2_1 = test()(fun2_def
    .call(input_text, 4)
    .returns(['TILL', 'Elizabeth', 'Netherfield,', 'Mr.']))


######## Q3 ########

fun3_def = (declarative
    .function("most_vowels")
    .params("word_lst")
    .returnType(str)
)

test3_1 = test()(fun3_def
    .call(["THIS", "List", "CONTAINS", "A", "Number", "Of", "WORDS!!!!"])
    .returns("CONTAINS"))

test3_2 = test()(fun3_def
    .call(["This", "list", "too!"])
    .returns("too!"))

######## Q4 ########

fun4_def = (declarative
    .function("percentage_decisive_games")
    .params("filename")
    .returnType(float)
)

test4_1 = test()(fun4_def
    .call("barca.txt")
    .returns(approx(36.84, abs=1e-1)))
