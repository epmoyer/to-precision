#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
   
from to_precision import to_precision, _number_profile, _sci_notation

def main():
    """ Main

    - Displays a table containing example conversions.
    - Creates a (candidate) JSON file containing test
      vectors.  Every conversion appearing in the table
      becomes a test vector. The test vectors are
      used by the associated pytest module for validation.
    """
    parser = argparse.ArgumentParser(description='Demonstrate to-precision library.')
    parser.add_argument("-p", "--profile", help="Show _number_profile() data",
                    action="store_true")
    parser.add_argument("-l", "--legacy", help="Use legacy options only",
                    action="store_true")
    parser.add_argument("-c", "--compare", help="Compare all results to std mode",
                    action="store_true")
    args = parser.parse_args()

    test_vectors = []

    # Build test values: 0.0, 10.0, 100.0
    test_values = [0.0, 10.0, 100.0]

    # Build test values: 1.0 ... 123456789.0
    test_value_strings = []
    for i in range(2, 11):
        test_value_strings.append(''.join([str(j) for j in range(1, i)]))
    test_values += [float(s) for s in test_value_strings]

    # Build test values: 1.2 ... 1.23456789
    test_value_strings = []
    for i in range(3, 11):
        test_value_strings.append('1.' + ''.join([str(j) for j in range(2, i)]))
    test_values += [float(s) for s in test_value_strings]

    # Build test values: 0.0000000009 ... 0.0123456789
    test_value_strings = []
    for i in range(9, 0, -1):
        end_digits = ''.join([str(j) for j in range(i, 10)])
        test_value_strings.append('0.' + '0' * (9-len(end_digits)) + end_digits)
    test_values += [float(s) for s in test_value_strings]

    # Build test values: Negative values
    test_values += [-n for n in test_values if n != 0]

    precisions = list(range(1, 6))
    headers = ['value'] + ['precision={}'.format(x) for x in precisions] + ['Additional Options']

    option_cases = [
        {},
        {'notation': 'std'},
        {'notation': 'eng'},
        {'notation': 'sci'},
    ]
    if not args.legacy:
        option_cases += [
            {'notation': 'std', 'strip_zeros': True},
            {'notation': 'sci', 'strip_zeros': True},
            {'notation': 'std', 'preserve': True},
            {'auto_limit': 5},
        ]   

    text_grid = TextGrid(headers)
    for options_dict in option_cases:
        for test_value in test_values:
            grid_row = [format_float(test_value)]
            for precision in precisions:
                result_string = to_precision(test_value, precision, **options_dict)
                if args.profile:
                    sig_digits, power, is_neg = _number_profile(test_value, precision)
                    is_neg, sig_digits, dot_power, ten_power = _sci_notation(test_value, precision)
                    grid_row.append('{} {} p:{} dp:{} tp:{}'.format(
                        '-' if is_neg else '+',
                        sig_digits, 
                        power,
                        dot_power,
                        ten_power
                        ))
                else:
                    prefix = ''
                    if args.compare:
                        compare_string = to_precision(test_value, precision, 'std')
                        prefix = '* ' if compare_string != result_string else '  '
                            
                    grid_row.append(prefix + result_string)

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
            grid_row.append(options_to_str(options_dict))
            text_grid.add_row(grid_row)
        text_grid.add_blank_row()
    print(text_grid)

    filename = 'candidate_test_vectors.json'
    with open(filename, 'w') as text_file:
        text_file.write(json.dumps(test_vectors, indent=4, separators=(',', ': ')))

    print('Wrote {} test vectors to "{}".'.format(len(test_vectors), filename))

class TextGrid():
    """Renders a multi-column grid of text cells
    """

    def __init__(self, headers):
        """Initialize

        Args:
            headers: A list of header strings
        """
        self.headers = headers
        self.rows = []
        self.cell_widths = []
        self.column_gap = 2

    def add_row(self, row):
        """Add a row to the table

        Args: 
            row: A list of strings (length must match header row)
        """
        self.rows.append(row)

    def add_blank_row(self):
        """Add a blank row to the table
        """
        self.add_row([' '] * len(self.headers))

    def render_row(self, row):
        """Returns the row as a properly formatted string

        Args: 
            row: A list of strings (length must match header row)
        """
        text = ''
        for cell_width, cell_text in zip(self.cell_widths, row):
            text += cell_text + ' ' * (cell_width - len(cell_text) + self.column_gap)
        return text + '\n'

    def render_divider(self):
        """Returns a formatted string containing column dividers
        """
        text = ''
        for cell_width in self.cell_widths:
            text += '-' * cell_width + ' ' * self.column_gap
        return text + '\n'

    def __repr__(self):
        """Returns the formatted table
        """
        self.cell_widths = [len(s) for s in self.headers]
        for row in self.rows:
            for i, cell_text in enumerate(row):
                self.cell_widths[i] = max(self.cell_widths[i], len(cell_text))

        text = self.render_row(self.headers)
        text += self.render_divider()
        for row in self.rows:
            text += self.render_row(row) 

        return text

def format_float(value):
    """Returns float as formatted sting with up to 10 decimal digits and stripped zeros"""
    out_str = '{:0.10f}'.format(value)
    out_str = out_str.rstrip('0')
    if out_str.endswith('.'):
        return out_str[:-1]
    return out_str

def options_to_str(options_dict):
    """Returns options dict as a string in standard Python call syntax

    {'this': 1} --> 'this=1'
    {'this': 1, 'that': 2} --> 'this=1, that=2'
    """
    if not options_dict:
        return ''
    options = [key + '=' + str(value) for key, value in options_dict.items()]
    return ', '.join(options)

if __name__ == '__main__':
    main()
