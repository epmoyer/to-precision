#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from tabulate import tabulate
from to_precision import to_precision

def main():
    """ Displays a table containing example conversions for to_precision()
    """

    # Build test values
    test_values = [0.0, 1.0, 10.0, 100.0, -1.0]
    seed = [int(123456789. / 10**x) for x in range(7, -1, -1)]
    test_values += [float(x) for x in seed]
    test_values += [float(x) / 10**int(math.log10(x))  for x in seed]
    test_values += [float(x) / 10**9  for x in seed]

    option_cases = [
        ('Default (Auto Notation)', {}),
        ('Standard Notation', {'notation': 'std'}),
        ('Engineering Notation', {'notation': 'eng'}),
        ('Scientific Notation', {'notation': 'sci'}),
        ('Standard Notation with zero stripping', {'notation': 'std', 'strip_zeros': True}),
        ('Scientific Notation with zero stripping', {'notation': 'sci', 'strip_zeros': True}),
        ('Standard Notation with integer preservation', {'notation': 'std', 'preserve_integer': True}),
        ('Auto Notation with exponent limit of 5', {'auto_limit': 5}),
    ]

    precisions = list(range(1, 6))
    
    for options_description, options_dict in option_cases:
        print(options_description + ':')
        options_string = ', '.join(
            ['value', 'precision'] +
            [key + '=' + value.__repr__() for key, value in options_dict.items()])
        print('    to_precision({})\n'.format(options_string))

        table = [['value'] + ['precision={}'.format(x) for x in precisions]]
        for test_value in test_values:
            table_row = ['{:0.10f}'.format(test_value).rstrip('0').rstrip('.')]
            for precision in precisions:
                result_string = to_precision(test_value, precision, **options_dict)
                table_row.append(result_string)
            table.append(table_row)
        table_text = tabulate(table, headers="firstrow", disable_numparse=True)
        print('\n'.join('    ' + ln for ln in table_text.splitlines()) + '\n')

if __name__ == '__main__':
    main()
