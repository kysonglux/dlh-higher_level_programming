#!/usr/bin/python3

def max_integer(my_list=[]):
    # max_value = 0  This fails for lists with all negative numbers.
    if my_list == []:
        return None
    else:
        my_list.sort()
        max_value = my_list[-1]
    return (max_value)
