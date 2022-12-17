class AddressEntry:
    def __init__(self, firstName, lastName, streetAddress, city, state, zipcode, phoneNumber, astroSign, age, email, alreadyMarried):
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.astroSign = astroSign
        self.email = email
        self.age = age
        self.alreadyMarried = alreadyMarried


def getAddressItem(addressItemName: str) -> str:
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


# This section is getting information for one person
print("Please enter the address details of one person.")
first_name = getAddressItem("first name")
last_name = getAddressItem("last name")
address = getAddressItem("address")
city = getAddressItem("city")
state = getAddressItem("state")
zipcode = getAddressItem("zipcode")
astro_sign = getAddressItem("astro sign")
email = getAddressItem("email")
already_married = getAddressItem(
    "your marital status? Would you say that you are married").lower() == "yes"
age = int(getAddressItem("age"))
phone_number = getAddressItem("phone number")

address_entry = AddressEntry(
    firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)
# End of section


# This section is getting information for one person
print("Please enter the address details of one person.")
first_name = getAddressItem("first name")
last_name = getAddressItem("last name")
address = getAddressItem("address")
city = getAddressItem("city")
state = getAddressItem("state")
zipcode = getAddressItem("zipcode")
astro_sign = getAddressItem("astro sign")
email = getAddressItem("email")
already_married = getAddressItem(
    "your marital status? Would you say that you are married").lower() == "yes"
age = int(getAddressItem("age"))
phone_number = getAddressItem("phone number")

address_entry1 = AddressEntry(
    firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)
# End of section

# This section is getting information for one person
print("Please enter the address details of one person.")
first_name = getAddressItem("first name")
last_name = getAddressItem("last name")
address = getAddressItem("address")
city = getAddressItem("city")
state = getAddressItem("state")
zipcode = getAddressItem("zipcode")
astro_sign = getAddressItem("astro sign")
email = getAddressItem("email")
already_married = getAddressItem(
    "your marital status? Would you say that you are married").lower() == "yes"
age = int(getAddressItem("age"))
phone_number = getAddressItem("phone number")

address_entry2 = AddressEntry(
    firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)
# End of section

# This section is getting information for one person
print("Please enter the address details of one person.")
first_name = getAddressItem("first name")
last_name = getAddressItem("last name")
address = getAddressItem("address")
city = getAddressItem("city")
state = getAddressItem("state")
zipcode = getAddressItem("zipcode")
astro_sign = getAddressItem("astro sign")
email = getAddressItem("email")
already_married = getAddressItem(
    "your marital status? Would you say that you are married").lower() == "yes"
age = int(getAddressItem("age"))
phone_number = getAddressItem("phone number")

address_entry3 = AddressEntry(
    firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)
# End of section

# Loop example
a = 10
while a > 5:
    print("The current value of a is: " + str(a))
    a = a - 1
print("The final value of a is: " + str(a))


def askUserToContinue() -> bool:
    # TODO: fill this out for homework
    return False


def printAddressBook(addressBook: list) -> None:
    # TODO: fill this out for homework
    pass


address_book = []
canContinue = True
while canContinue:

    print("Please enter the address details of one person.")
    first_name = getAddressItem("first name")
    last_name = getAddressItem("last name")
    address = getAddressItem("address")
    city = getAddressItem("city")
    state = getAddressItem("state")
    zipcode = getAddressItem("zipcode")
    astro_sign = getAddressItem("astro sign")
    email = getAddressItem("email")
    already_married = getAddressItem(
        "your marital status? Would you say that you are married").lower() == "yes"
    age = int(getAddressItem("age"))
    phone_number = getAddressItem("phone number")

    address_entry = AddressEntry(
        firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)
    address_book.append(address_entry)
    canContinue = askUserToContinue()
printAddressBook(address_book)
