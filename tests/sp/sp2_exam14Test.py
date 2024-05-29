from checkpy import *
import typing

only("sp2_exam14.py")
download("spotify.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/spotify.csv")


######## Q1 ########

fun1_def = (declarative
    .function("add_keys_values")
    .params("dict", "keys", "values")
    .returnType(dict)
)

test1_1 = test()(fun1_def
    .call(
        {'apple': 5, 'banana': 3, 'orange': 8},
        ['grapefruit', 'ananas'],
        [5, 4]
    )
    .returns({'apple': 5, 'banana': 3, 'orange': 8, 'grapefruit': 5, 'ananas': 4})
)

test1_2 = test()(fun1_def
    .call(
        {'swimming': 3.8, 'cycling': 180.2, 'running': 42.195},
        ['running', 'skiiing'],
        [42.195]
    )
    .returns({'swimming': 3.8, 'cycling': 180.2, 'running': 42.195})
)

######## Q2 ########

fun2_def = (declarative
    .function("bad_translator")
    .params("text", "translation")
    .returnType(str)
)


english_french_dict = {
    "i": "je",
    "ran": "courait",
    "into": "dans",
    "a": "un",
    "the": "le",
    "vague": "vague",
    "wave": "vague"
}

@test()
def test2_1():
    state = fun2_def.call("The vague wave", english_french_dict)()
    output = state.returned.strip(" ./,';!?'")
    assert output == "Le vague vague"

@test()
def test2_2():
    state = fun2_def.call("I ran into a problem", english_french_dict)()
    output = state.returned.strip(" ./,';!'")
    assert output == "Je courait dans un ???"

######## Q3 ########

fun3_def = (declarative
    .function("find_most_popular_song_based_on_number_of_streams")
    .params("filename")
)

test3_1 = test()(fun3_def.call("spotify.csv").returns(["Blinding Lights", "The Weeknd", 3703895074]))
