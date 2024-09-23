from checkpy import *
import typing

# only("sp1_exam10.py")
download("spotify.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/spotify.csv")


######## Q1 ########

fun1_def = (declarative
    .function("repeated_words")
    .params("text")
    .returnType(typing.List[str])
)

text1 = "'GOD' is an acronym which stands for 'GOD Over Djinn'."
text2 = """There was nothing so very remarkable in that; nor did Alice think it
 so very much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear!
 I shall be late!'"""

test1_1 = test()(fun1_def.call(text1).returns(["god"]))
test1_2 = test()(fun1_def.call(text2).returns(['so', 'very', 'the', 'to', 'oh', 'dear']))


######## Q2 ########

fun2_def = (declarative
    .function("sentiment_of_text")
    .params("text", "sentiment_of_word")
    .returnType(int)
)

sentiment_of_word = {
    "abysmal": -5, "dreadful": -5, "miserable": -4, "terrible": -5, "upset": -3,

    "amazing": 5, "fantastic": 4, "great": 3, "superb": 4, "fantabulous": 5
}

text1 = "Wow, what an amazing day it has been! The weather is fantastic!"

text2 = "Today has been abysmal. The weather is dreadful, and I feel miserably upset."

test2_1 = test()(fun2_def.call(text1, sentiment_of_word).returns(9))
test2_2 = test()(fun2_def.call(text2, sentiment_of_word).returns(-13))


######## Q3 ########

fun3_def = (declarative
    .function("find_artist_of_most_popular_song_based_on_number_of_streams")
    .params("filename")
    .returnType(str)
)

test3_1 = test()(fun3_def.call("spotify.csv").returns("The Weeknd"))

fun4_def = (declarative
    .function("find_most_popular_release_month_based_on_number_of_songs")
    .params("filename")
    .returnType(str)
)

test4_1 = test()(fun4_def.call("spotify.csv").returns("2022-5"))
