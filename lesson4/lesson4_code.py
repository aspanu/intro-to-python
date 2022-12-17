a = "12"
b = "24"
print(a + b)  # what do you think that this returns?

# This will return "1224" because both a and b are strings


a = 12
b = 24
print(a * 4)
print(a - 82)
print(a + b)

# In this case we will print:
# 48
# -70
# 36


myBoolean = True
print(myBoolean)

# This will show 'True', something which was alluded to in the last homework

myArray = [12, 4, 82]
print(myArray)

# This will show all items in the array: [12, 4, 82]

myArray = ["abc", 82, False]
print(myArray)

# The array will show ["abc", 82, False]

myArray = ["abc", 82, False]
print(myArray[0])  # "abc"
print(myArray[2])  # False

myArray = [12, 4, 82, 26, 71, 93]
myArray[2]  # 82
myArray[:2]  # [12, 4]
myArray[2:]  # [82, 26, 71, 93]

s = "myString"
s[3:]  # "tring"

# Control flow

phone_number = "(123)-728-8109"
if "(" in phone_number:
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
print(phone_number)
# phone_number is now "123-728-8109"

# Dealing with 2 cases
phone_number = "142.872.9182"
if "(" in phone_number:
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
elif "." in phone_number:
    phone_number = phone_number.replace(".", "-")
print(phone_number)
# phone_number will now be "142-872-9182"


def getAddressItem(addressItemName: str) -> str:
    print("What is the " + addressItemName + " for the address book?")
    fromUser = input()
    return fromUser


def formatPhoneNumber(phoneNumber: str) -> str:
    if "(" in phoneNumber:
        phoneNumber = phoneNumber.replace("(", "")
        phoneNumber = phoneNumber.replace(")", "")
    elif "." in phoneNumber:
        phoneNumber = phoneNumber.replace(".", "-")
    return phoneNumber


firstName = getAddressItem("first name")
lastName = getAddressItem("last name")
streetAddress = getAddressItem("street address")
city = getAddressItem("city")
zipCode = getAddressItem("zip code")
phoneNumber = formatPhoneNumber(getAddressItem("phone number"))
emailAddress = getAddressItem("email address")
