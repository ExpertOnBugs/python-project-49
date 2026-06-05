import prompt

def greeting(rules: str): 
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