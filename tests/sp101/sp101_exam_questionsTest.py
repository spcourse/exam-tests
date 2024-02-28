from checkpy import *
import typing

only("sp101_exam_questions.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("twoish")
    .params("n")
    .returnType(float)
)

test1_1 = test()(fun1_def.call(2).returns(approx(1.5, abs=0.01)))
test1_2 = test()(fun1_def.call(10).returns(approx(1.998046875, abs=0.01)))


######## Q2 ########

fun2_def = (declarative
    .function("hamming_distance")
    .params("text1", "text2")
    .returnType(int)
)

test2_1 = test()(fun2_def.call("Norwegian Wood", "Norwegian Fjord").returns(1))
test2_2 = test()(fun2_def.call(
    "I love deadlines. I love the whooshing noise they make as they go by.",
    "I LOVE pizza. I love the round shape they have.").returns(6))
