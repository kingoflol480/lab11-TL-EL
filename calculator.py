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
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def logarithm(a, b): 
    if b <= 0 or b == 1:
        raise ValueError("Invalid base for logarithm")
    if a <= 0:
        raise ValueError("Invalid argument for logarithm")
    return math.log(a,b)

def exponent(a, b): 
    return a**b

def square_root(a): 
    if a < 0:
        raise ValueError("Invalid argument for square root")
    return math.sqrt(a)

def hypotenuse(a, b): 
    return math.hypot(a, b) 
