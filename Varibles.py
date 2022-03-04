# this is a comment 
# this is a print method. print will echo out anything inside the ()round brackets to the terminal, when we run the file.
from unicodedata import name


print("This is my very first python script!")

#variables are placeholders, with dynamic values -> things that can change
# they get stored in memory and referenced later

name = "Yuki"
age = 34
eyecolor = "brown"
haircolor = "black"

#Arrays are variables on steriods. they let us store many values in one 
#variable -> to help us group data
# this make our scripting files easier to understand and work it.
# car1 = "Volvo"
# car2 = "Toyota"
# car3 = "Fiesta"
cars = ["Volvo", "Toyota", "Fieesta"]

print("My name is " + name)

# input is another python "thing" - it waits a flashing cursor
alternateName = input("what is YOUR name?")

print("My name is now " + alternateName)

print("My age is " + str(age))
