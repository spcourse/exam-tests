from checkpy import *
import typing

only("sp1_exam16.py")

download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")

######## Q1 ########

fun1_def = (declarative
    .function("silly_square_root")
    .params("n", "step_size")
    .returnType(float)
)

test1_1 = test()(fun1_def
    .call(9, 0.001)
    .returns(approx(3.0009999999997805, abs=1e-3)))

test1_1 = test()(fun1_def
    .call(2, 0.0001)
    .returns(approx(1.4142999999998607, abs=1e-3)))

######## Q2 ########

fun2_def = (declarative
    .function("censor_long_words")
    .params("phrase", "max_length")
    .returnType(str)
)

@test()
def test2_1():
    state = fun2_def.call("The sudden shift from calm to chaos left everyone feeling confused.", 5)()
    output = state.returned.strip()
    assert output == "The ###### shift from calm to chaos left ######## ####### #########"

######## Q4 ########

fun3_def = (declarative
    .function("combine_pairs")
    .params("list1", "list2")
    .returnType(list)
)


test3_1 = test()(fun3_def
    .call(["a", "b", "c"], ["1", "2"])
    .returns(['a1', 'a2', 'b1', 'b2', 'c1', 'c2']))



######## Q4 ########

fun4_def = (declarative
    .function("best_year")
    .params("filename")
    .returnType(tuple)
)

@test()
def test4_1():
    state = fun4_def.call("barca.txt")()
    output = state.returned
    assert len(output) == 2, "best_year() has to return two values: year, points"
    year, points = output
    assert int(year) == 12
    assert int(points) == 103
