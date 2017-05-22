import math

# def sci_not(value, filler):


def to_precision(value, precision, notation='auto'):
    '''
    returns a string representation of value formatted with a precision of precision

    notation
        auto - automatically chooses what type of notation to use
        std - standard notation ex(1, 0.0005, 5000) ref: http://www.mathsisfun.com/definitions/standard-notation.html
        E - E notation. ref: http://encyclopedia2.thefreedictionary.com/E+notation
            like scientific notation but with E
        e - e notation. ref: http://encyclopedia2.thefreedictionary.com/E+notation
            like scientific notation but with e

    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    '''

    value = float(value)

    if notation == 'auto':
        if value == 0:
            precision -= 1
            out = '0'
            if precision:
                out += '.' + '0' * precision

        else:
            out = ''

            if value < 0:
                out += '-'
                value *= -1

            e = int(math.log10(value))

            tens = math.pow(10, e - precision + 1)
            n = math.floor(value / tens)

            if n < math.pow(10, precision - 1):
                e = e -1
                tens = math.pow(10, e - precision+1)
                n = math.floor(value / tens)

            if abs((n + 1.) * tens - value) <= abs(n * tens -value):
                n = n + 1

            if n >= math.pow(10,precision):
                n = n / 10.
                e = e + 1


            m = '%.*g' % (precision, n)

            if e < -2 or e >= precision:
                out += m[0]
                if precision > 1:
                    out += '.'
                    out += m[1:precision]
                out += 'e'
                if e > 0:
                    out += '+'
                out += str(e)
            elif e == (precision -1):
                out += m
            elif e >= 0:
                out += m[:e+1]
                if e+1 < len(m):
                    out += '.'
                    out += m[e+1:]
            else:
                out += '0.'
                out += ['0']*-(e+1)
                out += m

        return out
