import random
from brain_games.functions import greeting
from brain_games.functions import prime

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

    if correct_num == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")