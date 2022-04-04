"""
Author: Lani Hurley
Date: 4/4/22
Filename: gaussSumRange.py
Simple Python example of using a loop independent of a list. Program uses for() loop to iterate and add all the numbers
in range().
"""
# accumulator variable
total = 0

""" for() loop will loop through the sequence of numbers that are within range(start, stop) and add every number 
in this range to the total starting from 0 (giving the sum of 0 to 100)"""

for number in range(0, 101):
    # variable holds and accumulates sum of numbers
    total += number
    # prints all the totals in the sequence
    print(total)