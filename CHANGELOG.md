# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## Unreleased

## Fixed
-  Made `demonstration.py` Python 2 compatible (emoved `end` keyword from print statements)

### Added
- `convention` argument to `to_precision()`
- Travis CI integration
- Header comments & permissions so test.py could be run as a script ($ ./tests.py)
- CHANGLELOG.md


## 2.0.0 - 2015-12-03

### Fixed
- `to_precision(0, 1, 'auto') => '0'` instead of '0.e0'`
- `to_precision(0, 1, 'std') => '0'` instead of `'0.'`

### Added
- Options to to_precision(): `auto_limit`, `strip_zeros`, `preserve_integer`
- `demonstration.py`
- `auto_notation()`
- 'delimiter' as default option to `sci_notation()`, `eng_notation()`

### Changed
- `filler` argument to `delimiter`

