#!/usr/bin/python

from datetime import date
import math

name = raw_input("Give me your name:")
age = int(raw_input("What is your current age:"))

year = date.today().year
print("Current Year is :",year)

birthYear = year-age
print("Your BirthYear was :" ,birthYear)
hunderedYear = birthYear + 100
print("Hello "+ name + " you'll be 100 years old in :"% hunderedYear)
