# Will print out "Hello Adrian"
a = "Adrian"
print("Hello " + a)

# Will print out "Hello Not Adrian"
a = "Adrian"
a = "Not Adrian"
print("Hello " + a)

# Will also print out "Hello Not Adrian"
a = "Not Adrian"
print("Hello " + a)

# Will print out Hello AdrianSomethingElse
aNameForOurVariable = "Adrian"
someOtherNameItDoesntMatterWhatItIs = "SomethingElse"
print("Hello " + aNameForOurVariable + someOtherNameItDoesntMatterWhatItIs)

# Print out "Hello ADRIAN"
something = "Adrian"
print("Hello " + something.upper())

# Get the user input and output it
print("Please enter your name:")
userInput = input()
print("Hello " + userInput)

# Return the uppercase version of the user input
print("Please enter your name:")
userInput = input()
userInput = userInput.upper()
print("Hello " + userInput)

# Get multiple user inputs
print("Please enter your name:")
name = input()
print("Please enter your address:")
address = input()
print("Hello " + name + " who lives at " + address)
