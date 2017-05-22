import math


def std_notation(value, precision):
  sig_digits, power, is_neg = number_profile(value, precision)

  return ('-' if is_neg else '') + place_dot(sig_digits, power)


def sci_notation(value, precision, filler):
  sig_digits, power, is_neg = number_profile(value, precision)

  return ('-' if is_neg else '') + place_dot(sig_digits, -(precision - 1)) + filler + str(power + precision - 1)


def _sci_notation(value, precision):
  sig_digits, power, is_neg = number_profile(value, precision)

  dot_power = -(precision - 1)
  ten_power = power + precision - 1

  return sig_digits, dot_power, ten_power


def place_dot(digits, power):
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


def number_profile(value, precision):
  '''
  returns:
    string of significant digits
    exponent of 10 to get string back to origional value
    bool that's true if value is less than zero else false
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


def eng_notation(value, precision, filler):
  sig_digits, power, is_neg = number_profile(value, precision)

  thousands = int(math.log(abs(value), 1000))
  tens = int(math.log(abs(value), 10)) % 3
  dot_power = -(precision - 1) - tens

  print()
  print(value, precision)
  print('th', thousands)
  print('t', tens)
  print('out', place_dot(sig_digits, dot_power))
  print()

  # return ('-' if is_neg else '') + place_dot(sig_digits, dot_power) + filler + str(eng_power)


import unittest


class TestEngNotation(unittest.TestCase):
  def test_multi(self):
    eng_notation(1, 1, 'e') #, '1e0')
    eng_notation(1, 2, 'e') #, '1e0')
    eng_notation(10, 1, 'e') #, '1e0')

    eng_notation(123, 1, 'e') #, '100e0')
    # eng_notation(123, 2, 'e') #, '120e0')  # round down
    # eng_notation(-1260, 2, 'e') #, '-1.3e3')  # round up

    # eng_notation(.123, 1, 'e') #, '100e-3')
    # eng_notation(-.0123, 2, 'e') #, '-12e-3')
    # eng_notation(-.0123, 3, 'e') #, '-12.3e-3')
    # eng_notation(.126, 2, 'e') #, '130e-3')

    # eng_notation(-123, 4, 'e') #, '-123.0e0')  # round down
    print()



class TestStdNotation(unittest.TestCase):
  def test_multi(self):
    self.assertEqual(std_notation(123, 1), '100')
    self.assertEqual(std_notation(123, 2), '120')  # round down
    self.assertEqual(std_notation(126, 2), '130')  # round up
    self.assertEqual(std_notation(1260, 2), '1300')  # round up

    self.assertEqual(std_notation(.123, 1), '0.1')
    self.assertEqual(std_notation(.0123, 2), '0.012')
    self.assertEqual(std_notation(.126, 2), '0.13')

    self.assertEqual(std_notation(123, 3), '123')
    self.assertEqual(std_notation(123, 4), '123.0')  # round down


class TestSciNotation(unittest.TestCase):
  def test_multi(self):
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
    self.assertEqual(place_dot('123', 0), '123')
    self.assertEqual(place_dot('120', 0), '120.')

    self.assertEqual(place_dot('123', 2), '12300')

    self.assertEqual(place_dot('123', -2), '1.23')
    self.assertEqual(place_dot('123', -3), '0.123')
    self.assertEqual(place_dot('123', -5), '0.00123')

class TestNumberProfile(unittest.TestCase):
  def test_positive(self):
    self.assertEqual(
        number_profile(123, 2),
        ('12', 1, False)
      )

    self.assertEqual(
        number_profile(123, 3),
        ('123', 0, False)
      )

  def test_negative(self):
    self.assertEqual(
        number_profile(-123, 3),
        ('123', 0, True)
      )

    self.assertEqual(
        number_profile(-123, 1),
        ('1', 2, True)
      )

    self.assertEqual(
        number_profile(-12.3, 2),
        ('12', 0, True)
      )

    self.assertEqual(
        number_profile(-12.3, 3),
        ('123', -1, True)
      )

    self.assertEqual(
        number_profile(-.123, 3),
        ('123', -3, True)
      )

    self.assertEqual(
        number_profile(-.123, 2),
        ('12', -2, True)
      )

  def test_zeros(self):
    self.assertEqual(
        number_profile(0, 1),
        ('0', 0, False)
      )

    self.assertEqual(
        number_profile(0, 3),
        ('000', -2, False)
      )

  def test_round_up(self):
    self.assertEqual(
        number_profile(-.126, 2),
        ('13', -2, True)
      )


if __name__ == '__main__':
  unittest.main()

