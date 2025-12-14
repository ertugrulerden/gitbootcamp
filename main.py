def example_function():
    print("Example.")
    for i in range(3):
        print(i + 1)

def another_example():
    print("Anotherr.")
    for item in ["One", "Two", "Three", "four","five"]:
        print(f"item:{item}\n")

def math_example(x, y):
    print(f"sum:{x + y} ", x * y)

def nested_example():
    print("Nested.")
    print("Inner.")
    for c in "ABC":
        print(c)

def user_input_example():
    print("Hello, TestUser")

if __name__ == "__main__":
    example_function()
    another_example()
    math_example(4, 7)
    nested_example()
    user_input_example()


