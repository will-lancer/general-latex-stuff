#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:58:36 2023

@author: willlancer
"""

#error calculator: DIVISION

first_parameter = float(input("first parameter: ")) #first val 
second_parameter = float(input("second parameter: ")) #second val

delta_first = float(input("error first: ")) #error first
delta_second = float(input("error second: ")) #error second

final_error = (first_parameter)/(second_parameter) * ( ((delta_first)/(first_parameter))**2 + 
((delta_second)/(second_parameter))**2 )**(1/2)

#^^error calculation

final_val = (first_parameter)/(second_parameter) #final value


print("final value: " + str(final_val)) #prints final value
print("error: " + str(final_error)) #prints final error

#choose first and second parameters carefully, as I'm assuming the
#first divides the second.
