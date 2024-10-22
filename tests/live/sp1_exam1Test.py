from checkpy import *
import typing

only("sp1_exam1.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("longest_word")
    .params("words")
    .returnType(str)
)

test1_1 = test()(fun1_def
    .call(['apple', 'banana', 'grapefruit', 'fig'])
    .returns('grapefruit'))

######## Q2 ########

fun2_def = (declarative
    .function("sum_squares_to")
    .params("value")
    .returnType(list)
)


test2_1 = test()(fun2_def
    .call(5)
    .returns([1, 4]))

test2_2 = test()(fun2_def
    .call(18)
    .returns([1, 4, 9, 16]))

######## Q4 ########

fun3_def = (declarative
    .function("print_pairs")
    .params("numbers", "target")
    .call([2, 3, 4, 5, 6], 7)
    .returns(None)
)

test3_1 = test()(fun3_def
    .stdoutRegex(r"[\s\S]*2 \+ 5 = 7", readable = "Expected '2 + 5 = 7' to be printed.")
)
test3_3 = test()(fun3_def
    .stdoutRegex(r"[\s\S]*3 \+ 4 = 7", readable = "Expected '3 + 4 = 7' to be printed.")
)

######## Q4 ########

fun4_def = (declarative
    .function("first_streak")
    .params("filename", "length")
    .returnType(str)
)

test4_1 = test()(fun4_def.call("barca.txt",6).returns("20/03/12"))
test4_2 = test()(fun4_def.call("barca_short.txt",1).returns("29/08/11"))
