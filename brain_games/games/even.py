import random
from brain_games.functions import greeting
from brain_games.functions import is_even
from brain_games.functions import result

def even_game():
    name = greeting('What is the result of the expression?')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_num = 0

    while correct_num < 3:
        random_number = random.randint(1, 100)

        print('Question:', random_number)

        correct_answer = 'yes' if is_even(random_number) else 'no'

        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_num += 1
        else:
            break
        
    result(correct_num, correct_answer, answer, name)