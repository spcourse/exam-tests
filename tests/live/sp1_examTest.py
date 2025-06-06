from checkpy import *
import typing
import pandas as pd

only("sp1_exam.py")
download("barca.txt", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/barca.txt")


class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip().replace("\n", " ")

    def __eq__(self, other_string):
        other_string = other_string.strip().replace("\n", " ")
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string) + "[approximately]"


class ApproxDataFrame:
    def __init__(self, base_df):
        self._base_df = base_df

    def __eq__(self, other_df):
        return self._base_df.to_dict() == other_df.to_dict()

    def __repr__(self):
        return repr(self._base_df)

######## Q1 ########

fun1_def = (declarative
    .function("approximate_pi")
    .params("n")
    .returnType(float)
)

test1_1 = test()(fun1_def
    .call(10)
    .returns(approx(3.04184, abs=1e-4))
)

test1_2 = test()(fun1_def
    .call(1000)
    .returns(approx(3.14059, abs=1e-4))
)

####### Q2 ########

fun2_def = (declarative
    .function("until_lvl")
    .params("monsters_to_defeat", "xp_to_lvl")
    .returnType(list)
)

monsters_to_defeat = ["goblin", "rabbit", "goblin", "goblin", "friendly NPC", "drake", "goblin", "friendly NPC", "friendly NPC", "goblin"]

test2_1 = test()(fun2_def
    .call(monsters_to_defeat, 300)
    .returns(['goblin', 'rabbit', 'goblin', 'goblin', 'friendly NPC', 'drake', 'goblin'])
)

####### Q3 ########

fun3_def = (declarative
    .function("grocery_prices")
    .params("base_prices", "discount_percentages")
    .returnType(list)
)

base_prices = [7.50, 3.99, 2.99, 3.99, 4.50, 9.99, 7.69, 1.25]
discount_percentages = [0, 20, 25, 10, 0, 60, 15, 20]

discounted_prices = [7.5, 3.19, 2.24, 3.59, 4.5, 4.0, 6.54, 1.0]

test3_1 = test()(fun3_def
    .call(base_prices, discount_percentages)
    .returns(discounted_prices)
)

####### Q4 ########

fun4_def = (declarative
    .function("number_of_boring_games")
    .params("filename")
    .returnType(int)
)


test4_1 = test()(fun4_def
    .call('barca.txt')
    .returns(44)
)
