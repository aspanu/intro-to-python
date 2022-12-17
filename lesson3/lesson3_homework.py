# Update what you had before asking the user to input at least 5 different items to use a small function
# Use functions to perform the transformations so you don’t need to copy that code
# Move the code which pretty prints an entry into it’s own separate function
# Add 2 more user inputs to your address book which have different types

# Starting with

'''
print("Please enter your name:")
name = input()
print("Please enter your address:")
address = input()
print("Please enter your zip code:")
zipcode = input()
print("Please enter your astrological sign:")
astro_sign = input()
print("Please enter your email address:")
email = input()
'''

# Going to


def getAddressItem(addressItemName):
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


def prettyPrintAddressEntry(name, address, zipcode, astroSign, email, alreadyMarried, age):
    print("Hello " + name)
    print("Hope you're doing well!")
    print("Here is what I know about you now:")
    print("You live at " + address + " in the zipcode " + zipcode)
    print("You can be reached at the email address " + email +
          " where we should send you everything about being a " + astroSign)
    print("Also, it turns out it is " + str(alreadyMarried) +
          " that you are already married.")
    print("Finally, we are in the esteemed presence of someone who is " +
          str(age) + " old!")


def capitalize(item):
    return item.upper()


name = getAddressItem("name")
address = getAddressItem("address")
zipcode = getAddressItem("zipcode")
astro_sign = getAddressItem("astro_sign")
email = getAddressItem("email")
already_married = getAddressItem(
    "your marital status? Would you say that you are married").lower() == "yes"
age = int(getAddressItem("age"))

address = capitalize(address)
astro_sign = capitalize(astro_sign)

prettyPrintAddressEntry(name, address, zipcode,
                        astro_sign, email, already_married, age)
