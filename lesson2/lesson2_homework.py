
# Asking the user to input at least 5 different items
print("Please enter your name:")
name = input()
print("Please enter your address:")
address = input()
print("Please enter your zip code:")
zipcode = input()
print("Please enter your astrological sign:")
astro_sign = input()
print("Please enter your email address:")
email = input()

# Transforming the input in at least 3 ways altogether
astro_sign = astro_sign.upper()  # Use all caps for the astrological sign
name = name.title()  # Use title case for the name
address = address.upper()  # Use all caps for the address
email = email.lower()  # Use the lowercase version of email

# Printing the whole entry in a pretty way somehow
print("Hello " + name)
print("Hope you're doing well!")
print("Here is what I know about you now:")
print("You live at " + address + " in the zipcode " + zipcode)
print("You can be reached at the email address " + email +
      " where we should send you everything about being a " + astro_sign)
