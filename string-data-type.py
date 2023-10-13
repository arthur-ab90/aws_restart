myString = "This is a String"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
########Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
########Input
name = input("What is your name? ")
print(name)
########Formatting output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))