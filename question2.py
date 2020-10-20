def first_odds(n):

    i = 1
    odd_number = 0

    while i <= n:
        if odd_number % 2 != 0:
            print(f"{i}: {odd_number}")
            i += 1
        odd_number += 1


first_odds(100)
