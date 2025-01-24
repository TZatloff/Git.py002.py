import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()


# main.py
def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}")
def greet(name): return f"Hello, {name}!"

def factorial(n): return 1 if n == 0 else n * factorial(n-1)

if __name__ == "__main__":
    print(greet(input("Enter your name: ")))
    print(f"The factorial of {number := int(input('Enter a number to calculate its factorial: '))} is {factorial(number)}")