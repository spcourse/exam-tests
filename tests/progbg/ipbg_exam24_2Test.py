from checkpy import *
import typing

only("ipbg_exam24_2.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("sum_to")
    .params("n")
    .returnType(int)
)

test1_1 = test()(fun1_def.call(10).returns(5))
test1_2 = test()(fun1_def.call(1).returns(2))

######## Q2 ########

fun2_def = (declarative
.function("sum_divisors")
.params("number")
.returnType(int)
)

test2_1 = test()(fun2_def.call(10).returns(8))
test2_2 = test()(fun2_def.call(6).returns(6))
test2_3 = test()(fun2_def.call(1000).returns(1340))

######## Q2 ########

fun3_def = (declarative
    .function("find_word")
    .params("text", "word_to_find")
    .returnType(list[int])
)

djinns = "Even if they are djinns, I will get djinns that can outdjinn them."


test3_1 = test()(fun3_def.call(djinns, "djinns").returns([4, 8]))
test3_2 = test()(fun3_def.call(djinns, "even").returns([0]))




######## Q4 ########

fun4_def = (declarative
    .function("biggest_goal_difference")
    .params("filename")
    .returnType(list)
)

test4_1 = test()(fun4_def.call("barca.txt").returns(['17/09/11', 'Osasuna', 8, 0]))
test4_2 = test()(fun4_def.call("barca_short.txt").returns(['17/09/11', 'Osasuna', 8, 0]))
