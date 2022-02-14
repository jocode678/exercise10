answer = input('Would you like to do a calculation? Type yes or no: ')
while answer != 'yes' and answer != 'no':
    print('Answer the question properly')
    answer = input('Would you like to do a calculation? Type yes or no: ')
else:
    while answer == 'yes':
        num1 = float(input('Type in your first number: '))
        num2 = float(input('Type in your second number: '))
        operator = input('Type in your operator: ')
        if operator == '+' or operator == 'plus' or operator == 'add':
            print('The answer to your calculation is ', num1 + num2)
        elif operator == '-' or operator == 'minus' or operator == 'subtract':
            print('The answer to your calculation is ', num1 - num2)
        elif operator == '*' or operator == 'multiply' or operator == 'times' or operator == 'x':
            print('The answer to your calculation is ', num1 * num2)
        elif operator == '/' or operator == 'divide':
            if num2 == 0:
                print('You cannot divide by zero!')
            else:
                print('The answer to your calculation is ', num1 / num2)
        else:
            print('please choose an applicable operator')
        answer = input('Would you like to do a calculation? Type yes or no: ')
    else:
        print('You do not have to play with the calculator anymore.')
