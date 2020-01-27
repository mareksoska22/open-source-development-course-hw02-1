[![Build Status](https://travis-ci.org/mareksoska22/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.org/mareksoska22/open-source-development-course-hw02-1)

# Simple Vector implementation in python

Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations: (Supported verctor-based operations)
- Addition with a scalar: `a + 1`
- Vector addition: `a + b`
- Vector comparison: `a >/>=/</<=/==/!= b` compares vectors according to their length
- Vector negation: `neg a` is equals to mutiplying vector by (-1)
- Reversed vector: `reverse a` reverses the order of vector coordinates
- Subtraction with a scalar: `a - 1`
- Vector subtraction: `a - b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector

Matrix operations:
- Addition

- Bitwise XOR on every coordinate: `a ^ 3` returns vector with XORed coords
- Vector length: `len a`
- Vector modification - modifies a verctor's coordinates

## Installation

```bash
pip install -U --no-cache .
```
