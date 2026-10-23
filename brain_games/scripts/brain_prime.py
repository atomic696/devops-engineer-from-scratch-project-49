import random

from brain_games.engine import run


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)

    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"

    return question, answer


def main():
    run(
        get_question_and_answer,
        'Answer "yes" if given number is prime. Otherwise answer "no".',
    )


if __name__ == "__main__":
    main()