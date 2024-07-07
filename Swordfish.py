while True:
    print('Who are you?')#1
    name = input()       #1
    if name != 'Joe':    #2
        continue         #2
    print('Hello, Joe. What is the password? (It is a fish.)')     #2
    password = input()                                             #2
    if password == 'swordfish':  #3
        break                    #3
print('Access granted.')
