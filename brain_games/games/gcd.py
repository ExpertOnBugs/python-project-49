import random
from brain_games.functions import greeting
from brain_games.functions import gcd
from brain_games.functions import result

def gcd_game():
    name = greeting('Find the greatest common divisor of given numbers.')

    correct_num = 0

    while correct_num < 3:

        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)

        correct_answer = gcd(first_number, second_number)

        print(f'Question: {first_number} {second_number}')

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')
            correct_num += 1
        else:
            break
    
    result(correct_num, correct_answer, answer, name)