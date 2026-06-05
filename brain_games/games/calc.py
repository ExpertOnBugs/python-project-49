import random
from brain_games.functions import greeting

def calc_game():
    name = greeting('What is the result of the expression?')

    operations = {1: '+', 2: '-', 3: '*'}
    
    correct_num = 0

    while correct_num < 3:
        num_oper = random.randint(1, 3)
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)

        print(f"Question: {first_num} {operations[num_oper]} {second_num}")

        match num_oper:
            case 1:
                correct_answer = first_num + second_num
            case 2:
                correct_answer = first_num - second_num
            case 3:
                correct_answer = first_num * second_num
    
        answer = int(input("Your answer: "))

        if correct_answer == answer:
            print('Correct!')
            correct_num += 1
        else:
            break

    if correct_num == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")

    