# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time



def password_checker(password):
    start_time = time.time()

    with open('rockyou.txt',encoding='latin1') as file:
        lines = [line.strip('\n') for line in file]
        print(f'checking for your password against {len(lines)} entries')

    for index, line in enumerate(lines):
        if line == password:
            print(f'password found at line {index + 1}!')
            end_time = time.time()
            execution_time = end_time - start_time
            print(f'Password found in {round(execution_time, 4)} seconds')

            return

    else:
        print(f'Password was not found in any of the {len(lines)} entries!  Try again?')
        password = input('Enter password Password:> ')
        password_checker(password)



# TODO
# Rename current method password_checker to be called dictionary_attack
# Create a new function: called Brute Force.
    # Inside this function use the characters = numbers, letters to crack 'password123'
    # Do what you did in dictionary_attack with outputting time taken to crack a password.
#Expand on your program to either do a dictionary/brute force attack. Hint: you can use args to do this ;)
def main():
    print('Can you guess the most common password from the 2009 \'RockYou\' data leak?')
    password = input('Enter password Password:> ')

    password_checker(password)


if __name__ == '__main__':
    main(),
