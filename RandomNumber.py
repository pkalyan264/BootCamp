# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def guess_the_number():
    """
    Takes user input until user guesses the number
    correctly and keeps track of num of guesses.
    :return: int
    """
    random_number_generated = random.randint(0, 100)
    guesses = 0    # Counting Guesses
    prev = -1
    prev_diff = 300

    while prev != random_number_generated:
        curr = int(input())
        guesses += 1
        curr_diff = abs(curr - random_number_generated)

        if curr < 0 or curr > 100:
            print("Out of Bounds")
        else:
            if guesses == 1:    # First Guess
                if curr_diff <= 10:
                    print("WARM")
                else:
                    print("COLD")

            else:
                if curr_diff > prev_diff:
                    print("COLDER")
                elif curr_diff == 0:
                    print("Hurrah You've Guessed it right and you've taken {} chances".format(guesses))
                    return guesses
                else:
                    print("WARMER")
            prev = curr
            prev_diff = curr_diff

    return guesses


guess_the_number()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
