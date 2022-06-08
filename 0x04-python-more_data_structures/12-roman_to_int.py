#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or (not isinstance(roman_string, str)):
        return (0)

    roman_numbers_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    
