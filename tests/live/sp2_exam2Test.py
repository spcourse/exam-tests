from checkpy import *
import typing

only("sp2_exam2.py")
download("election_amsterdam_2022.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/election_amsterdam_2022.csv")


######## Q1 ########

fun1_def = (declarative
    .function("total_score")
    .params("words", "letter_values")
    .returnType(int)
)

letter_values = {
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

test1_1 = test()(fun1_def
    .call(["word"], letter_values)
    .returns(13)
)
test1_2 = test()(fun1_def
    .call(["word", "wo-rd"], letter_values)
    .returns(26)
)
test1_3 = test()(fun1_def
    .call(["quartzy", "muzjiks", "quizzify"], letter_values)
    .returns(113)
)

######## Q2 ########

fun2_def = (declarative
    .function("autocomplete")
    .params("current_letter", "length", "most_likely_next_character_dict")
    .returnType(str)
)


next_character_english = {
    'a': 'n', 'b': 'e', 'c': 'o', 'd': 'e', 'e': ' ', 'f': 'o',
    'g': 'h', 'h': 'e', 'i': 'n', 'j': 'u', 'k': 'e', 'l': 'l',
    'm': 'e', 'n': 'd', 'o': 'n', 'p': 'r', 'q': 'u', 'r': 'e',
    's': 't', 't': 'h', 'u': 'r', 'v': 'e', 'w': 'i', 'x': 't',
    'y': 'o', 'z': 'e', ' ': 't'
}

test2_1 = test()(fun2_def
    .call("a", 2, next_character_english)
    .returns("nd")
)
test2_2 = test()(fun2_def
    .call("p", 2, next_character_english)
    .returns("re")
)
test2_3 = test()(fun2_def
    .call("i", 3, next_character_english)
    .returns("nde")
)
test2_4 = test()(fun2_def
    .call(" ", 4, next_character_english)
    .returns("the ")
)

######## Q3 ########

fun3_def = (declarative
    .function("total_votes_per_party")
    .params("filename")
)

@test()
def test3_1():
    state = fun3_def.call("election_amsterdam_2022.csv")()
    output = state.returned
    assert set(output.to_list()) == {39354, 52595, 40829, 30510}


fun4_def = (declarative
    .function("preferred_candidates")
    .params("filename")
)

@test()
def test4_1():
    state = fun4_def.call("election_amsterdam_2022.csv")()
    output = state.returned
    assert set(output['candidate_name'].to_list()) == {'Kabamba, C.K.E.', 'Koyuncu, S.', 'Nadif, I.'}
