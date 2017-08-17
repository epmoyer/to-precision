__author__ = 'William Rusnack github.com/BebeSparkelSparkel linkedin.com/in/williamrusnack williamrusnack@gmail.com'

import unittest
from to_precision import to_precision, std_notation, sci_notation, eng_notation, _sci_notation, _place_dot, _number_profile

class TestToPrecision(unittest.TestCase):
  def test_auto(self):
    # within limit
    self.assertEqual(
        to_precision(-552, 2, notation='auto', filler='e'),
        '-550'
      )

    self.assertEqual(
        to_precision(552, 2, notation='auto', filler='e'),
        '550'
      )

    # over limit
    self.assertEqual(
        to_precision(1001, 2, notation='auto', filler='e'),
        '1.0e3'
      )

    self.assertEqual(
        to_precision(-1001, 2, notation='auto', filler='e'),
        '-1.0e3'
      )

    self.assertEqual(
        to_precision(0.0009, 2, notation='auto', filler='e'),
        '9.0e-4'
      )

    self.assertEqual(
        to_precision(-0.0009, 2, notation='auto', filler='e'),
        '-9.0e-4'
      )

  def test_multi(self):
    self.assertEqual(
        to_precision(500, 2, notation='std', filler='e'),
        '500'
      )

    self.assertEqual(
        to_precision(500, 2, notation='sci', filler='e'),
        '5.0e2'
      )

    self.assertEqual(
        to_precision(1100, 2, notation='eng', filler='e'),
        '1.1e3'
      )


class TestEngNotation(unittest.TestCase):
  def test_multi(self):
    self.assertEqual(eng_notation(1, 1, 'e'), '1e0')
    self.assertEqual(eng_notation(1, 2, 'e'), '1.0e0')
    self.assertEqual(eng_notation(10, 1, 'e'), '10e0')

    self.assertEqual(eng_notation(123, 1, 'e'), '100e0')
    self.assertEqual(eng_notation(123, 2, 'e'), '120e0')  # round down
    self.assertEqual(eng_notation(-1260, 2, 'e'), '-1.3e3')  # round up

    self.assertEqual(eng_notation(.123, 1, 'e'), '100e-3')
    self.assertEqual(eng_notation(-.0123, 2, 'e'), '-12e-3')
    self.assertEqual(eng_notation(-.0123, 3, 'e'), '-12.3e-3')
    self.assertEqual(eng_notation(.126, 2, 'e'), '130e-3')

    self.assertEqual(eng_notation(-123, 4, 'e'), '-123.0e0')  # round down

    # sig zero
    self.assertEqual(eng_notation(10, 2, 'e'), '10.e0')


class TestStdNotation(unittest.TestCase):
  def test_multi(self):
    self.assertEqual(std_notation(123, 1), '100')
    self.assertEqual(std_notation(123, 2), '120')  # round down
    self.assertEqual(std_notation(126, 2), '130')  # round up
    self.assertEqual(std_notation(1260, 2), '1300')  # round up

    self.assertEqual(std_notation(.123, 1), '0.1')
    self.assertEqual(std_notation(.0123, 2), '0.012')
    self.assertEqual(std_notation(.126, 2), '0.13')
    self.assertEqual(std_notation(.126, 4), '0.1260')

    self.assertEqual(std_notation(123, 3), '123')
    self.assertEqual(std_notation(123, 4), '123.0')  # round down

    # sig zero
    self.assertEqual(std_notation(10, 2), '10.')



class TestSciNotation(unittest.TestCase):
  def test_multi(self):
    self.assertEqual(sci_notation(1, 1, 'e'), '1e0')
    self.assertEqual(sci_notation(1, 2, 'e'), '1.0e0')
    self.assertEqual(sci_notation(10, 1, 'e'), '1e1')

    self.assertEqual(sci_notation(123, 1, 'e'), '1e2')
    self.assertEqual(sci_notation(123, 2, 'e'), '1.2e2')  # round down
    self.assertEqual(sci_notation(-126, 2, 'e'), '-1.3e2')  # round up

    self.assertEqual(sci_notation(.123, 1, 'e'), '1e-1')
    self.assertEqual(sci_notation(-.0123, 2, 'e'), '-1.2e-2')
    self.assertEqual(sci_notation(.126, 2, 'e'), '1.3e-1')

    self.assertEqual(sci_notation(123, 3, 'e'), '1.23e2')
    self.assertEqual(sci_notation(-123, 4, 'e'), '-1.230e2')  # round down


class TestPlaceDot(unittest.TestCase):
  def test_all(self):
    self.assertEqual(_place_dot('123', 0), '123')
    self.assertEqual(_place_dot('120', 0), '120.')

    self.assertEqual(_place_dot('123', 2), '12300')

    self.assertEqual(_place_dot('123', -2), '1.23')
    self.assertEqual(_place_dot('123', -3), '0.123')
    self.assertEqual(_place_dot('123', -5), '0.00123')

class TestNumberProfile(unittest.TestCase):
  def test_positive(self):
    self.assertEqual(
        _number_profile(123, 2),
        ('12', 1, False)
      )

    self.assertEqual(
        _number_profile(123, 3),
        ('123', 0, False)
      )

  def test_negative(self):
    self.assertEqual(
        _number_profile(-123, 3),
        ('123', 0, True)
      )

    self.assertEqual(
        _number_profile(-123, 1),
        ('1', 2, True)
      )

    self.assertEqual(
        _number_profile(-12.3, 2),
        ('12', 0, True)
      )

    self.assertEqual(
        _number_profile(-12.3, 3),
        ('123', -1, True)
      )

    self.assertEqual(
        _number_profile(-.123, 3),
        ('123', -3, True)
      )

    self.assertEqual(
        _number_profile(-.123, 2),
        ('12', -2, True)
      )

  def test_zeros(self):
    self.assertEqual(
        _number_profile(0, 1),
        ('0', 0, False)
      )

    self.assertEqual(
        _number_profile(0, 3),
        ('000', -2, False)
      )

  def test_round_up(self):
    self.assertEqual(
        _number_profile(-.126, 2),
        ('13', -2, True)
      )


if __name__ == '__main__':
  unittest.main()
