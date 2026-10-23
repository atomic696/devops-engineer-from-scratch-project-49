import random

from brain_games.engine import run

DESCRIPTION = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = ["+", "-", "*"]


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)

    match operation:
        case "+":
            answer = number1 + number2
        case "-":
            answer = number1 - number2
        case "*":
            answer = number1 * number2

    question = f"{number1} {operation} {number2}"

    return question, str(answer)


def main():
    run(
        get_question_and_answer,
        DESCRIPTION,
    )


if __name__ == "__main__":
    main()
