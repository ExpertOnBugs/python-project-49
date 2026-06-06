import prompt
import random

def greeting(rules: str) -> str: 
    print('Welcome to the Brain Games!')
    
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')

    print(rules)

    return name

def gcd(first_number: int, second_number: int) -> int:
    
    if first_number == 0:
        return second_number

    while second_number != 0:
        temp = first_number
        first_number = second_number
        second_number = temp % second_number
    
    return first_number

def progression() -> list:
    start = random.randint(1, 9)
    step = random.randint(1, 9)

    progressions = [start]

    for i in range(1, 10):
        progressions.append(progressions[i - 1] + step)

    return progressions 

def prime(number: int) -> str:
    check = 0
    for i in range(2, number):
        if number % i == 0:
            check += 1
    
    if check == 0:
        return 'yes'
    else:
        return 'no'
    
def is_even(number: int) -> bool:
    return number % 2 == 0

def result(correct_num: int, correct_answer: str, answer: str, name: str):
    if correct_num == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")