# main.py
def greet(name):
    return f"Hello, {name}!"


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}")


def greet(name): return f"Hello, {name}!"


def factorial(n): return 1 if n == 0 else n * factorial(n - 1)

def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}")
    def square(number):
       return number ** 2

    def square(number):
      return number ** 2

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its square: "))
    print(f"The square of {number} is {square(number)}")




