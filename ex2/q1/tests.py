import unittest
from q1 import find_email_addresses


class MyTestCase(unittest.TestCase):
    def test_something(self):
        valid, invalid = find_email_addresses("file1.txt")
        self.assertEqual(valid,
                         ['Oriya@gmail.com', 'yonatan_alp@walla.com', 'noa.tap@yahoo.co.il', 'orianmar@outlook.cc'])
        self.assertEqual(invalid, ['prize.@money.com', 'fake_-address@fun.cm', '.inv@fun.cm', 'unsub@fun.c'])


if __name__ == '__main__':
    unittest.main()
