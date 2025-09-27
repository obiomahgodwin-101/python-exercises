# Exercise 1: Greet the user by name
def greet_user(name):
    greeting = f"Hello, {name}! Welcome!"
    print(greeting)


# Exercise 2: Calculate the area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area


# Exercise 3: Check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Test the functions
if __name__ == "__main__":
    greet_user("Godwin")
    print("The area of the rectangle is:", rectangle_area(10, 5))
    check_even_odd(7)
    check_even_odd(12)
