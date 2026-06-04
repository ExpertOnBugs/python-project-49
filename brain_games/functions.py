import prompt

def greeting(rules: str): 
    print('Welcome to the Brain Games!')
    
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!', sep='')

    print(rules)

    return name