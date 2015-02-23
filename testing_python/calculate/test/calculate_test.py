from nose.tools import *
import unittest
from calculate.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
      self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        print 'Hello'
        self.assertEqual(4,self.calc.add(2,2))
        self.assertAlmostEquals(1,1)

    def test_add_method_raises_typeerror_if_not_ints(self):
      self.assertRaises(TypeError,self.calc.add,"Hello"," World")

    def test_assert_raises(self):
       with self.assertRaises(AttributeError):
          [].get

if __name__=='__main__':
  unittest.main()
