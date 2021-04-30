#initialize calc_test.py

import calc
import unittest

class testCaseCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(4,5),9)
		self.assertEqual(calc.add(2,5),6)
	def test_subtract(self):
		self.assertEqual(calc.subtract(4,5),-1)
		self.assertEqual(calc.subtract(5,4),-1)
	def test_multiply(self):
		self.assertEqual(calc.multiply(4,5),20)
		self.assertEqual(calc.multiple(3,5),20)
	def test_divide(self):
		self.assertEqual(calc.divide(4,5),0)
		self.assertEqual(calc.divide(4,1),3)

#if __name__ == "__main__":
#	unittest.main()
