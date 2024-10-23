from checkpy import *
import typing

only("sp2_exam1.py")
download("meteo_data.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/meteo_data.csv")


######## Q1 ########

fun1_def = (declarative
    .function("group_titles_by_genre")
    .params("library")
    .returnType(dict)
)

test1_1 = test()(fun1_def
    .call(
        {"Life of Pi": "Adventure",
         "One World The Water Dancer": "Fantasy",
         "The Three Musketeers": "Adventure",
         "To Kill a Mockingbird": "Classics",
         "Circe": "Fantasy",
         "The Call of the Wild": "Adventure",
         "Little Women": "Classics"}
    )
    .returns(
        {'Adventure': ['Life of Pi', 'The Three Musketeers',
            'The Call of the Wild'],
        'Fantasy': ['One World The Water Dancer', 'Circe'],
        'Classics': ['To Kill a Mockingbird', 'Little Women']})
)

######## Q2 ########

fun2_def = (declarative
    .function("count_characters_in_words")
    .params("words")
    .returnType(dict)
)


test2_1 = test()(fun2_def
    .call(["Apple", "Banana", "Grape"])
    .returns({'a': 5, 'p': 3, 'l': 1, 'e': 2,
        'b': 1, 'n': 2, 'g': 1, 'r': 1})
)

######## Q3 ########

fun3_def = (declarative
    .function("top5_highest_weather_index")
    .params("filename")
)

test3_1 = test()(fun3_def
    .call("meteo_data.csv")
    .returns(['Lisbon', 'Athens', 'Madrid', 'Amsterdam', 'Paris'])
)
