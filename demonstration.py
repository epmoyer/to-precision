#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import math

from tabulate import tabulate
   
from to_precision import to_precision, _number_profile, _sci_notation

def main():
    """ Main

    - Displays a table containing example conversions.
    - Creates a (candidate) JSON file containing test
      vectors.  Every conversion appearing in the table
      becomes a test vector. The test vectors are
      used by the associated test module for validation.
    """

    # Build test values
    test_values = [0.0, 1.0, 10.0, 100.0]
    seed = [int(123456789. / 10**x) for x in range(7,-1,-1)]
    test_values += [float(x) for x in seed]
    test_values += [float(x) / 10**int(math.log10(x))  for x in seed]
    test_values += [float(x) / 10**9  for x in seed]
    test_values += [-n for n in test_values if n != 0] # Negatives

    option_cases = [
        {},
        {'notation': 'std'},
        {'notation': 'eng'},
        {'notation': 'sci'},
        {'notation': 'std', 'strip_zeros': True},
        {'notation': 'sci', 'strip_zeros': True},
        {'notation': 'std', 'preserve_integer': True},
        {'auto_limit': 5},
    ]  

    test_vectors = []
    precisions = list(range(1, 6))
    table = [['value'] + ['precision={}'.format(x) for x in precisions] + ['Additional Options']]

    for options_dict in option_cases:
        for test_value in test_values:
            table_row = ['{:0.10f}'.format(test_value).rstrip('0').rstrip('.')]
            for precision in precisions:
                result_string = to_precision(test_value, precision, **options_dict)
                table_row.append(result_string)

                # Build test vector
                input_parameters = {
                    'value': test_value,
                    'precision': precision
                }
                input_parameters.update(options_dict)
                test_vectors.append(
                    {
                        'input_parameters': input_parameters,
                        'expected_output': result_string,
                    }
                )
            table_row.append(
                ', '.join([key + '=' + str(value) for key, value in options_dict.items()]))
            table.append(table_row)
        table.append(['']) # Blank row
    print(tabulate(table, headers="firstrow", disable_numparse=True))

    filename = 'candidate_test_vectors.json'
    with open(filename, 'w') as text_file:
        text_file.write(json.dumps(test_vectors, indent=4, separators=(',', ': ')))

    print('Wrote {} test vectors to "{}".'.format(len(test_vectors), filename))

if __name__ == '__main__':
    main()
