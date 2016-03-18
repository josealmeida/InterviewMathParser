# Interview Technical Assignment - Math Parser

As part of the interview process, we require all candidates to submit a solution to a technical test.  We expect you to complete this as you would production code and be mindful of the practices and behaviours that NICE will be looking for - testing, design, craftsmanship etc.  I would suggest that spending 2-3 hours on the code is more than sufficient to give us an idea of your approach and technical ability.

===================

# Instructions
Implement a custom mathematical parser to take a string expression and compute its numerical value.

The parser must implement an order of precedence of left to right, brackets are used to explicitly denote precedence by grouping parts of an expression that should be evaluated first again left to right.

Rules:

a = '+', b = '-', c = '*', d = '/', e = '(', f = ')'

## Acceptance criteria

```
Input: 3a2c4
Result: 20

Input: 32a2d2
Result: 17

Input: 500a10b66c32
Result: 14208

Input: 3ae4c66fb32
Result: 235

Input: 3c4d2aee2a4c41fc4f
Result: 990

```

* Implement a solution in the language of your choice
* _prove_ that it meets the acceptance criteria.
* The supplied solution must compile (if required) and run on Windows 7.
* Submit your solutions via email (as a zip file).
* Please provide instructions explaining how to run your solution
