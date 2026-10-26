import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    return [str(start + i * step) for i in range(length)]


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = 10
    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer