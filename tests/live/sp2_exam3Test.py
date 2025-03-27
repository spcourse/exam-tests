from checkpy import *
import typing
import pandas as pd

only("sp2_exam3.py")
download("election_amsterdam_2022.csv", "https://raw.githubusercontent.com/spcourse/exam-tests/main/data/election_amsterdam_2022.csv")


class ApproxString:
    def __init__(self, base_string):
        self._base_string = base_string.strip().replace("\n", " ")

    def __eq__(self, other_string):
        other_string = other_string.strip().replace("\n", " ")
        return self._base_string == other_string

    def __repr__(self):
        return repr(self._base_string) + "[approximately]"


class ApproxSeries:
    def __init__(self, base_series):
        self._base_series = base_series

    def __eq__(self, other_series):
        return self._base_series.to_dict() == other_series.to_dict()

    def __repr__(self):
        return repr(self._base_series)

######## Q1 ########

fun1_def = (declarative
    .function("hack_grades")
    .params("original_grades")
    .returnType(dict)
)


student_grades = {
    "Pierina": {"grade":5.2, "corrector_name": "Mr. Dawson"},
    "Ottarr": {"grade":9.4, "corrector_name": "Ms. Jacksley"},
    "Donnchadh": {"grade":8.3, "corrector_name": "Ms. Jacksley"},
    "Juozas": {"grade":4.8, "corrector_name": "Mr. Dawson"},
    "Zdenko": {"grade":1.2, "corrector_name": "Mr. Dawson"},
    "Ilona": {"grade":7.4, "corrector_name": "Ms. Jacksley"},
    "Vilma": {"grade":6.0, "corrector_name": "Mr. Dawson"},
    "Blagoj": {"grade":6.6, "corrector_name": "Ms. Jacksley"},
    "Sirpa": {"grade":6.3, "corrector_name": "Ms. Jacksley"},
    "Midori": {"grade":8.8, "corrector_name": "Ms. Jacksley"},
    "Tamara": {"grade":9.9, "corrector_name": "Ms. Jacksley"},
    "Amit": {"grade":7.2, "corrector_name": "Ms. Jacksley"},
    "Oskar": {"grade":4.4, "corrector_name": "Mr. Dawson"}
}

hacked_grades =  {
    'Pierina': {'grade': 7.0, 'corrector_name': 'Elite Hacker'},
    'Ottarr': {'grade':9.4, 'corrector_name': 'Ms. Jacksley'},
    'Donnchadh': {'grade': 8.3, 'corrector_name': 'Ms. Jacksley'},
    'Juozas': {'grade': 7.0, 'corrector_name': 'Elite Hacker'},
    'Zdenko': {'grade': 7.0, 'corrector_name': 'Elite Hacker'},
    'Ilona': {'grade': 7.4, 'corrector_name': 'Ms. Jacksley'},
    'Vilma': {'grade': 6.0, 'corrector_name':'Mr. Dawson'},
    'Blagoj': {'grade': 6.6, 'corrector_name': 'Ms. Jacksley'},
    'Sirpa': {'grade': 6.3, 'corrector_name': 'Ms. Jacksley'},
    'Midori': {'grade': 8.8, 'corrector_name': 'Ms. Jacksley'},
    'Tamara': {'grade': 9.9, 'corrector_name': 'Ms. Jacksley'},
    'Amit': {'grade': 7.2, 'corrector_name': 'Ms. Jacksley'},
    'Oskar':{'grade': 7.0, 'corrector_name': 'Elite Hacker'}
}

test1_3 = test()(fun1_def
    .call(student_grades)
    .returns(hacked_grades)
)

####### Q2 ########

fun2_def = (declarative
    .function("crop_2pangram")
    .params("text")
    .returnType(str)
)

input_text = """Oh, solemn Sphinx of black Quartz! Heed my words, judge my vow.
I implore you! Pack my box with five dozen liquor jugs! And make it quick!"""

test2_1 = test()(fun2_def
    .call(input_text)
    .returns(ApproxString("Oh, solemn Sphinx of black Quartz! Heed my words, judge my vow. I implore you! Pack my box with five dozen liquor jugs!"))
)

fun3_def = (declarative
    .function("top3_candidates_per_party_only")
    .params("filename")
    .returnType(pd.Series)
)

expected = pd.Series({'4 Partij van de Arbeid (P.v.d.A.)': 47045, '2 D66': 30704, '1 GROENLINKS': 28910, '3 VVD': 27541, '6 Partij voor de Dieren': 16661, '13 JA21': 12808, '5 SP (Socialistische Partij)': 11332, '25 Volt': 10908, '12 Amsterdam BIJ1': 10000, '7 DENK': 7201, '9 CDA': 6615, '10 Partij van de Ouderen (P.v.d.O.)': 4643, '8 Forum voor Democratie': 3500, '15 De Groenen Basis Piraten': 2966, '11 ChristenUnie': 2511, '14 Hart voor Vrijheid Amsterdam': 1508, '26 LEF - Voor de Nieuwe Generatie': 375, '16 GO': 179})

test3_1 = test()(fun3_def
    .call('election_amsterdam_2022.csv')
    # .returns("x")
    .returns(ApproxSeries(expected))
)
