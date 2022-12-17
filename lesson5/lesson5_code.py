
def printAddressEntry(addressEntry: list) -> None:
    print("I have an address for " + addressEntry[0] + " " + addressEntry[1])
    print("Here is the street address: " + addressEntry[2])
    print("This person hails from the great state of: " +
          addressEntry[5] + " and lives in the city of " + addressEntry[4])
    print("The can be reached at " +
          addressEntry[3] + " or zipcode " + addressEntry[6])


first_name = "Bob"
last_name = "Henry"
street_address = "123 Maine Street"
phone_number = "867.5309"
city = "Chicago"
state = "Texas"
zipcode = "19270"
address_entry = [first_name, last_name, street_address,
                 phone_number, city, state, zipcode]
printAddressEntry(address_entry)


def printAddressEntryDict(addressEntry: dict) -> None:
    print("I have an address for " +
          addressEntry['firstName'] + " " + addressEntry['lastName'])
    print("Here is the street address: " + addressEntry['streetAddress'])
    print("This person hails from the great state of: " +
          addressEntry['state'] + " and lives in the city of " + addressEntry['city'])
    print("The can be reached at " +
          addressEntry['phoneNumber'] + " or zipcode " + addressEntry['zipcode'])


address_entry = {
    'firstName': first_name,
    'lastName': last_name,
    'streetAddress': street_address,
    'city': city,
    'state': state,
    'zipcode': zipcode,
    'phoneNumber': phone_number
}
printAddressEntryDict(address_entry)


class AddressEntry:
    def __init__(self, firstName, lastName, streetAddress, city, state, zipcode, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber


def printAddressEntryClass(addressEntry: AddressEntry) -> None:
    print("I have an address for " +
          addressEntry.firstName + " " + addressEntry.lastName)
    print("Here is the street address: " + addressEntry.streetAddress)
    print("This person hails from the great state of: " +
          addressEntry.state + " and lives in the city of " + addressEntry.city)
    print("The can be reached at " +
          addressEntry.phoneNumber + " or zipcode " + addressEntry.zipcode)


address_entry = AddressEntry(
    first_name, last_name, street_address, city, state, zipcode, phone_number)
printAddressEntryClass(address_entry)
