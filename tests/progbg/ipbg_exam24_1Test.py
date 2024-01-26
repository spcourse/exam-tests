from checkpy import *
import typing

only("ipbg_exam24_1.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("clamp")
    .params("numbers", "min", "max")
    .returnType(typing.List[float])
)

test1_1 = test()(fun1_def.call([1, 2, 5, 3, 0, 18, -3, 1, 6, 9], 1, 6).returns([1, 2, 5, 3, 1]))

######## Q2 ########

fun2_def = (declarative
.function("gcd")
.params("number1", "number2")
.returnType(int)
)

test2_1 = test()(fun2_def.call(10, 6).returns(2))
test2_2 = test()(fun2_def.call(6, 12).returns(6))
test2_3 = test()(fun2_def.call(1000, 240).returns(40))

######## Q2 ########

fun3_def = (declarative
    .function("silly_abridge")
    .params("input_text", "step")
    .returnType(str)
)

alice = """Oh, how I wish I could shut up like a telescope! \
I think I could, if only I knew how to begin."""

test3_1 = test()(fun3_def.call(alice, 4).returns("Oh, how I I could shut like a telescope! think I could, only I knew to begin."))
test3_2 = test()(fun3_def.call(alice, 2).returns("Oh, I I shut like telescope! think could, only knew to"))




######## Q4 ########

fun4_def = (declarative
    .function("goals_against_valencia")
    .params("filename")
    .returnType(int)
)

test4_1 = test()(fun4_def.call("barca.txt").returns(14))
test4_2 = test()(fun4_def.call("barca_short.txt").returns(2))
