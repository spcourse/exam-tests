from checkpy import *
import typing

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

fun2_def = (declarative
    .function("combine_dicts")
    .params("dict1", "dict2")
    .returnType(dict)
)

english_to_french = {'banana': 'banane', 'apple': 'pomme', 'almond': 'amande', 'cat': 'chat', 'fine': 'amande'}
french_to_spanish = {'pomme': 'manzana', 'car': 'coche', 'banane': 'plátano', 'amande': 'almendra'}
english_to_spanish = {'banana': 'plátano', 'apple': 'manzana', 'almond': 'almendra', 'fine': 'almendra'}

test2_1 = test()(fun2_def.call(english_to_french, french_to_spanish).returns(english_to_spanish))

######## Q3 ########

fun3_def = (declarative
    .function("most_frequent_actress")
    .params("filename")
    .returnType(tuple[str, list])
)

actress = "Bergman, Ingrid"
films = ['Count of Old Town, The', 'Autumn Sonata', 'Gaslight', 'Indiscreet', 'Walpurgis Night', 'Joan of Arc', 'A Woman Called Golda', 'A Walk in the Spring Rain', 'Under Capricorn', 'Notorious', 'June Night', 'Goodbye Again', 'Anastasia', "Bells of St. Mary's, The", 'Intermezzo', "A Woman's Face", 'Swedenhielms', 'Only One Night']

test3_1 = test()(fun3_def.call("films.csv").returns((actress, films)))
