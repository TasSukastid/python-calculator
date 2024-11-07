import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:


    def test_add(self):
        self.assertEqual(self.calc.add(50,6),56)

    def test_add(self):
        self.assertEqual(self.calc.add(10,20),30)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(-10,-2),-12)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3,50),-47)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-5,2),-10)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10,-10),-100)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,10),1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,0),"undefined")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2,10),2)

if __name__ == '__main__':
    unittest.main()