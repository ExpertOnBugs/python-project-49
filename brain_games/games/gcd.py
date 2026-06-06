import random

from brain_games.functions import gcd, greeting, result


def gcd_game():
    name = greeting('Find the greatest common divisor of given numbers.')

    points = 0

    ATTEMPTS = 3

    while points < ATTEMPTS:

        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)

        correct_answer = gcd(first_number, second_number)

        print(f'Question: {first_number} {second_number}')

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')
            points += 1
        else:
            break
    
    result(points, correct_answer, answer, name)