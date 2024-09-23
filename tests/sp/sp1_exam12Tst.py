from checkpy import *
import typing

only("sp1_exam12.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("fibonacci")
    .params("n")
    .returnType(int)
)

test1_1 = test()(fun1_def.call(7).returns(13))


######## Q2 ########

fun2_def = (declarative
    .function("classified")
    .params("text", "word")
    .returnType(str)
)
djinns = "Even if they are djinns I will get djinns that can outdjinn them."

@test()
def test2_1():
    state = fun2_def.call(djinns, "djinns")()
    output = state.returned.strip()
    assert output == "Even if they are ###### I will get ###### that can outdjinn them."

@test()
def test2_2():
    state = fun2_def.call(djinns, "even")()
    output = state.returned.strip()
    assert output == "#### if they are djinns I will get djinns that can outdjinn them."

######## Q4 ########

fun3_def = (declarative
    .function("newtons_method_square_root")
    .params("n", "steps")
    .returnType(float)
)

test3_1 = test()(fun3_def.call(9, 2).returns(approx(3.4, abs = 0.01)))
test3_2 = test()(fun3_def.call(9, 5).returns(approx(3.000000001396984, abs = 0.01)))
test3_3 = test()(fun3_def.call(16, 10).returns(approx(4.0, abs = 0.01)))


######## Q4 ########

fun4_def = (declarative
    .function("biggest_loss")
    .params("filename")
    .returnType(list)
)

test4_1 = test()(fun4_def.call("barca.txt").returns(['22/02/14', 'Sociedad', 1, 3]))
test4_2 = test()(fun4_def.call("barca_short.txt").returns(['10/09/11', 'Sociedad', 2, 2]))
