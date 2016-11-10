#!/usr/bin/python
import math

number = int(raw_input("Enter a number of your choice :"))
if number%2 is 0:
    if number%4 is 0:
        print("The number is even and is divisible by 4")
    else:
        print("The number you entered is even")
else:
    print("The number you entered is odd")
