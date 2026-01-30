#Third Program : Ask user for name and birth year. Then print name and age of the user checking condition and handle error using try/except
import os
from datetime import datetime
name = input("Input your name : ")
try:
  birth_year = int(input("Input your birth year : "))
except ValueError:
  print("Invalid Input")
  os.sys.exit()
age = datetime.now().year - birth_year
if(age < 0) :
    print("Invalid Birth Year")
elif(age > 120) :
    print("Unrealistic Age")
else :
    print(f"{name}, your age is {age}")
