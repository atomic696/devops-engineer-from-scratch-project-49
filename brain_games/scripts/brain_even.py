import random

from brain_games.engine import run


def get_question_and_answer():
    number = random.randint(1, 100)
    answer = "yes" if number % 2 == 0 else "no"

    return str(number), answer


def main():
    run(
        get_question_and_answer,
        'Answer "yes" if the number is even, otherwise answer "no".',
    )


if __name__ == "__main__":
    main()