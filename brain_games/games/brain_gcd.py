import math
import random

from brain_games.engine import run

DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    answer = math.gcd(number1, number2)
    question = f"{number1} {number2}"

    return question, str(answer)


def main():
    run(
        get_question_and_answer,
        DESCRIPTION,
    )


if __name__ == "__main__":
    main()
