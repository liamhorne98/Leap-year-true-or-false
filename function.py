def distance_from_zero(number):
    if type(number) is int or type(number) is float:
        if number < 0:
            return number*-1
        else:
            return number
    else:
         return "Nope"

import calendar
def is_leap(year):
    if year %4 == 0:
        return True
    else:
        return False
print(is_leap(2010))