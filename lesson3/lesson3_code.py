# Starting code from the homework last time

print("What is the first name for the address book?")
firstName = input()
print("What is the last name for the address book?")
lastName = input()
print("What is the street address for the address book?")
streetAddress = input()
print("What is the city for the address book?")
city = input()
print("What is the zip code for the address book?")
zipCode = input()
print("What is the phone number for the address book?")
phoneNumber = input()
print("What is the email address for the address book?")
emailAddress = input()


# "Refactored" by creating a function!
def getAddressItem(addressItemName):
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


firstName = getAddressItem("first name")
lastName = getAddressItem("last name")
streetAddress = getAddressItem("street address")
city = getAddressItem("city")
zipCode = getAddressItem("zip code")
phoneNumber = getAddressItem("phone number")
emailAddress = getAddressItem("email address")
