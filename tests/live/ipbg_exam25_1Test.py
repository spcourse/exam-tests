from checkpy import *
import typing

only("ipbg_exam25_1.py")

class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip()

    def __eq__(self, other_string):
        other_string = other_string.strip()
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string)

######## Q1 ########

fun1_def = (declarative
    .function("fop")
    .params("n")
    .returnType(list[int])
)

test1_1 = test()(fun1_def.call(35).returns([2, 3, 7, 8, 12, 13, 17, 18, 22, 23, 27, 28, 32, 33]))
test1_2 = test()(fun1_def.call(10).returns([2, 3, 7, 8]))

######## Q2 ########

fun2def = (declarative
    .function("twitterize")
    .params("text")
    .returnType(str)
)

text1 = """X is a silly name for a company.
Try to search X in google, it's 10X harder to find than Twitter."""
text1_out = """Twitter is a silly name for a company.
Try to search Twitter in google, it's 10X harder to find than Twitter."""
test2_1 = test()(fun2def.call(text1).returns(ApproxString(text1_out)))
test2_2 = test()(fun2def.call("X Xylofoon").returns(ApproxString("Twitter Xylofoon")))


######## Q3 ########

fun3_def = (declarative
    .function("dot")
    .params("l1", "l2")
    .returnType(int)
)


test3_1 = test()(fun3_def.call([1, 2, 4], [5, 2, 3]).returns(21))
test3_3 = test()(fun3_def.call([10, 20, 30, 40], [1, 1, 0, -1]).returns(-10))


######## Q4 ########

fun4def = (declarative
    .function("find_palindromes")
    .params("text")
    .returnType(list[str])
)

test4_1 = test()(fun4def
    .call("A kayak is a deified boat. A Honda Civic is not a racecar.")
    .returns(['A', 'kayak', 'a', 'deified', 'A', 'Civic', 'a', 'racecar'])
)

test4_2 = test()(fun4def
    .call("kOoRtSmEeTsYsTeEmStRoOk PaRtErReTrAp MaAnDnAaM")
    .returns(["kOoRtSmEeTsYsTeEmStRoOk", "PaRtErReTrAp", "MaAnDnAaM"])
)
######## Q5 ########


fun5def = (declarative
    .function("scrabble_options")
    .params("word_list", "letters")
    .returnType(list[str])
)

class LongList(list):
    def __repr__(self):
        return f"{repr(self[:3])[:-1]}, ...]" #f"{super().__repr__()[:4]}..."
english_words = LongList(['alike', 'apple', 'beach', 'beard', 'bicycle', 'bread', 'bride', 'brisk', 'brush', 'cage', 'candy', 'chair', 'charm', 'child', 'clock', 'close', 'cloud', 'dance', 'dove', 'dream', 'dusty', 'earth', 'field', 'fight', 'fishy', 'flame', 'flour', 'froze', 'fruit', 'glass', 'gloom', 'glove', 'goose', 'grape', 'grasp', 'grass', 'heart', 'house', 'knife', 'liver', 'loose', 'lunch', 'mango', 'match', 'money', 'movie', 'party', 'peach', 'petty', 'piano', 'plane', 'plant', 'plaza', 'poise', 'pound', 'purse', 'roast', 'robin', 'rocky', 'salad', 'shade', 'shell', 'shift', 'shine', 'shirt', 'shrub', 'skirt', 'smile', 'smoke', 'spice', 'squad', 'stone', 'stove', 'straw', 'sugar', 'sunny', 'sweat', 'sweep', 'swine', 'swoon', 'swoop', 'table', 'tiger', 'tramp', 'tree', 'trick', 'vivid', 'waste', 'water', 'whale', 'world', 'zebra'])
my_letters =  LongList(["a", "a", "b", "r", "p", "d", "e", "p", "l", "z", "s", "t"])
test5_1 = test()(fun5def.call(english_words, list('bicycle')).returns(['bicycle']))
test5_2 = test()(fun5def.call(english_words, my_letters).returns(['apple', 'beard', 'bread', 'plaza', 'salad', 'table', 'zebra']))




fun6def = (declarative
    .function("uncaesar")
    .params("text", "n")
    .returnType(str)
)

test6_1 = test()(fun6def.call("mttwfd, dtz ini ny! ltti otg. :)", 5).returns("hooray, you did it! good job. :)"))
