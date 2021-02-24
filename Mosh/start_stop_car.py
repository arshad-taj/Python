
while True:
    user_input = input('> ')
    if user_input.lower() == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit  
                 ''')

    elif user_input.lower() == 'start':
        print('car started...')
    elif user_input.lower() == 'stop':
        print('car stopped')
    elif user_input.lower() == 'quit':
        break
    else:
        print("I don't undertand that...")



