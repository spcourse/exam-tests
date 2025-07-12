# Author: Puck te Rietmole
# Date: 28/04/2025
# SP101 Exam 4 solutions code


# exc1
def remove_words_with_letter(text, forbidden_letter):
    forbidden_letter = forbidden_letter.lower()
    words = text.split(" ")
    new_text = ""
    for word in words:
        clean_word = word.lower()
        if forbidden_letter not in clean_word:
            new_text += word + " "
    return new_text

sentence = "I am not very good at these funny little word games."
censored_text_e = remove_words_with_letter(sentence, "e")
print(censored_text_e)
censored_text_a = remove_words_with_letter(sentence, "a")
print(censored_text_a)

other_sentence = "Edward was a tough customer."

# exc2
def longest_repetition(numbers):
    last = None
    rep = 0
    longest = 0
    for i in numbers:
        if i == last:
            rep += 1
        else:
            rep = 1
        if rep > longest:
            longest = rep
        last = i
    return longest



numbers1 = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
print(longest_repetition(numbers1))
numbers2 = [1, 1, 3, 3, 3, 3, 4, 4, 4]
print(longest_repetition(numbers2))


# exc3
peoples_hatcolor = {
    "Janeth":"black",
    "Berto":"green",
    "Gulnaz":"purple",
    "Frey":"pink",
    "Suman":"green",
    "Rabi":"red",
    "Jayesh":"green",
    "Callan":"pink",
    "Dzenan":"yellow",
    "Leonardo":"pink"
}

def hatcolor_frequency(peoples_hatcolor):
    color_frequency = {}
    for color in peoples_hatcolor.values():
        if color not in color_frequency:
            color_frequency[color] = 0
        color_frequency[color] += 1
    return color_frequency

frequency_of_colors = hatcolor_frequency(peoples_hatcolor)
print(frequency_of_colors)
