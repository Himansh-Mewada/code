def say_hello():
    """A simple hello function"""
    print("Hello from my first function!")
say_hello()

def calculate_area(length, width):
    """Calculates the area of a rectangle"""
    area = length * width
    print(area)
calculate_area(length=10, width=5)

def get_circle_circumference(radius):
    """Calculates the circumference of a circle"""
    return 2 * 3.14159 * radius
circumference_result = get_circle_circumference(7)
print(circumference_result)

def print_message(text, times=1):
    """prints a message n number of times"""
    for _ in range(times):
        print(text)
print_message("python is fun!")
print_message("python is fun!", times=3)
