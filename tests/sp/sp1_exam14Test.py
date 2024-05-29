from checkpy import *
import typing

only("sp1_exam14.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("get_to_n")
    .params("n")
    .returnType(list)
)

test1_1 = test()(fun1_def.call(8).returns([2, 6, 18, 16, 14, 12, 10, 8]))
test1_2 = test()(fun1_def.call(28).returns([2, 6, 18, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28]))

######## Q2 ########

fun2_def = (declarative
    .function("increasing_word_length")
    .params("text")
    .returnType(list)
)
sentence = "I am not very good at these funny little word games."

test2_1 = test()(fun2_def.call(sentence).returns(['I', 'am', 'not', 'very', 'these', 'little', 'games']))


######## Q4 ########

fun3_def = (declarative
    .function("sub_min")
    .params("numbers")
    .returnType(list)
)

test3_1 = test()(fun3_def.call([3,6,2,4]).returns([1, 4, 0, 2]))


######## Q4 ########

fun4_def = (declarative
    .function("total_barca_goals_in_month")
    .params("filename", "month")
    .returnType(int)
)

test4_1 = test()(fun4_def.call("barca.txt",8).returns(20))
test4_2 = test()(fun4_def.call("barca_short.txt",8).returns(5))
