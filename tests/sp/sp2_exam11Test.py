from checkpy import *
import typing

only("sp2_exam11.py")
download("films.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/films.csv")


######## Q1 ########

fun1_def = (declarative
    .function("after_is")
    .params("text")
    .returnType(dict)
)

text = """It was a place where up is down, and down is up; where nothing is
quite what it seems. Why is a raven like a writing desk?
"""

test1_1 = test()(fun1_def.call(text).returns({'a': 2, 'down': 1, 'up': 1}))


######## Q2 ########

fun2a_def = (declarative
    .function("unify")
    .params("dict1", "dict2")
    .returnType(dict)
)

dict1 = {"a": [1, 2, 3], "c": [4, 5, 6], "d": [6]}
dict2 = {"a": [1, 3, 4], "b": [9], "c": [2, 4]}

test2_1 = test()(fun2a_def.call(dict1, dict2).returns({'b': [9], 'c': [2, 4, 5, 6], 'd': [6], 'a': [1, 2, 3, 4]}))


fun2b_def = (declarative
    .function("melt")
    .params("dict")
    .returnType(list)
)

test2_2 = test()(fun2b_def.call(dict1).returns([('a', 1), ('a', 2), ('a', 3), ('c', 4), ('c', 5), ('c', 6), ('d', 6)]))


######## Q3 ########

fun3_def = (declarative
    .function("most_frequent_actress")
    .params("filename")
    .returnType(tuple[str, list])
)

actress = "Bergman, Ingrid"
films = ['Count of Old Town, The', 'Autumn Sonata', 'Gaslight', 'Indiscreet', 'Walpurgis Night', 'Joan of Arc',
'A Woman Called Golda', 'A Walk in the Spring Rain', 'Under Capricorn', 'Notorious', 'June Night', 'Goodbye Again',
'Anastasia', "Bells of St. Mary's, The", 'Intermezzo', "A Woman's Face", 'Swedenhielms', 'Only One Night', 'Dollar',
'Elena & Her Men', 'Europa Fifty-One', 'Voyage in Italy', 'Fear', 'Stromboli', 'Cactus Flower']

test3_1 = test()(fun3_def.call("films.csv").returns((actress, films)))
