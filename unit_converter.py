# Engineering Unit Conversion Toolkit
# Author: Derek Daggett
# Purpose: Practice engineering unit conversions using Python functions.

def feet_to_meters(feet):
    return feet * 0.3048

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def knots_to_mph(knots):
    return knots * 1.15078

def horsepower_to_watts(horsepower):
    return horsepower * 745.7

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Engineering Unit Conversion Toolkit")
print("-----------------------------------")

print("10 feet =", feet_to_meters(10), "meters")
print("150 pounds =", pounds_to_kilograms(150), "kilograms")
print("100 knots =", knots_to_mph(100), "mph")
print("1 horsepower =", horsepower_to_watts(1), "watts")
print("68°F =", fahrenheit_to_celsius(68), "°C")
