import unittest
from q3 import List


class MyTestCase(unittest.TestCase):
    def test_lists(self):
        mylist = List([[[1, 2, 4], [2, 3]], [1, 2]])
        self.assertEqual(1, mylist[0, 0, 0])
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]],
        ]
        )
        self.assertEqual(mylist[0, 1, 3], 66)
        self.assertEqual(mylist[2], [[13, 14, 15, 155], [16, 17, 18, 188]])

