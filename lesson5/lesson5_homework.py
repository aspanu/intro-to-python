# Add a class
# Use the class in functions it makes sense to add it
# Add a few more input fields

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


def prettyPrintAddressEntry(addressEntry: AddressEntry) -> None:
    print("Hello " + addressEntry.firstName)
    print("Hope you're doing well!")
    print("Here is what I know about you now:")
    print("You live at " + addressEntry.streetAddress +
          " in the zipcode " + addressEntry.zipcode)
    print("You can be reached at the email address " + addressEntry.email +
          " where we should send you everything about being a " + addressEntry.astroSign)
    print("Also, it turns out it is " + str(addressEntry.alreadyMarried) +
          " that you are already married.")
    print("Finally, we are in the esteemed presence of someone who is " +
          str(addressEntry.age) + " old!")
    print("By the way, this person's last name is " + addressEntry.lastName)
    print("As well, they live in the state of " + addressEntry.state)


def capitalize(item: str) -> str:
    return item.upper()


def understandAlreadyMarried(alreadyMarried: str) -> bool:
    # Translate from a string to a bool of whether married or not
    if alreadyMarried.lower == "yes":
        return True
    elif alreadyMarried[0] == 'y':
        return True
    else:
        return False


def formatZipCode(zipcode: str) -> str:
    # If the zipcode given is the full 9 digit zipcode, store it in a pretty way
    if len(zipcode) == 9:
        # Full zipcode should have a hyphen in it
        return zipcode[0:5] + "-" + zipcode[5:]
    else:
        return zipcode


def fixEmail(email: str) -> str:
    # If the email doesn't have an '@'
    # assume that it is a gmail email
    if "@" not in email:
        return email + "@gmail.com"
    else:
        return email


print("Please enter the address details of one person.")
first_name = getAddressItem("first name")
last_name = getAddressItem("last name")
address = getAddressItem("address")
city = getAddressItem("city")
state = getAddressItem("state")
zipcode = formatZipCode(getAddressItem("zipcode"))
astro_sign = getAddressItem("astro sign")
email = fixEmail(getAddressItem("email"))
already_married = understandAlreadyMarried(getAddressItem(
    "your marital status? Would you say that you are married").lower())
age = int(getAddressItem("age"))
phone_number = getAddressItem("phone number")

address = capitalize(address)
astro_sign = capitalize(astro_sign)
state = capitalize(state)

address_entry = AddressEntry(
    firstName=first_name, lastName=last_name, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phone_number, astroSign=astro_sign, age=age, email=email, alreadyMarried=already_married)

prettyPrintAddressEntry(addressEntry=address_entry)
