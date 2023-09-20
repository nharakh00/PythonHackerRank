def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0: 
        leap = True
        return leap 
    else: leap = False
    
    if year % 100 == 0 and year % 400 != 0:
        leap = False
        return leap
    else: leap = True 
    
    if year % 400 == 0 and year % 100 == 0 and year % 4 == 0:
        leap = True
        return leap
    else: leap = False
    
    return leap

year = int(input())
