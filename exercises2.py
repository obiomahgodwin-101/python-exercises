# Exercise 1: List of favorite fruits
fruits = ["Mango", "Apple", "Banana", "Orange", "Grapes"]
print("My second favorite fruit is:", fruits[1])


# Exercise 2: Dictionary for favorite book
favorite_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self-help"
}
print("The genre of my favorite book is:", favorite_book.get("genre"))


# Exercise 3: Random set of numbers
import random

numbers = [random.randint(1, 10) for _ in range(10)]
unique_numbers = set(numbers)

print("Random numbers generated:", numbers)
print("Unique numbers:", unique_numbers)
