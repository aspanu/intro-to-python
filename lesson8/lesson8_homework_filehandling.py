# Write a program which writes some strings to a file
# Read it back and print out the strings that you read from the file!

first_string = "This is just a string I want to write"
second_string = "another string, whatever"
third_string = "The last string to write"

strings_as_array = [first_string, second_string, third_string]

with open("writefile.txt", "w") as file_handle:
    file_handle.write("\n".join(strings_as_array))

with open("writefile.txt", "r") as read_file:
    file_contents = read_file.read()
    # read as list:

    print(file_contents.splitlines())
    # read as a single string:
    print(file_contents)

# Try to download a CSV file from the internet, save it into a file, and then read it from a file and print it to the screen
# file: testCSV.csv
with open("testCSV.csv", "r") as csv_file:
    listOfCsvFields = []  # 2D list
    for line in csv_file.read().splitlines():
        listOfCsvFields.append(line.split(","))

print(listOfCsvFields)
