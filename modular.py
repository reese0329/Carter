# from my_module import c_to_f
#
# celsius = float(input("Enter a temperature in Celsius:"))
# fahrenheit = c_to_f(celsius)
# print ("That's ",fahrenheit,"degree Fahrenheit")

import my_module

celsius = float(input("Enter a temperature in Celsius:"))
fahrenheit = my_module.c_to_f(celsius)
print ("That's ",fahrenheit,"degree Fahrenheit")