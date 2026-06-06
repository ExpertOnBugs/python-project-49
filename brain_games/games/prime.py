import random

from brain_games.functions import greeting, prime, result


def prime_game():
    name = greeting('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_num = 0

    while correct_num < 3:
        number = random.randint(1, 151)
        
        correct_answer = prime(number)

        print(f"Question: {number}")

        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_num += 1
        else:
            break

    result(correct_num, correct_answer, answer, name)