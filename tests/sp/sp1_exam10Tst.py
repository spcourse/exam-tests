from checkpy import *
import typing

# only("sp1_exam10.py")
download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("converge")
    .params("n")
    .returnType(typing.List[float])
)

test1_1 = test()(fun1_def.call(5).returns([0, 100, 50.0, 75.0, 62.5, 68.75]))
test1_2 = test()(fun1_def.call(10).returns([0, 100, 50.0, 75.0, 62.5, 68.75, 65.625, 67.1875, 66.40625, 66.796875, 66.6015625]))


######## Q2 ########

fun2_def = (declarative
    .function("longest_word")
    .params("text")
    .returnType(str)
)

test2_1 = test()(fun2_def.call("Hippopotomonstrosesquippedaliophobia is the fear of long words.").returns("Hippopotomonstrosesquippedaliophobia"))
test2_2 = test()(fun2_def.call("Those lazy lizards are lying like lumps in the leaves.").returns("lizards"))


######## Q3 ########

fun3_def = (declarative
    .function("biggest_win_per_year")
    .params("filename")
    .returnType(typing.List[int])
)

test3_1 = test()(fun3_def.call("barca.txt").returns([8, 7, 7, 7]))
test3_2 = test()(fun3_def.call("barca_short.txt").returns([8]))
