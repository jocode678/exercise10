# password = '1234'
# attempt = 1
# while attempt <= 3:
#     supplied_pin = input("Enter your PIN: ")
#     if password == supplied_pin:
#         print('It is a match')
#         break
#     else:
#         print('That is the incorrect password, please try again')
#         print('You have tried ', attempt, ' times. You have ', 3 - attempt, 'attempts remaining')
#         attempt += 1
# else:
#     print('You have run out of attempts')

import getpass
password = '1234'
attempt = 1
while attempt <= 3:
    supplied_pin = getpass.getpass(prompt="Enter your PIN: ", stream=None)
    if password == supplied_pin:
        print('It is a match')
        break
    else:
        print('That is the incorrect password, please try again')
        print('You have tried ', attempt, ' times. You have ', 3 - attempt, 'attempts remaining')
        attempt += 1
else:
    print('You have run out of attempts')