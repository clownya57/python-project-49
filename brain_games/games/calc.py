from random import choice, randint

DESCRIPTION = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ("+", "-", "*")


def calculate(first_number, second_number, operation):
    match operation:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case _:
            raise ValueError(f"Unsupported operation: {operation}")


def generate_round():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(OPERATIONS)

    question = f"{first_number} {operation} {second_number}"
    correct_answer = calculate(
        first_number,
        second_number,
        operation,
    )

    return question, str(correct_answer)
