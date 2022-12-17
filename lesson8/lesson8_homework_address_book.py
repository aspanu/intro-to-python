address_book_file_name = "saved_address_book.csv"


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
        self.age = age
        self.email = email
        self.alreadyMarried = alreadyMarried

    def prettyPrint(self) -> None:
        print("Hello " + self.firstName)
        print("Hope you're doing well!")
        print("Here is what I know about you now:")
        print("You live at " + self.streetAddress +
              " in the zipcode " + self.zipcode)
        print("You can be reached at the email address " + self.email +
              " where we should send you everything about being a " + self.astroSign)
        print("Also, it turns out it is " + str(self.alreadyMarried) +
              " that you are already married.")
        print("Finally, we are in the esteemed presence of someone who is " +
              str(self.age) + " old!")
        print("By the way, this person's last name is " + self.lastName)
        print("As well, they live in the state of " + self.state)

    def toCSVString(self) -> str:
        values = [self.firstName, self.lastName, self.streetAddress, self.city, self.state,
                  self.zipcode, self.phoneNumber, self.astroSign, str(self.age), self.email, str(self.alreadyMarried)]
        return ",".join(values)


def makeExportableAddressBook(addressBook: list) -> list:
    # Go through each line of address book, which is an 'AddressEntry' instance
    # and call toCSVString() on them
    exportBook = []
    for entry in addressBook:
        exportBook.append(entry.toCSVString())
    return exportBook


def writeToFile(fileHandle, exportableAddressBook: list) -> None:
    fileHandle.write("\n".join(exportableAddressBook))


def createAddressEntryFromReadLine(commaLine: str) -> AddressEntry:
    values = commaLine.split(",")
    return AddressEntry(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10])


def getAddressItem(addressItemName: str) -> str:
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


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


def askUserBooleanQuestion(question: str) -> bool:
    print(question)
    userDesire = input()
    if userDesire.lower() == "yes":
        return True
    else:
        return False


def printAddressBook(addressBook: list) -> None:
    print("The entirety of the address book is presented here")
    for entry in addressBook:
        print("=========== Entry Starting ===========")
        entry.prettyPrint()
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


def loadAddressBookFromFile() -> list:
    with open(address_book_file_name, "r") as readFile:
        fileLineList = readFile.read().splitlines()

    readAddressBook = []
    for line in fileLineList:
        readAddressBook.append(createAddressEntryFromReadLine(line))
    return readAddressBook


def saveAddressBookToFile(addressBook: list) -> None:
    exportableAddressBook = makeExportableAddressBook(addressBook)
    with open(address_book_file_name, "w") as writeFile:
        writeToFile(writeFile, exportableAddressBook)
    pass


shouldLoad = askUserBooleanQuestion("Should we load an address book?")
if shouldLoad:
    address_book = loadAddressBookFromFile()
else:
    address_book = []


canContinue = askUserBooleanQuestion("Do you want to add any more addresses?")
while canContinue:

    address_entry = getOneAddressEntryFromUser()

    address_book.append(address_entry)
    canContinue = askUserBooleanQuestion(
        "Do you want to add any more addresses?")

printAddressBook(address_book)
print(analyzeAddressBook(address_book))
saveAddressBookToFile(address_book)
