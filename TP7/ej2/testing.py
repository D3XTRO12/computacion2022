import unittest
from ej2.test import *

class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(validate_pin("12345"), False)

    def test_2(self):
        self.assertEquals(validate_pin("9725"), True)

    def test_3(self):
        self.assertEquals(validate_pin("a345"), False)

