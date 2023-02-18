# average.py
# Author: Kealan McGuinness
# Week 04 loops - t keeps reading numbers until the user enters a 0

numbers = []

number = int (input("enter number (0 to quit): "))
while number != 0:
    numbers.append(number)

    number = int(input("enter another number (0 to quit): "))

for value in numbers: 
    print (value)

average = float(sum(numbers)) / len(numbers)
print(f"the average is {average}")

