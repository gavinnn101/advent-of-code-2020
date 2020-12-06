# Each letter in alphabet is a different question
# Each group of passengers are separated by a blank line in the input file
# We only count unique answers. If more than 1 passenger says yes to the same question, it's still just counts as one.

import string
from collections import Counter


def create_question_list() -> dict:
    questions = {}
    for letter in string.ascii_lowercase:  # Create a dictionary of all possible questions
        questions[letter] = 0
    return questions


def count_questions(line: str, group_questions: dict) -> dict:
    for question in range(len(line)):
        if group_questions[line[question]] == 0:
            group_questions[line[question]] += 1
    return group_questions


group_questions = create_question_list()
total_answers = create_question_list()

with open('input.txt') as input_file:
    for line in input_file:
        if line == '\n':  # This is the end of the current group
            total_answers = Counter(total_answers) + Counter(group_questions)
            print(f"Current Total: {total_answers}")
            group_questions = create_question_list()  # Reset our question list for the next group
        else:
            line = line.strip()
            group_questions = count_questions(line, group_questions)
            print(group_questions)

total = 0
for _, amount in total_answers.items():
    print(amount)
    total += amount

print(f"Total: {total}")
