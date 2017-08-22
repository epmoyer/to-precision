__author__ = 'William Rusnack github.com/BebeSparkelSparkel linkedin.com/in/williamrusnack williamrusnack@gmail.com'

import math

def to_precision(
  value, 
  precision,
  notation='auto',
  filler='e',
  auto_limit=3,
  strip_zeros=False,
  preserve_integer=False):
  '''
  converts a value to the specified notation and precision
  value - any type that can be converted to a float
  precision - integer that is greater than zero
  notation - string
    'auto' - selects standard notation when abs(power) < auto_limit else 
      returns scientific notation.
    'sci' or 'scientific' - returns scientific notation
      ref: https://www.mathsisfun.com/numbers/scientific-notation.html
    'eng' or 'engineering' - returns engineering notation
      ref: http://www.mathsisfun.com/definitions/engineering-notation.html
    'std' or 'standard' - returns standard notation
      ref: http://www.mathsisfun.com/definitions/standard-notation.html
  filler - is placed between the decimal value and 10s exponent
  auto_limit - integer. When abs(power) exceeds this limit, 'auto'
    mode will return scientific notation.
  strip_zeros - if true, trailing decimal zeros will be removed.
  preserve_integer - if true, 'std' will preserve all digits when returning
    values that have no decimal component.
  '''
  is_neg, sig_digits, dot_power, ten_power = _sci_notation(value, precision)
  sign = ('-' if is_neg else '')

  if notation == 'auto':
    if abs(ten_power) < auto_limit:
      notation = 'std'
    else:
      notation = 'sci'

  if notation in ('sci', 'scientific'):
    result = sign + _place_dot(sig_digits, dot_power, strip_zeros) + filler + str(ten_power)

  elif notation in ('eng', 'engineering'):
    eng_power = int(3 * math.floor(ten_power / 3))
    eng_dot = dot_power + ten_power - eng_power
    result = sign + _place_dot(sig_digits, eng_dot, strip_zeros) + filler + str(eng_power)

  elif notation in ('std', 'standard'):
    sig_digits, power, is_neg = _number_profile(value, precision)
    result = sign + _place_dot(sig_digits, power, strip_zeros)
    if preserve_integer and not '.' in result:
      # Result was an integer, preserve all digits
      result = '{:0.0f}'.format(value)

  else:
    raise ValueError('Unknown notation: ' + str(notation))

  return result

def auto_notation(value, precision):
  '''
  TODO: Needs comment block
  Defaults to equivalent of auto_limit=3
  '''
  is_neg, sig_digits, dot_power, ten_power = _sci_notation(value, precision)
  if abs(ten_power) < 3:
    return std_notation(value, precision)
  else:
    return sci_notation(value, precision)

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


def sci_notation(value, precision):
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

  return ('-' if is_neg else '') + _place_dot(sig_digits, dot_power) + 'e' + str(ten_power)


def eng_notation(value, precision):
  '''
  engineering notation
  ref: http://www.mathsisfun.com/definitions/engineering-notation.html

  returns a string of value with the proper precision and 10s exponent that is divisable by 3
  filler is placed between the decimal value and 10s exponent

  ex:
    sci_notation(123, 1, 'E') => 100E0
    sci_notation(1230, 3, 'E') => 1.23E3
    sci_notation(.126, 2, 'E') => 120E-3

  created by William Rusnack
    github.com/BebeSparkelSparkel
    linkedin.com/in/williamrusnack/
    williamrusnack@gmail.com
  '''
  is_neg, sig_digits, sci_dot, sci_power = _sci_notation(value, precision)

  eng_power = int(3 * math.floor(sci_power / 3))
  eng_dot = sci_dot + sci_power - eng_power

  return ('-' if is_neg else '') + _place_dot(sig_digits, eng_dot) + 'e' + str(eng_power)


def _sci_notation(value, precision):
  '''
  returns the properties for to construct a scientific notation number
  used in sci_notation and eng_notation

  created by William Rusnack
    github.com/BebeSparkelSparkel
    linkedin.com/in/williamrusnack/
    williamrusnack@gmail.com
  '''
  value = float(value)
  sig_digits, power, is_neg = _number_profile(value, precision)

  dot_power = -(precision - 1)
  ten_power = power + precision - 1

  return is_neg, sig_digits, dot_power, ten_power


def _place_dot(digits, power, strip_zeros=False):
  '''
  places the dot in the correct spot in the digits
  if the dot is outside the range of the digits zeros will be added
  if strip_zeros is set, trailing decimal zeros will be removed

  ex:
    _place_dot('123',   2, False) => '12300'
    _place_dot('123',  -2, False) => '1.23'
    _place_dot('123',   3, False) => '0.123'
    _place_dot('123',   5, False) => '0.00123'
    _place_dot('120',   0, False) => '120.'
    _place_dot('1200', -2, False) => '12.00'
    _place_dot('1200', -2, True ) => '12'
    _place_dot('1200', -1, False) => '120.0'
    _place_dot('1200', -1, True ) => '120'

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
    out = digits + ('.' if digits[-1] == '0' and len(digits) > 1 else '')

  if strip_zeros and '.' in out:
    out = out.rstrip('0').rstrip('.')

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
  value = float(value)
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
    sig_digits = str(int(round(abs(value) * 10.0**power)))

  return sig_digits, int(-power), is_neg

