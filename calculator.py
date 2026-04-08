"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def logarithm(a, b): 
    try:
        return math.log(a, b)
    except ValueError as e:
        raise ValueError("Invalid argument for logarithm") from e

def exponent(a, b): 
    return a**b

def square_root(a): 
    try:
        return math.sqrt(a)
    except ValueError as e:
        raise ValueError("Invalid argument for square root") from e

def hypotenuse(a, b): 
    return math.hypot(a, b) 
