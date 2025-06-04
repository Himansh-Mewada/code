# Variables and data types
my_age = 18
is_learning = True
my_name = "Himansh Mewada"
print(f"my age: {my_age} {type(my_age)}")
print(f"my name: {my_name} {type(my_name)}")
print(f"is learning: {is_learning} {type(is_learning)}")


# Operators
num_a, num_b = 20, 7
print(f"addition: {num_a + num_b}")
print(f"subtraction: {num_a - num_b}")
print(f"multiplication: {num_a * num_b}")
print(f"floor division: {num_a // num_b}")
print(f"remainder: {num_a % num_b}")

is_sunny = True
print(not(is_sunny))

counter = 0
counter += 5
print(counter)


# Control flow
num = 23
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

for i in range(1,11):
    print(i)

x = 10
while x > 0:
    print(x)
    x -= 1

colors = ['red','blue','green',"yellow"]
for color in colors:
    if color == 'blue':
        continue
    print(color)


# Data structures
my_numbers = [5,4,3,2,1]

print(my_numbers[0],"\n",my_numbers[-1])

middle_numbers = my_numbers[1:4]

my_numbers.append(0)

my_numbers.insert(0,6)

my_numbers.remove(3)

print(my_numbers)


# Tuples
weekdays = 'Monday','Tuesday','Wednesday'

print(weekdays[1])

# weekdays[1] = 'Tueday'

numbers_and_letters = (1, 'a', 2, 'b', 2, 'c')
print(numbers_and_letters.count(2))

values = (100,200)
value1, value2 = values
print(f"{value1} \n{value2}")


# Dictionaries
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car.get("model"))

car['color'] = 'red'

car['year'] = 2024

del car['brand']

for key, value in car.items():
    print(f"{key} : {value}")


# Sets
fruit_set = {'apple', 'banana', 'orange', 'apple', 'grape'}
print(fruit_set)

fruit_set.add('kiwi')

fruit_set.update(['mango', 'cherry', 'banana'])

fruit_set.remove('banana')

fruit_set.discard('pineapple')

programming_language_1 = {"Python", "Java", "C++"}
programming_language_2 = {"Java", "JavaScript", "Python", "Go"}

print(programming_language_1 | programming_language_2)

print(programming_language_2 & programming_language_1)
