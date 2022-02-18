import random
import sys


def guess_the_number():
    random_number_generated = random.randint(0, 100)
    guesses = 0  # Counting Guesses
    prev = -1
    prev_diff = sys.maxsize

    while prev != random_number_generated:
        curr = int(input())
        guesses += 1
        curr_diff = abs(curr - random_number_generated)

        if curr < 0 or curr > 100:
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
            prev = curr
            prev_diff = curr_diff

    return guesses


