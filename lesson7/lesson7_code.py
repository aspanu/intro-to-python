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


first_name = "Bob"
last_name = "Henry"
street_address = "1323 Maine Junction"
city = "Denver"
zipcode = "90210"

address_entry = AddressEntry(
    first_name, last_name, street_address, city, zipcode)
address_entry.printEntry()
