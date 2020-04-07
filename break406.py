"""
break statement causes immediate exit from loop
1- prompt user to 'Enter name: ' and assign this value to variable name.
2- if user enters stop for name --> exit the loop using break stmt
3- prompt user to 'Enter age: ' and store value in age
4- use print function with 'Hello', name, '=>', int(age)**2
"""
while True:
    name = input('Enter name: ')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age)**2)
