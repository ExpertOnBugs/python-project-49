import random
from brain_games.cli import welcome_user

def is_even(number: int) -> bool:
    return number % 2 == 0

def game():
    print('Welcome to the Brain Games!')

    name = welcome_user()

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
        
    if correct_num == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")

def main():
    game()
  
if __name__ == "__main__":
    main()