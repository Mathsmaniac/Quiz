"""
quiz_workingsv1.py
Fourth component of quiz project
In this component, I make a function that asks a question from a file of words
The question will conform to a set theme; colours, dates or numbers
I also make another function that then checks the answer that was entered
"""

import random
from maori_words import maori_words_dict as words_dict


def ask_question():
    # Convert dictionary keys of the type to a list
    keys_list = list(words_dict[quiz_type].keys())
    global chosen
    chosen = random.choice(keys_list)
    return (f"What is the Māori translation for {chosen}? ")


def check_answer(answer, expected):
    correct = words_dict[quiz_type][expected]
    if answer.lower() == correct.lower():
        return ["Correct", "Well done"]
    else:
        return ["Incorrect", f"The correct answer is {correct}"]


if __name__ == "__main__":
    # Enter quiz type for testing
    quiz_type = input("Quiz type (colours, days_months, numbers): ")
    print(check_answer(input((ask_question())), chosen))
