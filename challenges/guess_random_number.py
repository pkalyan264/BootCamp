import random
import sys


def guess_the_number():
    random_number_generated = random.randint(0, 100)
    guesses = 0  # Counting Guesses
    prev = -1
    prev_diff = sys.maxsize

    while prev != random_number_generated:
        curr_guess = int(input())
        guesses += 1
        curr_diff = abs(curr_guess - random_number_generated)

        if curr_guess < 0 or curr_guess > 100:
            print("Out of Bounds")
        else:
            if guesses == 1:  # First Guess
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
            prev = curr_guess
            prev_diff = curr_diff

    return guesses


