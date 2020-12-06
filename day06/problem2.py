# Each letter in alphabet is a different question
# Each group of passengers are separated by a blank line in the input file
# We only count an answer if everyone in the group answers yes to the same question.

import string
from collections import Counter


def create_question_list() -> dict:
    questions = {}
    for letter in string.ascii_lowercase:  # Create a dictionary of all possible questions
        questions[letter] = 0
    return questions


def count_questions(line: str, group_questions: dict) -> dict:
    added = []
    for question in range(len(line)):
        if line[question] not in added:
            group_questions[line[question]] += 1
            added.append(line[question])
    return group_questions


group_questions = create_question_list()
total_answers = create_question_list()
people = 0  # Number of people in group

with open('input.txt') as input_file:
    for line in input_file:
        if line == '\n':  # This is the end of the current group
            for answer, value in group_questions.items():
                if value != people:
                    group_questions[answer] = 0
                else:
                    group_questions[answer] = 1
            total_answers = Counter(total_answers) + Counter(group_questions)
            print(f"Current Total: {total_answers}")
            group_questions = create_question_list()  # Reset our question list for the next group
            people = 0
        else:
            line = line.strip()
            people += 1
            group_questions = count_questions(line, group_questions)
            print(group_questions)

total = 0
for _, amount in total_answers.items():
    total += amount

print(f"Total: {total}")
