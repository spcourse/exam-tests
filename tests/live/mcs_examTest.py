from checkpy import *

only('mcs_exam.py')

class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip()

    def __eq__(self, other_string):
        other_string = other_string.strip()
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string)

######## Q1 ########

fun1 = test()(declarative
    .function("fizzy")
    .params("n")
    .returnType(list)
    .call(100)
    .returns([15, 21, 30, 42, 45, 60, 63, 75, 84, 90])
)

######## Q2 ########

fun2 = test()(declarative
    .function("count_elements")
    .params("text")
    .returnType(int)
    .call("Bananas, oranges, apples, strawberries, grapes.")
    .returns(2)
)

######## Q3 ########

fun3 = test()(declarative
    .function("find_non_reflexive_pairs")
    .params("numbers")
    .returnType(list)
    .call([1, 2, 3, 2])
    .returns([(1, 2), (1, 3), (1, 2), (2, 1), (2, 3), (3, 1), (3, 2), (3, 2), (2, 1), (2, 3)])
)

######## Q4 ########

fun4 = test()(declarative
    .function("auto_reformat")
    .params("text")
    .returnType(str)
    .call("hello,   world. This tExt NEeds   some cleaning    up.   ")
    .returns(ApproxString("Hello, world. This text Needs some cleaning up."))
)
######## Q5 ########

ingredients_banana_bread = {"banana (pcs)": 3, "butter (g)": 80, "baking soda (tsp)": 0.5, "sugar (g)": 150, "egg (pcs)": 1, "flour (g)": 200}
ingredients_brownies = {"butter (g)": 225, "sugar (g)": 450, "egg (pcs)": 5, "flour (g)": 110, "chocolate (g)": 140, "cocoa powder (g)": 55}

fun5 = test()(declarative
    .function("combine_ingredient_dictionaries")
    .params("dictionary1", "dictionary2")
    .returnType(dict)
    .call(ingredients_banana_bread, ingredients_brownies)
    .returns({'banana (pcs)': 3, 'butter (g)': 305, 'baking soda (tsp)': 0.5,
        'sugar (g)': 600, 'egg (pcs)': 6, 'flour (g)': 310, 'chocolate (g)': 140,
        'cocoa powder (g)': 55})
)
######## Q6 ########

square2 = [
    [16, 2,  3, 13],
    [5, 11, 10,  8],
    [9,  7,  6, 12],
    [4, 14, 15,  1]
]

fun6 = test()(declarative
    .function("magic_square")
    .params("square")
    .returnType(bool)
    .call(square2)
    .returns(True)
)
