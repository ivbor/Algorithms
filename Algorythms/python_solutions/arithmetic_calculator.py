#basic arithmetic, enhance with gui

def pick_operator():
    a = input('Pick operator: **, -, %, /, //, +, *\n')
    return a

def calculate(num1, num2, a):
    if a == '**':
        print(num_1 ** num_2)
    elif a == '-':
        print(num_1 - num_2)
    elif a == '%':
        print(num_1 % num_2)
    elif a == '/':
        print(num_1 / num_2)
    elif a == '//':
        print(num_1 // num_2)
    elif a == '+':
        print(num_1 + num_2)
    elif a == '*':
        print(num_1 * num_2)
    else:
        raise ValueError


#basic input system with error handling
while True:
    try:
        #the input is here
        num_1 = int(input("Enter first number:\n"))
        #the input is here
        break
    except:
        err = input('Wrong number type, do you want to enter again? (Y or N)   ')
        if err == 'N':
            exit()
        elif err != 'Y' and err != 'N':
            print('Wrong character. Exiting...')
            exit()

while True:
    try:
        #the input is here
        num_2 = int(input('Enter second number:\n'))
        #the input is here
        break
    except:
        err = input('Wrong number type, do you want to enter again? (Y or N)   ')
        if err == 'N':
            exit()
        elif err != 'Y' and err != 'N':
            print('Wrong character. Exiting...')
            exit()

while True:
    #the input is here
    a = pick_operator()
    #the input is here
    try:
        #the calculation is here
        calculate(num_1, num_2, a)
        #the calculation is here
        break
    except:
        err = input('Wrong operator, do you want to enter again? (Y or N)   ')
        if err == 'N':
            exit()
        elif err != 'Y' and err != 'N':
            print('Wrong character. Exiting...')
            exit()



              
