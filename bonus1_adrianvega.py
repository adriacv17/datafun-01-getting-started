"""

Purpose: Calculate the area of a circle.

Author: Denise Case

This script illustrates importing modules and using constants.

It illustrates the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# Ask for glucose values for three different patients
patient_alpha = input("Enter patient alpha's glucose: ")
patient_beta = input("Enter patient beta's glucose: ")
patient_gamma = input("Enter patient gamma's glucose: ")

# Convert strings to integers
alpha = int(patient_alpha)
beta = int(patient_beta)
gamma = int(patient_gamma)

#Calculate average, sum, product, min, max
sum = alpha + beta + gamma
average_glucose = (alpha + beta + gamma)/sum
product = alpha * beta * gamma
min_glucose = min(alpha, beta, gamma)
max_glucose = max(alpha, beta, gamma)

#Logged results
logger.info(f"The average of glucose of all patients is {average_glucose}.")
logger.info(f"The sum of glucose of all the patients is {sum}.")
logger.info(f"The product of all the glucose of all the patients is {product}.")
logger.info(f"The minimum glucose of all the patients is {min_glucose}.")
logger.info(f"The maximum glucose result of all the patients is {max_glucose}.")