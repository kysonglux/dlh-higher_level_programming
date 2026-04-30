#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = roman_string
    if not roman:
        return None
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_number = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and dic[roman[i]] < dic[roman[i + 1]]:
            roman_number -= dic[roman[i]]
        else:
            roman_number += dic[roman[i]]
    return roman_number
