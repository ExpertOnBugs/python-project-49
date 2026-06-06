import random

from brain_games.functions import greeting, is_even, result


def even_game():
    name = greeting('What is the result of the expression?')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    points = 0

    ATTEMPTS = 3

    while points < ATTEMPTS:
        random_number = random.randint(1, 100)

        print('Question:', random_number)

        correct_answer = 'yes' if is_even(random_number) else 'no'

        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            points += 1
        else:
            break
        
    result(points, correct_answer, answer, name)