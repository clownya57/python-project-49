from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def find_gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )

    return first_number


def generate_round():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{first_number} {second_number}"
    correct_answer = find_gcd(first_number, second_number)

    return question, str(correct_answer)
