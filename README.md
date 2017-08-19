# to_precision
Formatting floating point numbers to standard, scientific, or engineering notation with a specified number of significant digits.

Created by **William Rusnack**
github.com/BebeSparkelSparkel
linkedin.com/in/williamrusnack/
williamrusnack@gmail.com
and **Randle Taylor**
github.com/randlet

## Install

    pip install git+https://github.com/BebeSparkelSparkel/to-precision.git

### to_precision
to_precision.**to_precision**(value, precision, notation='auto', filler='e', auto_limit=3, strip_zeros=False, preserve=False)  

Converts a value to the specified notation and precision
value - any type that can be converted to a float
precision - integer that is greater than zero
notation - string

* value
    * The number to convert
* precision
    * The digits of precision
* notation
    * 'auto' - selects standard notation when abs(power) < auto_limit else returns scientific notation.
    * 'sci' or 'scientific' - returns scientific notation. https://www.mathsisfun.com/numbers/scientific-notation.html
    * 'eng' or 'engineering' - returns engineering notation. http://www.mathsisfun.com/definitions/engineering-notation.html
    * 'std' or 'standard' - returns standard notation. http://www.mathsisfun.com/definitions/standard-notation.html
* filler
    * Text that is placed between the decimal value and 10s exponent
* auto_limit
    * Integer. When abs(power) exceeds this limit, 'auto'
    mode will return scientific notation. The default (3) will cause 'auto' mode to return scientific notation for 0.001 < abs(value) < 1000
* strip_zeros
    * If true, trailing decimal zeros will be removed.
* preserve
    * If true, 'std' will preserve all digits when returning
    values that have no decimal component.

### standard notation
to_precision.**std_notation**(value, precision, extra=None, strip_zeros=False, preserve=False)

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

### scientific notation
to_precision.**sci_notation**(value, precision, filler, strip_zeros=False, extra=None):

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

returns a string of value with the proper precision and 10s exponent that is divisible by 3
filler is placed between the decimal value and 10s exponent

ex:

    >>> eng_notation(123, 1, 'E')
    100E0
    >>> eng_notation(1230, 3, 'E')
    1.23E3
    >>> eng_notation(.126, 2, 'E')
    120E-3

## Implicit vs. Explicit precision

Consider the following data set:

    A                 B              C              D              
    ----------------  -------------  -------------  -------------  
    1.00000000000     0.98765432100  0.08700000000  0.00000000234  
    1.20000000000     1.40000000000  1.00000000000  0.00000000002  
    1234.00000000000  1.23450000000  0.02345678000  0.00000000000 

In a scientific or engineering context, one typically indicates precision *explicitly* by showing all significant digits.  This can be accomplished using `to_pecision()` with its default arguments.

Using `to_precision(x, 3)` to render the example data set yields:

    A       B      C       D         
    ------  -----  ------  --------  
    1.00    0.988  0.0870  2.34e-9   
    1.20    1.40   1.00    2.00e-11  
    1.23e3  1.23   0.0235  0.00

In a business or informal context one may wish to *implicitly* specify precision, and render results in their simplest, least cluttered form given that precision.  This can be accomplished by invoking the `strip_zeros` and `preserve` arguments.  Additionally, `auto_limit` can be used to control the threshold at which scientific notation is adopted.

Using `to_precision(x, 3, auto_limit=4, strip_zeros=True, preserve=True)` to render the example data set yields:

    A     B      C       D        
    ----  -----  ------  -------  
    1     0.988  0.087   2.34e-9  
    1.2   1.4    1       2e-11    
    1234  1.23   0.0235  0 


## Demonstration

The script `demonstration.py` exercises the various options...

    $./demonstration.py 

    value         precision=1   precision=2    precision=3     precision=4      precision=5       Additional Options              
    ------------  ------------  -------------  --------------  ---------------  ----------------  ------------------------------  
    0             0             0.0            0.00            0.000            0.0000                                            
    1             1             1.0            1.00            1.000            1.0000                                            
    12            10            12             12.0            12.00            12.000                                            
    123           100           120            123             123.0            123.00                                            
    1234          1e3           1.2e3          1.23e3          1.234e3          1.2340e3                                          
    12345         1e4           1.2e4          1.23e4          1.234e4          1.2345e4                                          
    123456        1e5           1.2e5          1.23e5          1.235e5          1.2346e5                                          
    1234567       1e6           1.2e6          1.23e6          1.235e6          1.2346e6                                          
    12345678      1e7           1.2e7          1.23e7          1.235e7          1.2346e7                                          
    123456789     1e8           1.2e8          1.23e8          1.235e8          1.2346e8                                          
    1.2           1             1.2            1.20            1.200            1.2000                                            
    1.23          1             1.2            1.23            1.230            1.2300                                            
    1.234         1             1.2            1.23            1.234            1.2340                                            
    1.2345        1             1.2            1.23            1.234            1.2345                                            
    1.23456       1             1.2            1.23            1.235            1.2346                                            
    1.234567      1             1.2            1.23            1.235            1.2346                                            
    1.2345678     1             1.2            1.23            1.235            1.2346                                            
    1.23456789    1             1.2            1.23            1.235            1.2346                                            
    0.000000009   9e-9          9.0e-9         9.00e-9         9.000e-9         9.0000e-9                                         
    0.000000089   9e-8          8.9e-8         8.90e-8         8.900e-8         8.9000e-8                                         
    0.000000789   8e-7          7.9e-7         7.89e-7         7.890e-7         7.8900e-7                                         
    0.000006789   7e-6          6.8e-6         6.79e-6         6.789e-6         6.7890e-6                                         
    0.000056789   6e-5          5.7e-5         5.68e-5         5.679e-5         5.6789e-5                                         
    0.000456789   5e-4          4.6e-4         4.57e-4         4.568e-4         4.5679e-4                                         
    0.003456789   3e-3          3.5e-3         3.46e-3         3.457e-3         3.4568e-3                                         
    0.023456789   0.02          0.023          0.0235          0.02346          0.023457                                          
    0.123456789   0.1           0.12           0.123           0.1235           0.12346                                           
    -1            -1            -1.0           -1.00           -1.000           -1.0000                                           
    -12           -10           -12            -12.0           -12.00           -12.000                                           
    -123          -100          -120           -123            -123.0           -123.00                                           
    -1234         -1e3          -1.2e3         -1.23e3         -1.234e3         -1.2340e3                                         
    -12345        -1e4          -1.2e4         -1.23e4         -1.234e4         -1.2345e4                                         
    -123456       -1e5          -1.2e5         -1.23e5         -1.235e5         -1.2346e5                                         
    -1234567      -1e6          -1.2e6         -1.23e6         -1.235e6         -1.2346e6                                         
    -12345678     -1e7          -1.2e7         -1.23e7         -1.235e7         -1.2346e7                                         
    -123456789    -1e8          -1.2e8         -1.23e8         -1.235e8         -1.2346e8                                         
    -1.2          -1            -1.2           -1.20           -1.200           -1.2000                                           
    -1.23         -1            -1.2           -1.23           -1.230           -1.2300                                           
    -1.234        -1            -1.2           -1.23           -1.234           -1.2340                                           
    -1.2345       -1            -1.2           -1.23           -1.234           -1.2345                                           
    -1.23456      -1            -1.2           -1.23           -1.235           -1.2346                                           
    -1.234567     -1            -1.2           -1.23           -1.235           -1.2346                                           
    -1.2345678    -1            -1.2           -1.23           -1.235           -1.2346                                           
    -1.23456789   -1            -1.2           -1.23           -1.235           -1.2346                                           
    -0.000000009  -9e-9         -9.0e-9        -9.00e-9        -9.000e-9        -9.0000e-9                                        
    -0.000000089  -9e-8         -8.9e-8        -8.90e-8        -8.900e-8        -8.9000e-8                                        
    -0.000000789  -8e-7         -7.9e-7        -7.89e-7        -7.890e-7        -7.8900e-7                                        
    -0.000006789  -7e-6         -6.8e-6        -6.79e-6        -6.789e-6        -6.7890e-6                                        
    -0.000056789  -6e-5         -5.7e-5        -5.68e-5        -5.679e-5        -5.6789e-5                                        
    -0.000456789  -5e-4         -4.6e-4        -4.57e-4        -4.568e-4        -4.5679e-4                                        
    -0.003456789  -3e-3         -3.5e-3        -3.46e-3        -3.457e-3        -3.4568e-3                                        
    -0.023456789  -0.02         -0.023         -0.0235         -0.02346         -0.023457                                         
    -0.123456789  -0.1          -0.12          -0.123          -0.1235          -0.12346                                          
                                                                                                                                 
    0             0             0.0            0.00            0.000            0.0000            notation=std                    
    1             1             1.0            1.00            1.000            1.0000            notation=std                    
    12            10            12             12.0            12.00            12.000            notation=std                    
    123           100           120            123             123.0            123.00            notation=std                    
    1234          1000          1200           1230            1234             1234.0            notation=std                    
    12345         10000         12000          12300           12340            12345             notation=std                    
    123456        100000        120000         123000          123500           123460            notation=std                    
    1234567       1000000       1200000        1230000         1235000          1234600           notation=std                    
    12345678      10000000      12000000       12300000        12350000         12346000          notation=std                    
    123456789     100000000     120000000      123000000       123500000        123460000         notation=std                    
    1.2           1             1.2            1.20            1.200            1.2000            notation=std                    
    1.23          1             1.2            1.23            1.230            1.2300            notation=std                    
    1.234         1             1.2            1.23            1.234            1.2340            notation=std                    
    1.2345        1             1.2            1.23            1.234            1.2345            notation=std                    
    1.23456       1             1.2            1.23            1.235            1.2346            notation=std                    
    1.234567      1             1.2            1.23            1.235            1.2346            notation=std                    
    1.2345678     1             1.2            1.23            1.235            1.2346            notation=std                    
    1.23456789    1             1.2            1.23            1.235            1.2346            notation=std                    
    0.000000009   0.000000009   0.0000000090   0.00000000900   0.000000009000   0.0000000090000   notation=std                    
    0.000000089   0.00000009    0.000000089    0.0000000890    0.00000008900    0.000000089000    notation=std                    
    0.000000789   0.0000008     0.00000079     0.000000789     0.0000007890     0.00000078900     notation=std                    
    0.000006789   0.000007      0.0000068      0.00000679      0.000006789      0.0000067890      notation=std                    
    0.000056789   0.00006       0.000057       0.0000568       0.00005679       0.000056789       notation=std                    
    0.000456789   0.0005        0.00046        0.000457        0.0004568        0.00045679        notation=std                    
    0.003456789   0.003         0.0035         0.00346         0.003457         0.0034568         notation=std                    
    0.023456789   0.02          0.023          0.0235          0.02346          0.023457          notation=std                    
    0.123456789   0.1           0.12           0.123           0.1235           0.12346           notation=std                    
    -1            -1            -1.0           -1.00           -1.000           -1.0000           notation=std                    
    -12           -10           -12            -12.0           -12.00           -12.000           notation=std                    
    -123          -100          -120           -123            -123.0           -123.00           notation=std                    
    -1234         -1000         -1200          -1230           -1234            -1234.0           notation=std                    
    -12345        -10000        -12000         -12300          -12340           -12345            notation=std                    
    -123456       -100000       -120000        -123000         -123500          -123460           notation=std                    
    -1234567      -1000000      -1200000       -1230000        -1235000         -1234600          notation=std                    
    -12345678     -10000000     -12000000      -12300000       -12350000        -12346000         notation=std                    
    -123456789    -100000000    -120000000     -123000000      -123500000       -123460000        notation=std                    
    -1.2          -1            -1.2           -1.20           -1.200           -1.2000           notation=std                    
    -1.23         -1            -1.2           -1.23           -1.230           -1.2300           notation=std                    
    -1.234        -1            -1.2           -1.23           -1.234           -1.2340           notation=std                    
    -1.2345       -1            -1.2           -1.23           -1.234           -1.2345           notation=std                    
    -1.23456      -1            -1.2           -1.23           -1.235           -1.2346           notation=std                    
    -1.234567     -1            -1.2           -1.23           -1.235           -1.2346           notation=std                    
    -1.2345678    -1            -1.2           -1.23           -1.235           -1.2346           notation=std                    
    -1.23456789   -1            -1.2           -1.23           -1.235           -1.2346           notation=std                    
    -0.000000009  -0.000000009  -0.0000000090  -0.00000000900  -0.000000009000  -0.0000000090000  notation=std                    
    -0.000000089  -0.00000009   -0.000000089   -0.0000000890   -0.00000008900   -0.000000089000   notation=std                    
    -0.000000789  -0.0000008    -0.00000079    -0.000000789    -0.0000007890    -0.00000078900    notation=std                    
    -0.000006789  -0.000007     -0.0000068     -0.00000679     -0.000006789     -0.0000067890     notation=std                    
    -0.000056789  -0.00006      -0.000057      -0.0000568      -0.00005679      -0.000056789      notation=std                    
    -0.000456789  -0.0005       -0.00046       -0.000457       -0.0004568       -0.00045679       notation=std                    
    -0.003456789  -0.003        -0.0035        -0.00346        -0.003457        -0.0034568        notation=std                    
    -0.023456789  -0.02         -0.023         -0.0235         -0.02346         -0.023457         notation=std                    
    -0.123456789  -0.1          -0.12          -0.123          -0.1235          -0.12346          notation=std                    
                                                                                                                                 
    0             0e0           0.0e0          0.00e0          0.000e0          0.0000e0          notation=eng                    
    1             1e0           1.0e0          1.00e0          1.000e0          1.0000e0          notation=eng                    
    12            10e0          12e0           12.0e0          12.00e0          12.000e0          notation=eng                    
    123           100e0         120e0          123e0           123.0e0          123.00e0          notation=eng                    
    1234          1e3           1.2e3          1.23e3          1.234e3          1.2340e3          notation=eng                    
    12345         10e3          12e3           12.3e3          12.34e3          12.345e3          notation=eng                    
    123456        100e3         120e3          123e3           123.5e3          123.46e3          notation=eng                    
    1234567       1e6           1.2e6          1.23e6          1.235e6          1.2346e6          notation=eng                    
    12345678      10e6          12e6           12.3e6          12.35e6          12.346e6          notation=eng                    
    123456789     100e6         120e6          123e6           123.5e6          123.46e6          notation=eng                    
    1.2           1e0           1.2e0          1.20e0          1.200e0          1.2000e0          notation=eng                    
    1.23          1e0           1.2e0          1.23e0          1.230e0          1.2300e0          notation=eng                    
    1.234         1e0           1.2e0          1.23e0          1.234e0          1.2340e0          notation=eng                    
    1.2345        1e0           1.2e0          1.23e0          1.234e0          1.2345e0          notation=eng                    
    1.23456       1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=eng                    
    1.234567      1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=eng                    
    1.2345678     1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=eng                    
    1.23456789    1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=eng                    
    0.000000009   9e-9          9.0e-9         9.00e-9         9.000e-9         9.0000e-9         notation=eng                    
    0.000000089   90e-9         89e-9          89.0e-9         89.00e-9         89.000e-9         notation=eng                    
    0.000000789   800e-9        790e-9         789e-9          789.0e-9         789.00e-9         notation=eng                    
    0.000006789   7e-6          6.8e-6         6.79e-6         6.789e-6         6.7890e-6         notation=eng                    
    0.000056789   60e-6         57e-6          56.8e-6         56.79e-6         56.789e-6         notation=eng                    
    0.000456789   500e-6        460e-6         457e-6          456.8e-6         456.79e-6         notation=eng                    
    0.003456789   3e-3          3.5e-3         3.46e-3         3.457e-3         3.4568e-3         notation=eng                    
    0.023456789   20e-3         23e-3          23.5e-3         23.46e-3         23.457e-3         notation=eng                    
    0.123456789   100e-3        120e-3         123e-3          123.5e-3         123.46e-3         notation=eng                    
    -1            -1e0          -1.0e0         -1.00e0         -1.000e0         -1.0000e0         notation=eng                    
    -12           -10e0         -12e0          -12.0e0         -12.00e0         -12.000e0         notation=eng                    
    -123          -100e0        -120e0         -123e0          -123.0e0         -123.00e0         notation=eng                    
    -1234         -1e3          -1.2e3         -1.23e3         -1.234e3         -1.2340e3         notation=eng                    
    -12345        -10e3         -12e3          -12.3e3         -12.34e3         -12.345e3         notation=eng                    
    -123456       -100e3        -120e3         -123e3          -123.5e3         -123.46e3         notation=eng                    
    -1234567      -1e6          -1.2e6         -1.23e6         -1.235e6         -1.2346e6         notation=eng                    
    -12345678     -10e6         -12e6          -12.3e6         -12.35e6         -12.346e6         notation=eng                    
    -123456789    -100e6        -120e6         -123e6          -123.5e6         -123.46e6         notation=eng                    
    -1.2          -1e0          -1.2e0         -1.20e0         -1.200e0         -1.2000e0         notation=eng                    
    -1.23         -1e0          -1.2e0         -1.23e0         -1.230e0         -1.2300e0         notation=eng                    
    -1.234        -1e0          -1.2e0         -1.23e0         -1.234e0         -1.2340e0         notation=eng                    
    -1.2345       -1e0          -1.2e0         -1.23e0         -1.234e0         -1.2345e0         notation=eng                    
    -1.23456      -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=eng                    
    -1.234567     -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=eng                    
    -1.2345678    -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=eng                    
    -1.23456789   -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=eng                    
    -0.000000009  -9e-9         -9.0e-9        -9.00e-9        -9.000e-9        -9.0000e-9        notation=eng                    
    -0.000000089  -90e-9        -89e-9         -89.0e-9        -89.00e-9        -89.000e-9        notation=eng                    
    -0.000000789  -800e-9       -790e-9        -789e-9         -789.0e-9        -789.00e-9        notation=eng                    
    -0.000006789  -7e-6         -6.8e-6        -6.79e-6        -6.789e-6        -6.7890e-6        notation=eng                    
    -0.000056789  -60e-6        -57e-6         -56.8e-6        -56.79e-6        -56.789e-6        notation=eng                    
    -0.000456789  -500e-6       -460e-6        -457e-6         -456.8e-6        -456.79e-6        notation=eng                    
    -0.003456789  -3e-3         -3.5e-3        -3.46e-3        -3.457e-3        -3.4568e-3        notation=eng                    
    -0.023456789  -20e-3        -23e-3         -23.5e-3        -23.46e-3        -23.457e-3        notation=eng                    
    -0.123456789  -100e-3       -120e-3        -123e-3         -123.5e-3        -123.46e-3        notation=eng                    
                                                                                                                                 
    0             0e0           0.0e0          0.00e0          0.000e0          0.0000e0          notation=sci                    
    1             1e0           1.0e0          1.00e0          1.000e0          1.0000e0          notation=sci                    
    12            1e1           1.2e1          1.20e1          1.200e1          1.2000e1          notation=sci                    
    123           1e2           1.2e2          1.23e2          1.230e2          1.2300e2          notation=sci                    
    1234          1e3           1.2e3          1.23e3          1.234e3          1.2340e3          notation=sci                    
    12345         1e4           1.2e4          1.23e4          1.234e4          1.2345e4          notation=sci                    
    123456        1e5           1.2e5          1.23e5          1.235e5          1.2346e5          notation=sci                    
    1234567       1e6           1.2e6          1.23e6          1.235e6          1.2346e6          notation=sci                    
    12345678      1e7           1.2e7          1.23e7          1.235e7          1.2346e7          notation=sci                    
    123456789     1e8           1.2e8          1.23e8          1.235e8          1.2346e8          notation=sci                    
    1.2           1e0           1.2e0          1.20e0          1.200e0          1.2000e0          notation=sci                    
    1.23          1e0           1.2e0          1.23e0          1.230e0          1.2300e0          notation=sci                    
    1.234         1e0           1.2e0          1.23e0          1.234e0          1.2340e0          notation=sci                    
    1.2345        1e0           1.2e0          1.23e0          1.234e0          1.2345e0          notation=sci                    
    1.23456       1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci                    
    1.234567      1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci                    
    1.2345678     1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci                    
    1.23456789    1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci                    
    0.000000009   9e-9          9.0e-9         9.00e-9         9.000e-9         9.0000e-9         notation=sci                    
    0.000000089   9e-8          8.9e-8         8.90e-8         8.900e-8         8.9000e-8         notation=sci                    
    0.000000789   8e-7          7.9e-7         7.89e-7         7.890e-7         7.8900e-7         notation=sci                    
    0.000006789   7e-6          6.8e-6         6.79e-6         6.789e-6         6.7890e-6         notation=sci                    
    0.000056789   6e-5          5.7e-5         5.68e-5         5.679e-5         5.6789e-5         notation=sci                    
    0.000456789   5e-4          4.6e-4         4.57e-4         4.568e-4         4.5679e-4         notation=sci                    
    0.003456789   3e-3          3.5e-3         3.46e-3         3.457e-3         3.4568e-3         notation=sci                    
    0.023456789   2e-2          2.3e-2         2.35e-2         2.346e-2         2.3457e-2         notation=sci                    
    0.123456789   1e-1          1.2e-1         1.23e-1         1.235e-1         1.2346e-1         notation=sci                    
    -1            -1e0          -1.0e0         -1.00e0         -1.000e0         -1.0000e0         notation=sci                    
    -12           -1e1          -1.2e1         -1.20e1         -1.200e1         -1.2000e1         notation=sci                    
    -123          -1e2          -1.2e2         -1.23e2         -1.230e2         -1.2300e2         notation=sci                    
    -1234         -1e3          -1.2e3         -1.23e3         -1.234e3         -1.2340e3         notation=sci                    
    -12345        -1e4          -1.2e4         -1.23e4         -1.234e4         -1.2345e4         notation=sci                    
    -123456       -1e5          -1.2e5         -1.23e5         -1.235e5         -1.2346e5         notation=sci                    
    -1234567      -1e6          -1.2e6         -1.23e6         -1.235e6         -1.2346e6         notation=sci                    
    -12345678     -1e7          -1.2e7         -1.23e7         -1.235e7         -1.2346e7         notation=sci                    
    -123456789    -1e8          -1.2e8         -1.23e8         -1.235e8         -1.2346e8         notation=sci                    
    -1.2          -1e0          -1.2e0         -1.20e0         -1.200e0         -1.2000e0         notation=sci                    
    -1.23         -1e0          -1.2e0         -1.23e0         -1.230e0         -1.2300e0         notation=sci                    
    -1.234        -1e0          -1.2e0         -1.23e0         -1.234e0         -1.2340e0         notation=sci                    
    -1.2345       -1e0          -1.2e0         -1.23e0         -1.234e0         -1.2345e0         notation=sci                    
    -1.23456      -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci                    
    -1.234567     -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci                    
    -1.2345678    -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci                    
    -1.23456789   -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci                    
    -0.000000009  -9e-9         -9.0e-9        -9.00e-9        -9.000e-9        -9.0000e-9        notation=sci                    
    -0.000000089  -9e-8         -8.9e-8        -8.90e-8        -8.900e-8        -8.9000e-8        notation=sci                    
    -0.000000789  -8e-7         -7.9e-7        -7.89e-7        -7.890e-7        -7.8900e-7        notation=sci                    
    -0.000006789  -7e-6         -6.8e-6        -6.79e-6        -6.789e-6        -6.7890e-6        notation=sci                    
    -0.000056789  -6e-5         -5.7e-5        -5.68e-5        -5.679e-5        -5.6789e-5        notation=sci                    
    -0.000456789  -5e-4         -4.6e-4        -4.57e-4        -4.568e-4        -4.5679e-4        notation=sci                    
    -0.003456789  -3e-3         -3.5e-3        -3.46e-3        -3.457e-3        -3.4568e-3        notation=sci                    
    -0.023456789  -2e-2         -2.3e-2        -2.35e-2        -2.346e-2        -2.3457e-2        notation=sci                    
    -0.123456789  -1e-1         -1.2e-1        -1.23e-1        -1.235e-1        -1.2346e-1        notation=sci                    
                                                                                                                                 
    0             0             0              0               0                0                 notation=std, strip_zeros=True  
    1             1             1              1               1                1                 notation=std, strip_zeros=True  
    12            10            12             12              12               12                notation=std, strip_zeros=True  
    123           100           120            123             123              123               notation=std, strip_zeros=True  
    1234          1000          1200           1230            1234             1234              notation=std, strip_zeros=True  
    12345         10000         12000          12300           12340            12345             notation=std, strip_zeros=True  
    123456        100000        120000         123000          123500           123460            notation=std, strip_zeros=True  
    1234567       1000000       1200000        1230000         1235000          1234600           notation=std, strip_zeros=True  
    12345678      10000000      12000000       12300000        12350000         12346000          notation=std, strip_zeros=True  
    123456789     100000000     120000000      123000000       123500000        123460000         notation=std, strip_zeros=True  
    1.2           1             1.2            1.2             1.2              1.2               notation=std, strip_zeros=True  
    1.23          1             1.2            1.23            1.23             1.23              notation=std, strip_zeros=True  
    1.234         1             1.2            1.23            1.234            1.234             notation=std, strip_zeros=True  
    1.2345        1             1.2            1.23            1.234            1.2345            notation=std, strip_zeros=True  
    1.23456       1             1.2            1.23            1.235            1.2346            notation=std, strip_zeros=True  
    1.234567      1             1.2            1.23            1.235            1.2346            notation=std, strip_zeros=True  
    1.2345678     1             1.2            1.23            1.235            1.2346            notation=std, strip_zeros=True  
    1.23456789    1             1.2            1.23            1.235            1.2346            notation=std, strip_zeros=True  
    0.000000009   0.000000009   0.000000009    0.000000009     0.000000009      0.000000009       notation=std, strip_zeros=True  
    0.000000089   0.00000009    0.000000089    0.000000089     0.000000089      0.000000089       notation=std, strip_zeros=True  
    0.000000789   0.0000008     0.00000079     0.000000789     0.000000789      0.000000789       notation=std, strip_zeros=True  
    0.000006789   0.000007      0.0000068      0.00000679      0.000006789      0.000006789       notation=std, strip_zeros=True  
    0.000056789   0.00006       0.000057       0.0000568       0.00005679       0.000056789       notation=std, strip_zeros=True  
    0.000456789   0.0005        0.00046        0.000457        0.0004568        0.00045679        notation=std, strip_zeros=True  
    0.003456789   0.003         0.0035         0.00346         0.003457         0.0034568         notation=std, strip_zeros=True  
    0.023456789   0.02          0.023          0.0235          0.02346          0.023457          notation=std, strip_zeros=True  
    0.123456789   0.1           0.12           0.123           0.1235           0.12346           notation=std, strip_zeros=True  
    -1            -1            -1             -1              -1               -1                notation=std, strip_zeros=True  
    -12           -10           -12            -12             -12              -12               notation=std, strip_zeros=True  
    -123          -100          -120           -123            -123             -123              notation=std, strip_zeros=True  
    -1234         -1000         -1200          -1230           -1234            -1234             notation=std, strip_zeros=True  
    -12345        -10000        -12000         -12300          -12340           -12345            notation=std, strip_zeros=True  
    -123456       -100000       -120000        -123000         -123500          -123460           notation=std, strip_zeros=True  
    -1234567      -1000000      -1200000       -1230000        -1235000         -1234600          notation=std, strip_zeros=True  
    -12345678     -10000000     -12000000      -12300000       -12350000        -12346000         notation=std, strip_zeros=True  
    -123456789    -100000000    -120000000     -123000000      -123500000       -123460000        notation=std, strip_zeros=True  
    -1.2          -1            -1.2           -1.2            -1.2             -1.2              notation=std, strip_zeros=True  
    -1.23         -1            -1.2           -1.23           -1.23            -1.23             notation=std, strip_zeros=True  
    -1.234        -1            -1.2           -1.23           -1.234           -1.234            notation=std, strip_zeros=True  
    -1.2345       -1            -1.2           -1.23           -1.234           -1.2345           notation=std, strip_zeros=True  
    -1.23456      -1            -1.2           -1.23           -1.235           -1.2346           notation=std, strip_zeros=True  
    -1.234567     -1            -1.2           -1.23           -1.235           -1.2346           notation=std, strip_zeros=True  
    -1.2345678    -1            -1.2           -1.23           -1.235           -1.2346           notation=std, strip_zeros=True  
    -1.23456789   -1            -1.2           -1.23           -1.235           -1.2346           notation=std, strip_zeros=True  
    -0.000000009  -0.000000009  -0.000000009   -0.000000009    -0.000000009     -0.000000009      notation=std, strip_zeros=True  
    -0.000000089  -0.00000009   -0.000000089   -0.000000089    -0.000000089     -0.000000089      notation=std, strip_zeros=True  
    -0.000000789  -0.0000008    -0.00000079    -0.000000789    -0.000000789     -0.000000789      notation=std, strip_zeros=True  
    -0.000006789  -0.000007     -0.0000068     -0.00000679     -0.000006789     -0.000006789      notation=std, strip_zeros=True  
    -0.000056789  -0.00006      -0.000057      -0.0000568      -0.00005679      -0.000056789      notation=std, strip_zeros=True  
    -0.000456789  -0.0005       -0.00046       -0.000457       -0.0004568       -0.00045679       notation=std, strip_zeros=True  
    -0.003456789  -0.003        -0.0035        -0.00346        -0.003457        -0.0034568        notation=std, strip_zeros=True  
    -0.023456789  -0.02         -0.023         -0.0235         -0.02346         -0.023457         notation=std, strip_zeros=True  
    -0.123456789  -0.1          -0.12          -0.123          -0.1235          -0.12346          notation=std, strip_zeros=True  
                                                                                                                                 
    0             0e0           0e0            0e0             0e0              0e0               notation=sci, strip_zeros=True  
    1             1e0           1e0            1e0             1e0              1e0               notation=sci, strip_zeros=True  
    12            1e1           1.2e1          1.2e1           1.2e1            1.2e1             notation=sci, strip_zeros=True  
    123           1e2           1.2e2          1.23e2          1.23e2           1.23e2            notation=sci, strip_zeros=True  
    1234          1e3           1.2e3          1.23e3          1.234e3          1.234e3           notation=sci, strip_zeros=True  
    12345         1e4           1.2e4          1.23e4          1.234e4          1.2345e4          notation=sci, strip_zeros=True  
    123456        1e5           1.2e5          1.23e5          1.235e5          1.2346e5          notation=sci, strip_zeros=True  
    1234567       1e6           1.2e6          1.23e6          1.235e6          1.2346e6          notation=sci, strip_zeros=True  
    12345678      1e7           1.2e7          1.23e7          1.235e7          1.2346e7          notation=sci, strip_zeros=True  
    123456789     1e8           1.2e8          1.23e8          1.235e8          1.2346e8          notation=sci, strip_zeros=True  
    1.2           1e0           1.2e0          1.2e0           1.2e0            1.2e0             notation=sci, strip_zeros=True  
    1.23          1e0           1.2e0          1.23e0          1.23e0           1.23e0            notation=sci, strip_zeros=True  
    1.234         1e0           1.2e0          1.23e0          1.234e0          1.234e0           notation=sci, strip_zeros=True  
    1.2345        1e0           1.2e0          1.23e0          1.234e0          1.2345e0          notation=sci, strip_zeros=True  
    1.23456       1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci, strip_zeros=True  
    1.234567      1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci, strip_zeros=True  
    1.2345678     1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci, strip_zeros=True  
    1.23456789    1e0           1.2e0          1.23e0          1.235e0          1.2346e0          notation=sci, strip_zeros=True  
    0.000000009   9e-9          9e-9           9e-9            9e-9             9e-9              notation=sci, strip_zeros=True  
    0.000000089   9e-8          8.9e-8         8.9e-8          8.9e-8           8.9e-8            notation=sci, strip_zeros=True  
    0.000000789   8e-7          7.9e-7         7.89e-7         7.89e-7          7.89e-7           notation=sci, strip_zeros=True  
    0.000006789   7e-6          6.8e-6         6.79e-6         6.789e-6         6.789e-6          notation=sci, strip_zeros=True  
    0.000056789   6e-5          5.7e-5         5.68e-5         5.679e-5         5.6789e-5         notation=sci, strip_zeros=True  
    0.000456789   5e-4          4.6e-4         4.57e-4         4.568e-4         4.5679e-4         notation=sci, strip_zeros=True  
    0.003456789   3e-3          3.5e-3         3.46e-3         3.457e-3         3.4568e-3         notation=sci, strip_zeros=True  
    0.023456789   2e-2          2.3e-2         2.35e-2         2.346e-2         2.3457e-2         notation=sci, strip_zeros=True  
    0.123456789   1e-1          1.2e-1         1.23e-1         1.235e-1         1.2346e-1         notation=sci, strip_zeros=True  
    -1            -1e0          -1e0           -1e0            -1e0             -1e0              notation=sci, strip_zeros=True  
    -12           -1e1          -1.2e1         -1.2e1          -1.2e1           -1.2e1            notation=sci, strip_zeros=True  
    -123          -1e2          -1.2e2         -1.23e2         -1.23e2          -1.23e2           notation=sci, strip_zeros=True  
    -1234         -1e3          -1.2e3         -1.23e3         -1.234e3         -1.234e3          notation=sci, strip_zeros=True  
    -12345        -1e4          -1.2e4         -1.23e4         -1.234e4         -1.2345e4         notation=sci, strip_zeros=True  
    -123456       -1e5          -1.2e5         -1.23e5         -1.235e5         -1.2346e5         notation=sci, strip_zeros=True  
    -1234567      -1e6          -1.2e6         -1.23e6         -1.235e6         -1.2346e6         notation=sci, strip_zeros=True  
    -12345678     -1e7          -1.2e7         -1.23e7         -1.235e7         -1.2346e7         notation=sci, strip_zeros=True  
    -123456789    -1e8          -1.2e8         -1.23e8         -1.235e8         -1.2346e8         notation=sci, strip_zeros=True  
    -1.2          -1e0          -1.2e0         -1.2e0          -1.2e0           -1.2e0            notation=sci, strip_zeros=True  
    -1.23         -1e0          -1.2e0         -1.23e0         -1.23e0          -1.23e0           notation=sci, strip_zeros=True  
    -1.234        -1e0          -1.2e0         -1.23e0         -1.234e0         -1.234e0          notation=sci, strip_zeros=True  
    -1.2345       -1e0          -1.2e0         -1.23e0         -1.234e0         -1.2345e0         notation=sci, strip_zeros=True  
    -1.23456      -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci, strip_zeros=True  
    -1.234567     -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci, strip_zeros=True  
    -1.2345678    -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci, strip_zeros=True  
    -1.23456789   -1e0          -1.2e0         -1.23e0         -1.235e0         -1.2346e0         notation=sci, strip_zeros=True  
    -0.000000009  -9e-9         -9e-9          -9e-9           -9e-9            -9e-9             notation=sci, strip_zeros=True  
    -0.000000089  -9e-8         -8.9e-8        -8.9e-8         -8.9e-8          -8.9e-8           notation=sci, strip_zeros=True  
    -0.000000789  -8e-7         -7.9e-7        -7.89e-7        -7.89e-7         -7.89e-7          notation=sci, strip_zeros=True  
    -0.000006789  -7e-6         -6.8e-6        -6.79e-6        -6.789e-6        -6.789e-6         notation=sci, strip_zeros=True  
    -0.000056789  -6e-5         -5.7e-5        -5.68e-5        -5.679e-5        -5.6789e-5        notation=sci, strip_zeros=True  
    -0.000456789  -5e-4         -4.6e-4        -4.57e-4        -4.568e-4        -4.5679e-4        notation=sci, strip_zeros=True  
    -0.003456789  -3e-3         -3.5e-3        -3.46e-3        -3.457e-3        -3.4568e-3        notation=sci, strip_zeros=True  
    -0.023456789  -2e-2         -2.3e-2        -2.35e-2        -2.346e-2        -2.3457e-2        notation=sci, strip_zeros=True  
    -0.123456789  -1e-1         -1.2e-1        -1.23e-1        -1.235e-1        -1.2346e-1        notation=sci, strip_zeros=True  
                                                                                                                                 
    0             0             0.0            0.00            0.000            0.0000            notation=std, preserve=True     
    1             1             1.0            1.00            1.000            1.0000            notation=std, preserve=True     
    12            12            12             12.0            12.00            12.000            notation=std, preserve=True     
    123           123           123            123             123.0            123.00            notation=std, preserve=True     
    1234          1234          1234           1234            1234             1234.0            notation=std, preserve=True     
    12345         12345         12345          12345           12345            12345             notation=std, preserve=True     
    123456        123456        123456         123456          123456           123456            notation=std, preserve=True     
    1234567       1234567       1234567        1234567         1234567          1234567           notation=std, preserve=True     
    12345678      12345678      12345678       12345678        12345678         12345678          notation=std, preserve=True     
    123456789     123456789     123456789      123456789       123456789        123456789         notation=std, preserve=True     
    1.2           1             1.2            1.20            1.200            1.2000            notation=std, preserve=True     
    1.23          1             1.2            1.23            1.230            1.2300            notation=std, preserve=True     
    1.234         1             1.2            1.23            1.234            1.2340            notation=std, preserve=True     
    1.2345        1             1.2            1.23            1.234            1.2345            notation=std, preserve=True     
    1.23456       1             1.2            1.23            1.235            1.2346            notation=std, preserve=True     
    1.234567      1             1.2            1.23            1.235            1.2346            notation=std, preserve=True     
    1.2345678     1             1.2            1.23            1.235            1.2346            notation=std, preserve=True     
    1.23456789    1             1.2            1.23            1.235            1.2346            notation=std, preserve=True     
    0.000000009   0.000000009   0.0000000090   0.00000000900   0.000000009000   0.0000000090000   notation=std, preserve=True     
    0.000000089   0.00000009    0.000000089    0.0000000890    0.00000008900    0.000000089000    notation=std, preserve=True     
    0.000000789   0.0000008     0.00000079     0.000000789     0.0000007890     0.00000078900     notation=std, preserve=True     
    0.000006789   0.000007      0.0000068      0.00000679      0.000006789      0.0000067890      notation=std, preserve=True     
    0.000056789   0.00006       0.000057       0.0000568       0.00005679       0.000056789       notation=std, preserve=True     
    0.000456789   0.0005        0.00046        0.000457        0.0004568        0.00045679        notation=std, preserve=True     
    0.003456789   0.003         0.0035         0.00346         0.003457         0.0034568         notation=std, preserve=True     
    0.023456789   0.02          0.023          0.0235          0.02346          0.023457          notation=std, preserve=True     
    0.123456789   0.1           0.12           0.123           0.1235           0.12346           notation=std, preserve=True     
    -1            -1            -1.0           -1.00           -1.000           -1.0000           notation=std, preserve=True     
    -12           -12           -12            -12.0           -12.00           -12.000           notation=std, preserve=True     
    -123          -123          -123           -123            -123.0           -123.00           notation=std, preserve=True     
    -1234         -1234         -1234          -1234           -1234            -1234.0           notation=std, preserve=True     
    -12345        -12345        -12345         -12345          -12345           -12345            notation=std, preserve=True     
    -123456       -123456       -123456        -123456         -123456          -123456           notation=std, preserve=True     
    -1234567      -1234567      -1234567       -1234567        -1234567         -1234567          notation=std, preserve=True     
    -12345678     -12345678     -12345678      -12345678       -12345678        -12345678         notation=std, preserve=True     
    -123456789    -123456789    -123456789     -123456789      -123456789       -123456789        notation=std, preserve=True     
    -1.2          -1            -1.2           -1.20           -1.200           -1.2000           notation=std, preserve=True     
    -1.23         -1            -1.2           -1.23           -1.230           -1.2300           notation=std, preserve=True     
    -1.234        -1            -1.2           -1.23           -1.234           -1.2340           notation=std, preserve=True     
    -1.2345       -1            -1.2           -1.23           -1.234           -1.2345           notation=std, preserve=True     
    -1.23456      -1            -1.2           -1.23           -1.235           -1.2346           notation=std, preserve=True     
    -1.234567     -1            -1.2           -1.23           -1.235           -1.2346           notation=std, preserve=True     
    -1.2345678    -1            -1.2           -1.23           -1.235           -1.2346           notation=std, preserve=True     
    -1.23456789   -1            -1.2           -1.23           -1.235           -1.2346           notation=std, preserve=True     
    -0.000000009  -0.000000009  -0.0000000090  -0.00000000900  -0.000000009000  -0.0000000090000  notation=std, preserve=True     
    -0.000000089  -0.00000009   -0.000000089   -0.0000000890   -0.00000008900   -0.000000089000   notation=std, preserve=True     
    -0.000000789  -0.0000008    -0.00000079    -0.000000789    -0.0000007890    -0.00000078900    notation=std, preserve=True     
    -0.000006789  -0.000007     -0.0000068     -0.00000679     -0.000006789     -0.0000067890     notation=std, preserve=True     
    -0.000056789  -0.00006      -0.000057      -0.0000568      -0.00005679      -0.000056789      notation=std, preserve=True     
    -0.000456789  -0.0005       -0.00046       -0.000457       -0.0004568       -0.00045679       notation=std, preserve=True     
    -0.003456789  -0.003        -0.0035        -0.00346        -0.003457        -0.0034568        notation=std, preserve=True     
    -0.023456789  -0.02         -0.023         -0.0235         -0.02346         -0.023457         notation=std, preserve=True     
    -0.123456789  -0.1          -0.12          -0.123          -0.1235          -0.12346          notation=std, preserve=True     
                                                                                                                                 
    0             0             0.0            0.00            0.000            0.0000            auto_limit=5                    
    1             1             1.0            1.00            1.000            1.0000            auto_limit=5                    
    12            10            12             12.0            12.00            12.000            auto_limit=5                    
    123           100           120            123             123.0            123.00            auto_limit=5                    
    1234          1000          1200           1230            1234             1234.0            auto_limit=5                    
    12345         10000         12000          12300           12340            12345             auto_limit=5                    
    123456        1e5           1.2e5          1.23e5          1.235e5          1.2346e5          auto_limit=5                    
    1234567       1e6           1.2e6          1.23e6          1.235e6          1.2346e6          auto_limit=5                    
    12345678      1e7           1.2e7          1.23e7          1.235e7          1.2346e7          auto_limit=5                    
    123456789     1e8           1.2e8          1.23e8          1.235e8          1.2346e8          auto_limit=5                    
    1.2           1             1.2            1.20            1.200            1.2000            auto_limit=5                    
    1.23          1             1.2            1.23            1.230            1.2300            auto_limit=5                    
    1.234         1             1.2            1.23            1.234            1.2340            auto_limit=5                    
    1.2345        1             1.2            1.23            1.234            1.2345            auto_limit=5                    
    1.23456       1             1.2            1.23            1.235            1.2346            auto_limit=5                    
    1.234567      1             1.2            1.23            1.235            1.2346            auto_limit=5                    
    1.2345678     1             1.2            1.23            1.235            1.2346            auto_limit=5                    
    1.23456789    1             1.2            1.23            1.235            1.2346            auto_limit=5                    
    0.000000009   9e-9          9.0e-9         9.00e-9         9.000e-9         9.0000e-9         auto_limit=5                    
    0.000000089   9e-8          8.9e-8         8.90e-8         8.900e-8         8.9000e-8         auto_limit=5                    
    0.000000789   8e-7          7.9e-7         7.89e-7         7.890e-7         7.8900e-7         auto_limit=5                    
    0.000006789   7e-6          6.8e-6         6.79e-6         6.789e-6         6.7890e-6         auto_limit=5                    
    0.000056789   6e-5          5.7e-5         5.68e-5         5.679e-5         5.6789e-5         auto_limit=5                    
    0.000456789   0.0005        0.00046        0.000457        0.0004568        0.00045679        auto_limit=5                    
    0.003456789   0.003         0.0035         0.00346         0.003457         0.0034568         auto_limit=5                    
    0.023456789   0.02          0.023          0.0235          0.02346          0.023457          auto_limit=5                    
    0.123456789   0.1           0.12           0.123           0.1235           0.12346           auto_limit=5                    
    -1            -1            -1.0           -1.00           -1.000           -1.0000           auto_limit=5                    
    -12           -10           -12            -12.0           -12.00           -12.000           auto_limit=5                    
    -123          -100          -120           -123            -123.0           -123.00           auto_limit=5                    
    -1234         -1000         -1200          -1230           -1234            -1234.0           auto_limit=5                    
    -12345        -10000        -12000         -12300          -12340           -12345            auto_limit=5                    
    -123456       -1e5          -1.2e5         -1.23e5         -1.235e5         -1.2346e5         auto_limit=5                    
    -1234567      -1e6          -1.2e6         -1.23e6         -1.235e6         -1.2346e6         auto_limit=5                    
    -12345678     -1e7          -1.2e7         -1.23e7         -1.235e7         -1.2346e7         auto_limit=5                    
    -123456789    -1e8          -1.2e8         -1.23e8         -1.235e8         -1.2346e8         auto_limit=5                    
    -1.2          -1            -1.2           -1.20           -1.200           -1.2000           auto_limit=5                    
    -1.23         -1            -1.2           -1.23           -1.230           -1.2300           auto_limit=5                    
    -1.234        -1            -1.2           -1.23           -1.234           -1.2340           auto_limit=5                    
    -1.2345       -1            -1.2           -1.23           -1.234           -1.2345           auto_limit=5                    
    -1.23456      -1            -1.2           -1.23           -1.235           -1.2346           auto_limit=5                    
    -1.234567     -1            -1.2           -1.23           -1.235           -1.2346           auto_limit=5                    
    -1.2345678    -1            -1.2           -1.23           -1.235           -1.2346           auto_limit=5                    
    -1.23456789   -1            -1.2           -1.23           -1.235           -1.2346           auto_limit=5                    
    -0.000000009  -9e-9         -9.0e-9        -9.00e-9        -9.000e-9        -9.0000e-9        auto_limit=5                    
    -0.000000089  -9e-8         -8.9e-8        -8.90e-8        -8.900e-8        -8.9000e-8        auto_limit=5                    
    -0.000000789  -8e-7         -7.9e-7        -7.89e-7        -7.890e-7        -7.8900e-7        auto_limit=5                    
    -0.000006789  -7e-6         -6.8e-6        -6.79e-6        -6.789e-6        -6.7890e-6        auto_limit=5                    
    -0.000056789  -6e-5         -5.7e-5        -5.68e-5        -5.679e-5        -5.6789e-5        auto_limit=5                    
    -0.000456789  -0.0005       -0.00046       -0.000457       -0.0004568       -0.00045679       auto_limit=5                    
    -0.003456789  -0.003        -0.0035        -0.00346        -0.003457        -0.0034568        auto_limit=5                    
    -0.023456789  -0.02         -0.023         -0.0235         -0.02346         -0.023457         auto_limit=5                    
    -0.123456789  -0.1          -0.12          -0.123          -0.1235          -0.12346          auto_limit=5 