from checkpy import *
import typing

only("sp101_exam1.py")


class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip().replace("\n", " ")

    def __eq__(self, other_string):
        other_string = other_string.strip().replace("\n", " ")
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string) + "[approximately]"


######## Q1 ########


fun1_def = (declarative
    .function("differences")
    .params("numbers")
    .returnType(list)
)

test1_1 = test()(fun1_def
    .call([3,5,6,3,4,1,9,7,6,5])
    .returns([2, 1, -3, 1, -3, 8, -2, -1, -1])
)

######## Q2 ########

fun2_def = (declarative
    .function("taalk_sloow")
    .params("text")
    .returnType(str)
)
sentence = "Could you repeat that again, but more slowly this time?"

test2_1 = test()(fun2_def
    .call(sentence)
    .returns(ApproxString("Coouuld yoouu reepeeaat thaat aagaaiin, buut mooree sloowly thiis tiimee?"))
)

######## Q3 ########


fun3_def = (declarative
    .function("same_as_last_year")
    .params("prev_holiday_destination", "new_holiday_destination")
    .returnType(list)
)

holiday_destination_2024 = {
    "Kristina":"US",
    "Gulbrandr":"Netherlands",
    "Fatimah":"France",
    "Morteza":"South Pole",
    "Hippolytos":"Netherlands",
    "Roxana":"France",
    "Parvez":"Germany",
    "Tammie":"Netherlands",
    "Baldr":"South Korea",
    "Rizvan":"Netherlands"
}

holiday_destination_2025 = {
    "Kristina":"Netherlands",
    "Gulbrandr":"Netherlands",
    "Fatimah":"Spain",
    "Morteza":"South Pole",
    "Hippolytos":"Spain",
    "Roxana":"Norway",
    "Parvez":"Germany",
    "Tammie":"France",
    "Baldr":"North Korea",
    "Rizvan":"South Korea"
}

test3_1 = test()(fun3_def
    .call(holiday_destination_2024, holiday_destination_2025)
    .returns(['Gulbrandr', 'Morteza', 'Parvez'])
)
