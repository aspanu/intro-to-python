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


def askUserToContinue() -> bool:
    print("Do you want to add any more addresses?")
    userDesire = input()
    if userDesire.lower() == "yes":
        return True
    else:
        return False


def printAddressBook(addressBook: list) -> None:
    print("The entirety of the address book is presented here")
    for entry in addressBook:
        print("=========== Entry Starting ===========")
        prettyPrintAddressEntry(entry)
        print("=========== Entry Complete ===========")


def analyzeAddressBook(addressBook: list) -> str:
    return "The address book has " + str(len(addressBook)) + " entries inside of it"


def getOneAddressEntryFromUser() -> AddressEntry:
    firstName = getAddressItem("first name")
    lastName = getAddressItem("last name")
    address = getAddressItem("address")
    city = getAddressItem("city")
    state = getAddressItem("state")
    zipcode = formatZipCode(getAddressItem("zipcode"))
    astroSign = getAddressItem("astro sign")
    email = fixEmail(getAddressItem("email"))
    alreadyMarried = understandAlreadyMarried(getAddressItem(
        "your marital status? Would you say that you are married").lower())
    age = int(getAddressItem("age"))
    phoneNumber = getAddressItem("phone number")

    address = capitalize(address)
    astroSign = capitalize(astroSign)
    state = capitalize(state)

    address_entry = AddressEntry(
        firstName=firstName, lastName=lastName, streetAddress=address, city=city, state=state, zipcode=zipcode, phoneNumber=phoneNumber, astroSign=astroSign, age=age, email=email, alreadyMarried=alreadyMarried)
    return address_entry


address_book = []
canContinue = True
while canContinue:

    address_entry = getOneAddressEntryFromUser()

    address_book.append(address_entry)
    canContinue = askUserToContinue()

printAddressBook(address_book)
print(analyzeAddressBook(address_book))
