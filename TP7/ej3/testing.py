import random
import unittest
from ej3.test import *

class MyTest(unittest.TestCase):

    def test_1(self):
        num = list(range(0, 101))
        random.shuffle(num)
        num.remove(3)
        self.assertEquals(missing_no(num), [3])

    def test_2(self):
        num = list(range(0, 101))
        random.shuffle(num)
        num.remove(100)
        self.assertEquals(missing_no(num), [100])