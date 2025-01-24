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
