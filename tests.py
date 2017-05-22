import unittest
from to_precision import to_precision as tp

class TestToPrecision(unittest.TestCase):
  def test_standard(self):
    self.assertEqual(tp(0, 1), '0')
    self.assertEqual(tp(0, 3), '0.00')

    self.assertEqual(tp(1, 1), '1')
    self.assertEqual(tp(1, 3), '1.00')
    self.assertEqual(tp(1.1, 1), '1')
    self.assertEqual(tp(1.1, 2), '1.1')
    self.assertEqual(tp(1.11, 2), '1.1')

    self.assertEqual(tp(.001, 1), '1e-3')
    self.assertEqual(tp(.0011, 2), '1.1e-3')
    self.assertEqual(tp(10e-6, 2), '1.0e-5')

  # def test_no_scientific_notation(self):




if __name__ == '__main__':
  unittest.main()