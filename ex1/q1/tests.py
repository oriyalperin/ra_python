import unittest
from q1 import safe_call


class MyTestCase(unittest.TestCase):
    def test_fun(self):
        def fun(x: int, y: str, z: dict):
            z[x] = y
            return z

        self.assertRaises(TypeError, safe_call, f=fun, x=5, y="a", z=[])
        self.assertRaises(TypeError, safe_call, f=fun, x=5, y=5, z=[])
        self.assertRaises(TypeError, safe_call, f=fun, x='a', y=5, z={})
        self.assertRaises(TypeError, safe_call, f=fun, x=[], y=[], z={})
        self.assertEqual(safe_call(f=fun, x=3, y='a', z={}), {3: 'a'})

    def test_pow(self):
        def pow(x: int, p: float):
            return x ** p

        self.assertRaises(TypeError, safe_call, f=pow, x=2.5, p=1)
        self.assertEqual(safe_call(f=pow, x=9, p=0.5), 3)

    def test_chain(self):
        def chain(str1: str, str2: str):
            return str1 + " " + str2

        self.assertRaises(TypeError, safe_call, f=chain, str1="number", str2=1)
        self.assertEqual(safe_call(f=chain, str1="Im", str2="tiered"), "Im tiered")


if __name__ == '__main__':
    unittest.main()
