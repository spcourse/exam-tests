from checkpy import *
import typing

only("mcs_practice3.py")

fun_def = (declarative
    .function("sumodd")
    .params("numbers")
    .returnType(float)
)

test1 = test()(fun_def
    .call([1,2,3,1,2,3,3,4])
    .returns(11)
)



fun_def = (declarative
    .function("reverse_list")
    .params("lst")
    .returnType(list)
)

test2 = test()(fun_def
    .call(["he", "l", "lo"])
    .returns(['lo', 'l', 'he'])
)



fun_def = (declarative
    .function("longest_repetition")
    .params("lst")
    .returnType(int)
)

test3 = test()(fun_def
    .call([1, 2, 2, 5, 5, 5, "a", "a"])
    .returns(3)
)



fun_def = (declarative
    .function("combine_dicts")
    .params("dict1", "dict2")
    .returnType(dict)
)

test4 = test()(fun_def
    .call({"a": 9, "b": 22, "c": 8}, {"x": 2, "b": 18, "y": 3})
    .returns({'a': 9, 'b': [22, 18], 'c': 8, 'x': 2, 'y': 3})
)



fun_def = (declarative
    .function("newtons_method_square_root_t")
    .params("n", "threshold")
    .returnType(float)
)

test5 = test()(fun_def
    .call(9, 0.01)
    .returns(approx(3.00009155413138, abs=0.001))
)




fun_def = (declarative
    .function("generate_1x1_grid")
    .params("step")
    .returnType(list[tuple,...])
)


@test()
def test6():
    output = fun_def.call(0.5)().returned
    assert set(output) == {(0, 0), (0, 0.5), (0, 1.0), (0.5, 0),
        (0.5, 0.5), (0.5, 1.0), (1.0, 0), (1.0, 0.5), (1.0, 1.0)}
