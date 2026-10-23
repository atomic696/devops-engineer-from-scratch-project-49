import math
import random

from brain_games.engine import run


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    answer = math.gcd(number1, number2)
    question = f"{number1} {number2}"

    return question, str(answer)


def main():
    run(
        get_question_and_answer,
        "Find the greatest common divisor of given numbers.",
    )


if __name__ == "__main__":
    main()