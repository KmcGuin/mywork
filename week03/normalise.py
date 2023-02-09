# normalise.py
# Author: Kealan McGuinness
# Week03 Strings noramlise

rawstring = input("Please enter a string: ")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalised = len(normalisedstring)

print(f"That String normalised is: {normalisedstring}")
print(f"We reduced the input from {lengthofrawstring} to {lengthofnormalised} characters")
