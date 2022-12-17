# File Reading and Writing

theStringIWantToWriteToAFile = "Hello world\nor whatever"

fileHandle = open("fileName.txt", "w")  # "w" specifies that it is write mode
# the name of the file that we are creating is "fileName.txt"
# which we have chosen ourselves

fileHandle.write(theStringIWantToWriteToAFile)
fileHandle.close()

read_file_handle = open("filename.txt", "r")
file_contents = read_file_handle.read()
theStringVersionOfTheEntireContentsOfTheFile = file_contents
theListVersionOfTheContents = file_contents.splitlines()
read_file_handle.close()

print(theListVersionOfTheContents)
print(theStringVersionOfTheEntireContentsOfTheFile)


# Serializing and Deserializing

class AddressEntry:
    # we have a __init__ member function that we already defined
    def __init__(self, firstName, lastName, streetAddress, city, zipcode):
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.city = city
        self.zipcode = zipcode

    def printEntry(self) -> None:
        print("This is the address entry for " + self.firstName)
        print("Right now, we have a last name as well: " + self.lastName)
        # ...

    def toCSVString(self) -> str:
        return self.firstName+","+self.lastName+","+self.streetAddress+","+self.city+","+self.zipcode


def makeExportableAddressBook(addressBook: list) -> list:
    # Go through each line of address book, which is an 'AddressEntry' instance
    # and call toCSVString() on them
    exportBook = []
    for entry in addressBook:
        exportBook.append(entry.toCSVString())
    return exportBook


def writeToFile(fileHandle, exportableAddressBook: list) -> None:
    fileHandle.write("\n".join(exportableAddressBook))


address_book = []
first_name = "Bob"
last_name = "Henry"
street_address = "1323 Maine Junction"
city = "Denver"
zipcode = "90210"
address_entry = AddressEntry(
    first_name, last_name, street_address, city, zipcode)
address_book.append(address_entry)

first_name = "Alice"
last_name = "Jones"
street_address = "8712 Where AmI Boulevard"
city = "Phoenix"
zipcode = "71202"
address_entry = AddressEntry(
    first_name, last_name, street_address, city, zipcode)
address_book.append(address_entry)

# using the address book from above
exportable_address_book = makeExportableAddressBook(address_book)
# exportable_address_book will be a list of strings - that's what makes it 'exportable'
# write all of the strings to the file
with open("saveFile.txt", "w") as file_handle:
    writeToFile(file_handle, exportable_address_book)


def createAddressEntryFromReadLine(commaLine: str) -> AddressEntry:
    values = commaLine.split(",")
    return AddressEntry(values[0], values[1], values[2], values[3], values[4])


def printAddressBook(addressBook: list) -> None:
    print("The entirety of the address book is presented here")
    for entry in addressBook:
        entry.printEntry()


# Now let us deserialize into a new address book variable!
with open("saveFile.txt", "r") as read_file:
    fileLineList = read_file.read().splitlines()

read_address_book = []
for line in fileLineList:
    read_address_book.append(createAddressEntryFromReadLine(line))
printAddressBook(read_address_book)
