#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
to_str = str(number)
Last_no = to_str[-1]
Ln = int(Last_no)
if Ln > 5:
    print(f"Last digit of {number} is {Ln} and is greater than 5")
elif Ln == 0:
    print(f"Last digit of {number} is {Ln} and is 0")
elif Ln < 6 and Ln != 0:
    print(f"Last digit of {number} is {Ln} and is less than 6 and not 0")
