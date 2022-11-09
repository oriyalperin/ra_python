import unittest
from q2 import last_call


class MyTestCase(unittest.TestCase):

    def test_primitive_objects(self):
        @last_call
        def sqr(x: int):
            return x ** 2

        @last_call
        def power_3(x: int):
            return x ** 3

        self.assertEqual(1, sqr(1))
        self.assertEqual(1, sqr(2))
        self.assertIsNone(sqr(1))

    def test_objects(self):
        class Person:
            def __init__(self, name: str, age: float):
                self.name = name
                self.age = age

            @last_call
            def get_name(self):
                return self.name

            @last_call
            def get_age(self):
                return self.age

        nevo = Person("nevo avraham", 0.4)
        benaya = Person("benaya eliyhu", 0.3)
        oriya = Person("oriya", 23)
        yoni = Person("yonatan", 23)
        self.assertEqual("nevo avraham", nevo.get_name())
        self.assertIsNone(nevo.get_name())
        self.assertEqual(0.3, benaya.get_age())
        self.assertEqual(oriya.get_age(),yoni.get_age())
        self.assertEqual("yonatan", yoni.get_name())
        self.assertIsNone(yoni.get_age())


if __name__ == '__main__':
    unittest.main()
