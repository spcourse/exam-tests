from checkpy import *
import typing
import pandas as pd

only("sp2_exam.py")
download("films.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/films.csv")


class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip().replace("\n", " ")

    def __eq__(self, other_string):
        other_string = other_string.strip().replace("\n", " ")
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string) + "[approximately]"


class ApproxDataFrame:
    def __init__(self, base_lst):
        self._base_lst = base_lst

    def __eq__(self, other_df):
        return self._base_lst == list(other_df["Title"])

    def __repr__(self):
        return repr(self._base_lst)

######## Q1 ########

fun1_def = (declarative
    .function("passed_students")
    .params("student_grades")
    .returnType(list)
)


grades_dict = {
"Paul": [7.0, 5.1, 6.3],
"Livia": [7.8, 8.9, 6.4],
"Linos": [8.3, 4.3, 9.8],
"Corinna": [5.5, 5.3, 5.1],
"Yasmina": [7.0, 9.1, 8.3],
"Leonard": [3.0, 2.1, 3.3],
"Eula": [7.6, 7.7, 3.3],
"Shukra": [5.0, 5.0, 8.0],
"Emil": [7.0, 5.1, 6.3],
}

passed_lst =  ['Paul', 'Livia', 'Linos', 'Yasmina', 'Eula', 'Shukra', 'Emil']


test1_3 = test()(fun1_def
    .call(grades_dict)
    .returns(passed_lst)
)

####### Q2 ########

fun2_def = (declarative
    .function("count_letters")
    .params("word")
    .returnType(dict)
)

input_word = "elementary"

test2_1 = test()(fun2_def
    .call(input_word)
    .returns({'e': 3, 'l': 1, 'm': 1, 'n': 1, 't': 1, 'a': 1, 'r': 1, 'y': 1})
)

fun3_def = (declarative
    .function("is_anagram")
    .params("word1", "word2")
    .returnType(bool)
)

test2_2 = test()(fun3_def
    .call('listen', 'silent')
    .returns(True)
)

test2_3 = test()(fun3_def
    .call('angular', 'granular')
    .returns(False)
)

####### Q3 ########

fun4_def = (declarative
    .function("second_best_film_per_year")
    .params("filename")
    .returnType(pd.DataFrame)
)

expected_titles = ["Kriemhild's Revenge, The Nibelungenlied", 'Joyless Street', 'Flesh & the Devil, The', 'My Best Girl', 'Mysterious Lady, The', 'Wild Orchids', 'Anna Christie', 'Mata Hari', 'Number Seventeen', 'Baby Face', 'Judge Priest', 'Adventures of Rex & Rinty, The', 'Camille', 'Intermezzo', "A Woman's Face", 'Jamaica Inn', 'Law & Order', 'Man from Montana', 'Reap the Wild Wind', 'Ape Man, The', 'Gaslight', 'Flame of Barbary Coast', 'Gilda', 'Hawk of Powder River', 'Three Godfathers', 'She Wore a Yellow Ribbon', 'Stage Fright', 'Strangers on a Train', 'Come Back, Little Sheba', 'Mogambo', 'Inauguration of the Pleasure Dome', 'Rebel Without a Cause', 'Seventh Seal, The', 'Gunfight at the OK Corral', 'Matchmaker, The', 'Carlton-Browne of the F.O.', 'Spartacus', 'Four Horsemen of the Apocalypse, The', 'Lolita', 'Cleopatra', 'Goldfinger', 'Dear Brigitte', 'Russians Are Coming, the Russians Are, The', 'Bobo, The', 'War & Peace', 'True Grit', 'Getting Straight', 'Statue, The', 'Say Goodbye Maggie Cole', 'Dillinger', 'Monty Python & the Holy Grail', 'That Lucky Touch', 'Rocky', 'Slap Shot', 'Magic', 'Alien', 'Rodeo Girl', 'For Your Eyes Only', 'King of Comedy', 'Man with Two Brains, The', 'Romancing the Stone', 'Out of the Darkness', 'Best of Times, The', 'Matewan', 'Phantom of the Ritz', "New Year's Day", 'Guilty by Suspicion', 'Raw Nerve', 'Party Girl', 'Honeymoon in Vegas', 'Island of Dr. Moreau, The', 'Alien: resurrection']


test3_1 = test()(fun4_def
    .call('films.csv')
    .returns(ApproxDataFrame(expected_titles))
)
