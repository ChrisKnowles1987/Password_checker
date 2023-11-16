# This is a sample Python script.
import itertools
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time



def dictionary_attack(password):
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
        dictionary_attack(password)

def brute_force(password):
    start_time = time.time()
    lowercase_chars = [chr(i) for i in range (ord('a'), ord('z')+1)]
    uppercase_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    number_chars = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    char_list = lowercase_chars + uppercase_chars + number_chars

    for length in range(0,9):
        for index, guess in enumerate(itertools.product(char_list, repeat = length)):
            guess = ''.join(guess)
            print(f'checking password {index + 1}, current guess = \'{guess}\'')
            if guess == password:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f'password \'{guess}\' brute forced in {round(execution_time, 4)} seconds at iteration {index + 1}!')

                return

# TODO
#user workflow - do dictionary first, if not found ask if they want to brute force or give up?
#
#time elapsed for brute forced as its running
#clean terminal up so it displays rather than updates
#Expand on your program to either do a dictionary/brute force attack. Hint: you can use args to do this ;)
#how to point at doms server?
def main():
    print('Can you guess the most common password from the 2009 \'RockYou\' data leak?')
    password = input('Enter password Password:> ')


    brute_force(password)
    dictionary_attack(password)


if __name__ == '__main__':
    main(),
