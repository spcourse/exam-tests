from checkpy import *
import typing

only("ipbg_practice_exam.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("even")
    .params("numbers")
    .returnType(typing.List[float])
)

test1_1 = test()(fun1_def.call([1, 3, 4, 3, 2, 2, 1, 6]).returns([4, 2, 2, 6]))


######## Q2 ########

fun2_def = (declarative
    .function("swap_words")
    .params("text")
    .returnType(str)
)

test2_1 = test()(fun2_def.call("Why is a raven like a writing desk?").returns("is Why raven a a like desk? writing"))
test2_2 = test()(fun2_def.call("You can always take more than nothing.").returns("can You take always than more nothing."))


######## Q3 ########

fun3_def = (declarative
    .function("collatz")
    .params("n")
    .returnType(typing.List[float])
)

test3_1 = test()(fun3_def.call(12).returns([12, 6, 3, 10, 5, 16, 8, 4, 2, 1]))
test3_2 = test()(fun3_def.call(3).returns([3, 10, 5, 16, 8, 4, 2, 1]))


######## Q4 ########

fun4_def = (declarative
    .function("home_advantage")
    .params("filename")
    .returnType(int)
)

test4_1 = test()(fun4_def.call("barca.txt").returns(15))
test4_2 = test()(fun4_def.call("barca_short.txt").returns(2))
