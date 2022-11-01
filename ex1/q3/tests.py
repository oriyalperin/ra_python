import unittest
from q3 import sort


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        s = {'p', 'y', 't', 'h', 'o', 'n'}
        struct = {3: ['f', 'u', 'n'], 6: s, 4: (5, 7, 6, 5)}
        sorted_struct = {3: ['f', 'n', 'u'], 4: (5, 5, 6, 7), 6: {'h', 'n', 'o', 'p', 't', 'y'}}
        self.assertEqual(sorted_struct, sort(struct))


if __name__ == '__main__':
    unittest.main()
