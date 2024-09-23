from checkpy import *
import typing

only("sp1_exam11.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")
download("barca_short.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca_short.txt")

######## Q1 ########

fun1_def = (declarative
    .function("bounce")
    .params("n")
    .returnType(typing.List[float])
)

test1_1 = test()(fun1_def.call(20).returns([1.0, 4.0, 16.0, 64.0, 256.0, 128.0, 64.0, 32.0, 16.0, 8.0, 4.0, 2.0, 1.0, 4.0, 16.0, 64.0, 256.0, 128.0, 64.0, 32.0]))


######## Q2 ########

fun2_def = (declarative
    .function("swap_words")
    .params("text")
    .returnType(str)
)

test2_1 = test()(fun2_def.call("Why is a raven like a writing desk?").returns("is Why raven a a like desk? writing"))
test2_2 = test()(fun2_def.call("You can always take more than nothing.").returns("can You take always than more nothing."))


######## Q4 ########

fun3_def = (declarative
    .function("gregory_leibniz")
    .params("n")
    .returnType(float)
)

test3_1 = test()(fun3_def.call(1).returns(4))
test3_2 = test()(fun3_def.call(10).returns(3.0418396189294032))
test3_3 = test()(fun3_def.call(1000000).returns(3.1415916535897743))


######## Q4 ########

fun4_def = (declarative
    .function("home_advantage")
    .params("filename")
    .returnType(int)
)

test4_1 = test()(fun4_def.call("barca.txt").returns(15))
test4_2 = test()(fun4_def.call("barca_short.txt").returns(2))
