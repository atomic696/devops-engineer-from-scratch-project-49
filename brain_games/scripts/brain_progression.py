import random

from brain_games.engine import run


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
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
        "What number is missing in the progression?",
    )


if __name__ == "__main__":
    main()