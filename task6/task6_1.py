import unittest
from fizzbuzz import fizzbuzzz


class FizzBuzzAcceptanceTestCase(unittest.TestCase):
    def test_business_as_usual(self):
        self.assertEqual(fizzbuzzz(1), 1)
        self.assertEqual(fizzbuzzz(51), 51)
        self.assertEqual(fizzbuzzz(23), 23)

    def test_fizz(self):
        self.assertEqual(fizzbuzzz(3), 'fizz')
        self.assertEqual(fizzbuzzz(6), 'fizz')
        self.assertEqual(fizzbuzzz(27), 'fizz')
        self.assertEqual(fizzbuzzz(99), 'fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzzz(5), 'buzz')
        self.assertEqual(fizzbuzzz(10), 'buzz')
        self.assertEqual(fizzbuzzz(20), 'buzz')
        self.assertEqual(fizzbuzzz(500), 'buzz')

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzzz(15), 'fizzbuzz')
        self.assertEqual(fizzbuzzz(30), 'fizzbuzz')
        self.assertEqual(fizzbuzzz(45), 'fizzbuzz')
        self.assertEqual(fizzbuzzz(600), 'fizzbuzz')

    def test_zero(self):
        self.assertEqual(fizzbuzzz(0), 'fizzbuzz')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
