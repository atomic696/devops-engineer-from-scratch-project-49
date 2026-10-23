import prompt

from brain_games.cli import welcome_user


def run(generate_round, instruction):
    name = welcome_user()
    print(instruction)

    for _ in range(3):
        question, correct_answer = generate_round()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")