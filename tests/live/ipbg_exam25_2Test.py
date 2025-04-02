from checkpy import *
import typing

only("ipbg_exam25_2.py")



######## Q1 ########

fun1_def = (declarative
    .function("dud")
    .params("n")
    .returnType(list[int])
)

test1_1 = test()(fun1_def.call(200).returns([3, 18, 33, 48, 63, 78, 93, 108, 123, 138, 153, 168, 183, 198]))

######## Q2 ########

fun2_def = (declarative
    .function("reverse_words")
    .params("sentence")
    .returnType(str)
)

test2_1 = test()(fun2_def.call("Every adventure requires a first step.").returns("Step first a requires adventure every."))

######## Q3 ########

fun3_def = (declarative
    .function("select_adults")
    .params("people", "ages")
    .returnType(list[str])
)

people = ["Jan", "Piet", "Anne", "Marieke", "Robin", "Jeroen",
    "Femke", "Kim", "Bas", "Noor", "Lieke", "Sam"]
ages = [12, 52, 15, 29, 18, 41, 26, 4, 47, 16, 24, 13]
adults = ['Piet', 'Marieke', 'Robin', 'Jeroen', 'Femke', 'Bas', 'Lieke']

test3_1 = test()(fun3_def.call(people, ages).returns(adults))

######## Q4 ########

fun4_def = (declarative
    .function("sPoNgEbOb")
    .params("text")
    .returnType(str)
)

spongebob_input = "Hello everyone! I'm new to the internet! Let's have a respectful discussion about interesting and complicated topics; like politics, and philosophy!"
spongebob_output = "Hello eVeRyOnE! I'm new to the iNtErNeT! Let's have a rEsPeCtFuL dIsCuSsIoN about iNtErEsTiNg and cOmPlIcAtEd topics; like pOlItIcS, and pHiLoSoPhY!"

test4_1 = test()(fun4_def.call(spongebob_input).returns(spongebob_output))

######## Q5 ########

## NOTE: THIS CHECK DOES NOT YET WORK AS INTENDED

class ApproxString:
    def __init__(self, base_string):
        self._base_string = "\n".join([line.rstrip() for line in base_string.split("\n") if line.rstrip()])


    def __eq__(self, other_string):
        # check if number of lines match expected number
        expected_nr_lines = len(self._base_string.split("\n"))
        actual_nr_lines = len(self._base_string.split("\n"))
        assert expected_nr_lines == actual_nr_lines, f"Expected {expected_nr_lines} lines, your code returned {actual_nr_lines} lines"

        # check line by line if output string is correct
        for i, (expected_line, actual_line) in enumerate(zip(self._base_string.split("\n"), other_string.split("\n"))):
            assert expected_line.rstrip(" ") == actual_line.rstrip(" "), f"Your code output something incorrect on line {i}"

        return True

    def __repr__(self):
        return repr(self._base_string)

fun5_def = (declarative
    .function("top_to_bottom")
    .params("text")
    .returnType(str)
)

top_to_bottom_input = "Neo. \n You have to wake up. \n None of this is real. \n Wake up, Neo."
top_to_bottom_output = ApproxString("""N Y N W
e o o a
o u n k
.   e e
  h
  a o u
  v f p
  e   ,
    t
  t h N
  o i e
    s o
  w   .
  a i
  k s
  e
    r
  u e
  p a
  . l
    .
    """)

test5_1 = test()(fun5_def.call(top_to_bottom_input).returns(top_to_bottom_output))

######## Q6 ########

square1 = [
    "abcde",
    "fghik",
    "lmnop",
    "qrstu",
    "vwxyz"
    ]

square2 = [
    "agntz",
    "fmsye",
    "lrxdk",
    "qwcip",
    "vbhou"
    ]

fun6_def = (declarative
    .function("decode_polybius")
    .params("square", "text")
    .returnType(str)
)

polybius_input1 = "144254 21445125 21545532 21445125 21545532 21545532 21545532 1453322525! :)"
polybius_input2 = "543445'5115 124234251533 442315 431513421544 13341415! 52153131 14343315. :)"

test6_1 = test()(fun6_def.call(square2, polybius_input1).returns("two five four five four four four three! :)"))
test6_2 = test()(fun6_def.call(square1, polybius_input2).returns("you've broken the secret code! well done. :)"))
