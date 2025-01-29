from checkpy import *
import typing

only("ipbg_exam25_0.py")

class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip()

    def __eq__(self, other_string):
        other_string = other_string.strip()
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string)

class UnorderedList:
    def __init__(self, base_list):
        self._base_list = sorted(base_list)

    def __eq__(self, other_list):
        other_list = sorted(other_list)
        return self._base_list == other_list

    def __repr__(self):
        return repr(self._base_list)

######## Q1 ########

fun1_def = (declarative
    .function("fuz")
    .params("n")
    .returnType(list[int])
)

test1_1 = test()(fun1_def.call(35).returns([3, 5, 6, 9, 10, 12, 18, 20, 21, 24, 25, 27, 33]))
test1_2 = test()(fun1_def.call(10).returns([3, 5, 6, 9]))

######## Q2 ########

fun2def = (declarative
    .function("count_elements")
    .params("text")
    .returnType(int)
)

test2_1 = test()(fun2def.call("Bananas, oranges, apples, strawberrys, grapes.").returns(2))
test2_2 = test()(fun2def.call("ooo,oo,o,b,b").returns(3))


######## Q3 ########

fun3_def = (declarative
    .function("gcd")
    .params("number1", "number2")
    .returnType(int)
)


test3_1 = test()(fun3_def.call(10, 6).returns(2))
test3_3 = test()(fun3_def.call(240, 1000).returns(40))


######## Q4 ########

fun4def = (declarative
    .function("auto_reformat")
    .params("text")
    .returnType(str)
)

test4_1 = test()(fun4def
    .call("hello,   world. This tExt NEeds   some cleaning    up.   ")
    .returns(ApproxString("Hello, world. This text Needs some cleaning up."))
)

test4_2 = test()(fun4def
    .call("i wAs jUsT gIvInG mYsElF sOmE gOoD aDvIcE.")
    .returns(ApproxString("I was just giving myself some good advice."))
)
######## Q5 ########


fun5def = (declarative
    .function("magic_square")
    .params("square")
    .returnType(bool)
)


square1 = [
    [16, 2,  3, 13],
    [5, 11, 10,  8],
    [9,  7,  6, 12],
    [4, 14, 15,  1]
]
test5_1 = test()(fun5def.call(square1).returns(True))
square2 = [
    [16, 3,  2, 13],
    [5, 11,  6,  8],
    [9,  7, 10, 12],
    [4, 14, 15,  1]
]
test5_2 = test()(fun5def.call(square2).returns(False))



fun6def = (declarative
    .function("coprimes")
    .params("n")
    .returnType(list[tuple[int, int]])
)

test6_1 = test()(fun6def.call(10).returns(UnorderedList([(4, 9), (8, 9)])))
test6_2 = test()(fun6def.call(20)
    .returns(UnorderedList([
        (4, 9), (4, 15), (8, 9),
        (8, 15), (9, 10), (9, 14),
        (9, 16), (14, 15), (15, 16)
    ]))
)
