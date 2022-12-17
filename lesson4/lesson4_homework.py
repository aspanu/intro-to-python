# Add type hints to functions

def getAddressItem(addressItemName: str) -> str:
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


def prettyPrintAddressEntry(name: str, address: str, zipcode: str, astroSign: str, email: str, alreadyMarried: bool, age: int) -> None:
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


name = getAddressItem("name")
address = getAddressItem("address")
zipcode = formatZipCode(getAddressItem("zipcode"))
astro_sign = getAddressItem("astro_sign")
email = fixEmail(getAddressItem("email"))
already_married = understandAlreadyMarried(getAddressItem(
    "your marital status? Would you say that you are married").lower())
age = int(getAddressItem("age"))

address = capitalize(address)
astro_sign = capitalize(astro_sign)

prettyPrintAddressEntry(name, address, zipcode,
                        astro_sign, email, already_married, age)
