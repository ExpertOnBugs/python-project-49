import random

from brain_games.functions import greeting, prime, result


def prime_game():
    name = greeting('Answer "yes" if given number is prime.'
    ' Otherwise answer "no".')

    points = 0

    ATTEMPTS = 3

    while points < ATTEMPTS:
        number = random.randint(1, 151)
        
        correct_answer = prime(number)

        print(f"Question: {number}")

        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            points += 1
        else:
            break

    result(points, correct_answer, answer, name)