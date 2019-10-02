import time
import unittest


class D(object):
    def __init__(self, name="D"):
        self.name = name
        self.time_created = time.time()

    def print_D(self):
        print(self.return_D())
        return True

    def return_D(self):
        return("D")

    def get_time_created(self):
        return self.time_created


class TestD(unittest.TestCase):
    def test_return_D(self):
        self.assertEqual(D().return_D(), "D")


if __name__ == '__main__':
    unittest.main()
