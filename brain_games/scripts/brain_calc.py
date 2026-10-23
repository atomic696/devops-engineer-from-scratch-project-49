import random

from brain_games.engine import run


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(["+", "-", "*"])

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
        "What is the result of the expression?",
    )


if __name__ == "__main__":
    main()