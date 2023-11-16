# This is a sample Python script.
import itertools
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

def attack_selector(password):
    print('Welcome to the dictionary / brute force attack simulator.  Select one of the following options:\n')
    selection = input('1 - Run a dictionary attack using the 14 million most common passwords from the 2009 RockYou.txt leak \n'
                      '2 - Run a brute force attack using only symbols and numbers \n enter number:')
    if selection == '1':
        dictionary_attack(password)
        return
    if selection == '2':
        brute_force(password)
        return
    else:
        print('not a valid entry, please select one of the following options')
        attack_selector(password)


def attack_sequencer(func):
    def attack(password):
        print(f'Running {func.__name__}...\n')
        start_time = time.time()
        func(password)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{func.__name__} complete in in {round(execution_time, 4)} seconds \n')

    return attack

@attack_sequencer
def dictionary_attack(password):

    with open('rockyou.txt',encoding='latin1') as file:
        lines = [line.strip('\n') for line in file]
        print(f'checking for your password against {len(lines)} entries')

    for index, line in enumerate(lines):
        if line == password:
            print(f'password found at line {index + 1}!')
            return

    else:
        print(f'Password was not found in any of the {len(lines)} entries')
        attack_selector(password)
@attack_sequencer
def brute_force(password):
    lowercase_chars = [chr(i) for i in range (ord('a'), ord('z')+1)]
    uppercase_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    number_chars = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    char_list = lowercase_chars + uppercase_chars + number_chars

    for length in range(0,9):
        for index, guess in enumerate(itertools.product(char_list, repeat = length)):
            guess = ''.join(guess)
            print(f'checking password {index + 1}, current guess = \'{guess}\'')
            if guess == password:
                print(f'password \'{guess}\' brute forced in {index + 1} attempts!')
                return

# TODO
#user workflow - do dictionary first, if not found ask if they want to brute force or give up?
#
#time elapsed for brute forced as its running
#clean terminal up so it displays rather than updates
#Expand on your program to either do a dictionary/brute force attack. Hint: you can use args to do this ;)
#how to point at doms server?
def main():
    password = input('Enter password Password:> ')


    attack_selector(password)
    # dictionary_attack(password)
    # brute_force(password)



if __name__ == '__main__':
    main(),
