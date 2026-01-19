#First Program : Ask user for name and birth year. Then print name and age of the user
from datetime import datetime #for getting datetime dynamically
name = input("Input your name : ")
birth_year = int(input("Input your birth year : "))
age = datetime.now().year - birth_year
print(f"{name}, your age is {age}")
