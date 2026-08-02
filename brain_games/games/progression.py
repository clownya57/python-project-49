from random import randint

DESCRIPTION = "What number is missing in the progression?"
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10
PROGRESSION_LENGTH = 10
HIDDEN_ELEMENT = ".."


def generate_progression(start, step, length):
    return [
        start + index * step
        for index in range(length)
    ]


def generate_round():
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(
        start,
        step,
        PROGRESSION_LENGTH,
    )

    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]

    question_elements = [
        HIDDEN_ELEMENT if index == hidden_index else str(number)
        for index, number in enumerate(progression)
    ]
    question = " ".join(question_elements)

    return question, str(correct_answer)
