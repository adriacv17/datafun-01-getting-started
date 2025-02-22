"""
Purpose: Illustrate basic expressions and operators in Python.

Author: Denise Case

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""

# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Declare  Variables
# TODO: Try changing the values of these variables
# TODO: Add some new variables (like rectangle_length and rectangle_width)
#       and calculate the area of a rectangle (rectangle_area = rectangle_length * rectangle_width)
triangle_base = 11
triangle_height = 6
rectangle_length = 17
rectangle_width = 4
num1 = 45
num2 = 50
float_num1 = 7.7
float_num2 = 2.1
float_num3 = 4.3

# Basic Arithmetic Operations
triangle_area_renamed = triangle_base * triangle_height / 2
total_sum = float_num1 + float_num2
difference = num1 - num2

rectangle_area = rectangle_length * rectangle_width

# Log Information
logger.info(
    f"Given base={triangle_base} and height={triangle_height}, triangle area = {triangle_area_renamed}"
)
logger.info(
    f"Given length={rectangle_length} and width={rectangle_width}, rectangle area = {rectangle_area}"
)
logger.info(
    f"Given float_num1={float_num1} and float_num2={float_num2}, sum = {total_sum}"
)
logger.info(f"Given num1={num1} and num2={num2}, the difference = {difference}")
