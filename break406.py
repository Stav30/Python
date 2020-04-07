"""
break statement causes immediate exit from loop
promput user to 'Enter name: '
when user enters stop for name --> exit the loop using break stmt
"""
while True:
    name = input('Enter name: ')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age)**2)
    
