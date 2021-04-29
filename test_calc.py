#initialize calc_test.py

import calc
import unittest

class testCaseCalc(unittest.TestCase):
	def test_calc():
		result1 = calc.add(5,4)
		self.assertEqual(result1, 9)
		result2 = calc.subtract(5,4)
		self.assertEqual(result2,1)
		result3 = calc.multiply(5,4)
		self.assertEqual(result3, 20)
		result4 = calc.divide(5,4)
		self.assertEqual(result4,1)
	

if __name__ == "__main__":
	unittest.main()
