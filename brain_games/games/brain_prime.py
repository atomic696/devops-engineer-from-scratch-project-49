import random

from brain_games.engine import run

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)

    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return question, answer


def main():
    run(
        get_question_and_answer,
        DESCRIPTION,
    )


if __name__ == "__main__":
    main()
