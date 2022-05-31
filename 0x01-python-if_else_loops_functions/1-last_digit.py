#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs (number) % 10
if number < 0:
    last_dig = -last_dig
print("Last digit of {} is {} is".format(number, last_dig), end="")
if last_dig > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")