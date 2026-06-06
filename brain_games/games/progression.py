import random
from brain_games.functions import greeting
from brain_games.functions import progression
from brain_games.functions import result

def progression_game():
    name = greeting('What number is missing in the progression?')

    correct_num = 0

    while correct_num < 3:
        progressions = progression()

        hidden = random.randint(0, 9)

        correct_answer = progressions[hidden]
        progressions[hidden] = '..'

        print('Question:', *progressions)

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')
            correct_num += 1
        else:
            break

    result(correct_num, correct_answer, answer, name)