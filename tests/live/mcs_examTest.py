from checkpy import *

only('mcs_exam.py')

######## Q1 ########

fun1 = test()(declarative
    .function("mean")
    .params("numbers")
    .returnType(float)
    .call([2, 2, 2, 4, 5])
    .returns(3.0)
)

######## Q2 ########

fun2 = test()(declarative
    .function("countif")
    .params("numbers", "number")
    .returnType(int)
    .call([1, 2, 6, 1, 2, 6, 6, 4], 6)
    .returns(3)
)

######## Q3 ########

fun3 = test()(declarative
    .function("longest_ones_sequence")
    .params("binary_list")
    .returnType(int)
    .call([1, 1, 0, 1, 1, 1, 0, 1])
    .returns(3)
)

######## Q4 ########

fun4 = test()(declarative
    .function("group_titles_by_genre")
    .params("library")
    .returnType(dict)
    .call({
        "Life of Pi": "Adventure",
        "One World The Water Dancer": "Fantasy",
        "The Three Musketeers": "Adventure",
        "To Kill a Mockingbird": "Classics",
        "Circe": "Fantasy",
        "The Call of the Wild": "Adventure",
        "Little Women": "Classics"
    })
    .returns({
        'Adventure': ['Life of Pi', 'The Three Musketeers', 'The Call of the Wild'],
        'Fantasy': ['One World The Water Dancer', 'Circe'],
        'Classics': ['To Kill a Mockingbird', 'Little Women']
    })
)
######## Q5 ########

fun5 = test()(declarative
    .function("find_pairs")
    .params("numbers", "target")
    .returnType(list[tuple,...])
    .call([1, 2, 3, 4, 5, 6], 7)
    .returns([(1, 6), (2, 5), (3, 4)])
)
######## Q6 ########

fun6_def = (declarative
    .function("multi_split")
    .params("text", "delimiters")
    .returnType(list[str, ...])
)

@test()
def test6():
    state = fun6_def.call(
        "The workshop covered several topics: It focused on painting and sculpting. \
Everyone learned something.",
        [":", "."])()
    cleaned = [_txt.strip() for _txt in state.returned]
    assert cleaned == ['The workshop covered several topics', 'It focused on painting and sculpting',
       'Everyone learned something', '']
