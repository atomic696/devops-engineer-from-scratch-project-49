import random

from brain_games.engine import run

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if number % 2 == 0 else "no"

    return str(number), answer


def main():
    run(
        get_question_and_answer,
        DESCRIPTION,
    )


if __name__ == "__main__":
    main()
