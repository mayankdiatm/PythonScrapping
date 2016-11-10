from datetime import date
import math
import sys
print(sys.implementation)

#name =raw_input("Enter your name :")
#age  =int(raw_input("Enter your age :"))

#year = date.today().year
#balanceYear = year-age
#newYear = balanceYear + 100
#print "Hello,",name,"!You'll be 100 years old in ",newYear


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for lessThanFive in (element for element in a if element<5):
    print(lessThanFive)