# ==============================
# Exercise 1: Local vs Global Scope
# ==============================

x = "Global Variable"   # Global scope

def scope_test():
    x = "Local Variable"  # Local scope
    print("Inside function:", x)

scope_test()
print("Outside function:", x)


# ==============================
# Exercise 2: Namespace Exploration
# ==============================

def count_function():
    count = 10  # Local variable inside count_function
    print("Count inside count_function:", count)

def log_function():
    count = "Log message count"  # Local variable inside log_function
    print("Count inside log_function:", count)

count_function()
log_function()


# ==============================
# Exercise 3: Scope Hierarchy (LEGB Rule)
# ==============================

x = "Global Variable"  # Global scope

def outer_function():
    x = "Enclosing Variable"  # Enclosing scope

    def inner_function():
        # Python searches in order: Local -> Enclosing -> Global -> Built-in
        print("Accessing variable in inner_function:", x)  

    inner_function()
    print("Accessing variable in outer_function:", x)

outer_function()
print("Accessing variable in global scope:", x)

# Explanation of LEGB Rule:
# L = Local (variables inside the current function)
# E = Enclosing (variables in outer functions)
# G = Global (variables defined at the top level of the script)
# B = Built-in (Python’s reserved names, like print, len, etc.)
