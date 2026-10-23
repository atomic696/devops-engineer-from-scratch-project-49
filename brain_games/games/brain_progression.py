import random

from brain_games.engine import run

DESCRIPTION = "What number is missing in the progression?"
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_question_and_answer():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    hidden_index = random.randint(0, length - 1)

    progression = []

    for index in range(length):
        number = start + index * step
        progression.append(number)

    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, answer


def main():
    run(
        get_question_and_answer,
        DESCRIPTION,
    )


if __name__ == "__main__":
    main()
