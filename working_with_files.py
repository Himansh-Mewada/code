with open("my_notes.txt", "w") as file:
    file.write("My first note on python.\n")
    file.write("File handling is interesting.\n")
    file.write("Always remember to close files.")

with open("my_notes.txt", "a") as file:
    file.write("\nand the with statement is best practice.")

with open("my_notes.txt", "r") as file:
    return_string = file.read()
    print(return_string)

with open("my_notes.txt", "r") as file:
    for line in file:
        print(line, end='')
