# to_precision
Formatting floating point numbers to standard, scientific, or engineering notation with a specified number of significant digits.

created by **William Rusnack**
github.com/BebeSparkelSparkel
linkedin.com/in/williamrusnack/
williamrusnack@gmail.com
and **Randle Taylor**
github.com/randlet

## Install

    pip install git+https://github.com/BebeSparkelSparkel/to-precision.git

### to_precision
to_precision.**to_precision**(value, precision, notation='auto')
converts a value to the specified notation and precision
value - any type that can be converted to a float
predision - integer that is greater than zero
notation - string
* 'auto' - selects standard notation when 0.001 < abs(value) < 1000 else returns scientific notation
* 'sci' or 'scientific' - returns scientific notation. https://www.mathsisfun.com/numbers/scientific-notation.html
* 'eng' or 'engineering' - returns engineering notation. http://www.mathsisfun.com/definitions/engineering-notation.html
* 'std' or 'standard' - returns standard notation. http://www.mathsisfun.com/definitions/standard-notation.html

### standard notation
to_precision.**std_notation**(value, precision)
standard notation (US version). http://www.mathsisfun.com/definitions/standard-notation.html

returns a string of value with the proper precision

ex:

    >>> std_notation(5, 2)
    5.0
    >>> std_notation(5.36, 2)
    5.4
    >>> std_notation(5360, 2)
    5400
    >>> std_notation(0.05363, 3)
    0.0536

# scientific notation
to_precision.**sci_notation**(value, precision, filler)
scientific notation. https://www.mathsisfun.com/numbers/scientific-notation.html

returns a string of value with the proper precision and 10s exponent
filler is placed between the decimal value and 10s exponent

ex:

    >>> sci_notation(123, 1, 'E')
    1E2
    >>> sci_notation(123, 3, 'E')
    1.23E2
    >>> sci_notation(.126, 2, 'E')
    1.3E-1

### engineering notation
to_precision.**eng_notation**(value, precision, filler)
engineering notation. http://www.mathsisfun.com/definitions/engineering-notation.html

returns a string of value with the proper precision and 10s exponent that is divisable by 3
filler is placed between the decimal value and 10s exponent

ex:

    >>> eng_notation(123, 1, 'E')
    100E0
    >>> eng_notation(1230, 3, 'E')
    1.23E3
    >>> eng_notation(.126, 2, 'E')
    120E-3
