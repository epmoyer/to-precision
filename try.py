import math

__author__ = 'William Rusnack github.com/BebeSparkelSparkel linkedin.com/in/williamrusnack williamrusnack@gmail.com'


def std_notation(value, precision):
  '''
  standard notation (US version)
  ref: http://www.mathsisfun.com/definitions/standard-notation.html

  returns a string of value with the proper precision

  ex:
    std_notation(5, 2) => 5.0
    std_notation(5.36, 2) => 5.4
    std_notation(5360, 2) => 5400
    std_notation(0.05363, 3) => 0.0536

    created by William Rusnack
      github.com/BebeSparkelSparkel
      linkedin.com/in/williamrusnack/
      williamrusnack@gmail.com
  '''
  sig_digits, power, is_neg = _number_profile(value, precision)

  return ('-' if is_neg else '') + _place_dot(sig_digits, power)


def sci_notation(value, precision, filler):
  '''
  scientific notation
  ref: https://www.mathsisfun.com/numbers/scientific-notation.html

  returns a string of value with the proper precision and 10s exponent
  filler is placed between the decimal value and 10s exponent

  ex:
    sci_notation(123, 1, 'E') => 1E2
    sci_notation(123, 3, 'E') => 1.23E2
    sci_notation(.126, 2, 'E') => 1.3E-1

    created by William Rusnack
      github.com/BebeSparkelSparkel
      linkedin.com/in/williamrusnack/
      williamrusnack@gmail.com
  '''
  is_neg, sig_digits, dot_power, ten_power = _sci_notation(value, precision)

  return ('-' if is_neg else '') + _place_dot(sig_digits, dot_power) + filler + str(ten_power)


def eng_notation(value, precision, filler):
  '''
  engineering notation
  ref: http://www.mathsisfun.com/definitions/engineering-notation.html

  returns a string of value with the proper precision and 10s exponent that is divisable by 3
  filler is placed between the decimal value and 10s exponent

  created by William Rusnack
    github.com/BebeSparkelSparkel
    linkedin.com/in/williamrusnack/
    williamrusnack@gmail.com
  '''
  is_neg, sig_digits, sci_dot, sci_power = _sci_notation(value, precision)

  eng_power = 3 * math.floor(sci_power / 3)
  eng_dot = sci_dot + sci_power - eng_power

  return ('-' if is_neg else '') + _place_dot(sig_digits, eng_dot) + filler + str(eng_power)


def _sci_notation(value, precision):
  '''
  returns the properties for to construct a scientific notation number
  used in sci_notation and eng_notation

  created by William Rusnack
    github.com/BebeSparkelSparkel
    linkedin.com/in/williamrusnack/
    williamrusnack@gmail.com
  '''
  sig_digits, power, is_neg = _number_profile(value, precision)

  dot_power = -(precision - 1)
  ten_power = power + precision - 1

  return is_neg, sig_digits, dot_power, ten_power


def _place_dot(digits, power):
  '''
  places the dot in the correct spot in the digits
  if the dot is outside the range of the digits zeros will be added

  ex:
    _place_dot(123, 2) => 12300
    _place_dot(123, -2) => 1.23
    _place_dot(123, 3) => 0.123
    _place_dot(123, 5) => 0.00123

    created by William Rusnack
      github.com/BebeSparkelSparkel
      linkedin.com/in/williamrusnack/
      williamrusnack@gmail.com
  '''
  if power > 0:
    out = digits + '0' * power

  elif power < 0:
    power = abs(power)
    precision = len(digits)

    if power < precision:
      out = digits[:-power] + '.' + digits[-power:]

    else:
      out = '0.' + '0' * (power - precision) + digits

  else:
    out = digits + ('.' if digits[-1] == '0' else '')

  return out


def _number_profile(value, precision):
  '''
  returns:
    string of significant digits
    10s exponent to get the dot to the proper location in the significant digits
    bool that's true if value is less than zero else false

    created by William Rusnack
      github.com/BebeSparkelSparkel
      linkedin.com/in/williamrusnack/
      williamrusnack@gmail.com
  '''
  if value == 0:
    sig_digits = '0' * precision
    power = -(1 - precision)
    is_neg = False

  else:
    if value < 0:
      value = abs(value)
      is_neg = True
    else:
      is_neg = False

    power = -1 * math.floor(math.log10(value)) + precision - 1
    sig_digits = str(round(abs(value) * 10**power))

  return sig_digits, -power, is_neg


import unittest


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

