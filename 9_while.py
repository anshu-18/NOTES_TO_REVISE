cmd = ""
while cmd != 'quit':
    cmd = input("> ")
    if cmd == 'start':
        print('car started')
    elif cmd == 'stop':
        print('car stopped')
    else:
        print('''Follow below instructions: 
start - to start the car
stop - to stop the car
quit - to quit''')