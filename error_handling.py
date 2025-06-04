# Division by zero error
def get_quotient(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
    except Exception as e:
        print(f"Unknown error: {e}")
    else:
        print(result)
    finally:
        print("Process complete")

get_quotient(10, 2)
get_quotient(5, 0)

# Runs until a valid value is entered
m = "0"
while True:
    m = str(input("please enter an integer: "))
    try:
        int(m)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    else:
        print(f"You entered: {m}")
        break

# Prevents error in case a file doesn't exist
try:
    with open("read_me.txt", "r") as file:
        return_string = file.read()
        print(return_string)
except FileNotFoundError:
    print("The file 'read_me.txt' does not exist.")
finally:
    print("Attempted to read a file")
