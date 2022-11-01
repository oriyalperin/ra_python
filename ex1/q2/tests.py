import unittest
from q2 import breadth_first_search


class MyTestCase(unittest.TestCase):
    def test_friends(self):
        friends = {"yonatan": ["oriya", "shmuel", "yizhak", "shraga"],
                   "oriya": ["noa", "orian", "yonatan", "yossi"],
                   "yizhak": ["noa", "yonatan", "shmuel", "shraga"],
                   "noa": ["orian", "oriya", "shmuel", "yossi", "shraga", "yizhak"],
                   "shraga": ["noa", "yonatan", "shmuel", "yizhak", "tzabari"],
                   "yossi": ["oriya", "orian", "noa"],
                   "tzabari": ["shraga"],
                   "orian": ["oriya", "noa", "sapir", 'yossi'],
                   "shmuel": ["noa", "shraga", "yizhak", "yonatan"],
                   "sapir": ["orian"],
                   "bar": ["linoy"],
                   "linoy": ["bar"],
                   "eli": []}

        f = lambda item: friends[item]
        path = ['sapir', 'orian', 'noa', 'shraga', 'tzabari']
        self.assertEqual(path, breadth_first_search("sapir", 'tzabari', f))
        path = ['orian', 'oriya', 'yonatan']
        self.assertEqual(path, breadth_first_search('orian', 'yonatan', f))
        path = ['yossi', 'noa', 'yizhak']
        self.assertEqual(path, breadth_first_search("yossi", 'yizhak', f))
        path = ['shmuel', 'shraga']
        self.assertEqual(path, breadth_first_search('shmuel', 'shraga', f))
        path = ['noa']
        self.assertEqual(path, breadth_first_search('noa', 'noa', f))
        path = []
        self.assertEqual(path, breadth_first_search('sapir', 'bar', f))
        path = []
        self.assertEqual(path, breadth_first_search('eli', 'bar', f))

    def test_two_dim(self):
        def four_neighbors_x(node: tuple):
            x, y = node[0], node[1]
            return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        path = [(1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5)]
        self.assertEqual(path, breadth_first_search((1, 2), (4, 5), four_neighbors_x))

        path = [(9, 6), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10)]
        self.assertEqual(path, breadth_first_search((9, 6), (8, 10), four_neighbors_x))

        path = [(1,1)]
        self.assertEqual(path, breadth_first_search((1,1), (1, 1), four_neighbors_x))

        def four_neighbors_y(node: tuple):
            x, y = node[0], node[1]
            return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        path = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5)]
        self.assertEqual(path, breadth_first_search((1, 2), (4, 5), four_neighbors_y))


if __name__ == '__main__':
    unittest.main()
