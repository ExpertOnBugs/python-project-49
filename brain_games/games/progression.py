import random

from brain_games.functions import greeting, progression, result


def progression_game():
    name = greeting('What number is missing in the progression?')

    points = 0

    ATTEMPTS = 3

    while points < ATTEMPTS:
        progressions = progression()

        hidden = random.randint(0, 9)

        correct_answer = progressions[hidden]
        progressions[hidden] = '..'

        print('Question:', *progressions)

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')
            points += 1
        else:
            break

    result(points, correct_answer, answer, name)