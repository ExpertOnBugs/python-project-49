import random

from brain_games.functions import greeting, result


def calc_game():
    name = greeting('What is the result of the expression?')

    operations = {1: '+', 2: '-', 3: '*'}
    
    points = 0

    ATTEMPTS = 3

    while points < ATTEMPTS:
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
            points += 1
        else:
            break

    result(points, correct_answer, answer, name)

    