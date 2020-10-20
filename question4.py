def is_leap_year(a_year):
    leap = False

    if a_year % 400 == 0:
        leap = True

    elif a_year % 100 ==0:
        leap = False

    elif a_year % 4 == 0:
        leap = True

    return leap

a_year = int(input())
print(is_leap_year(a_year))
