
def eating_all_cookies(n):

    lookup ={"sum_previous":1, "sum_current":1}


    if n == 1:

        return lookup["sum_current"]


    counter = 2

    while counter <= n:

        current = lookup["sum_current"]

        lookup["sum_current"] = lookup["sum_previous"] + current

        lookup["sum_previous"] = current

        counter += 1

    return lookup["sum_current"]

def eating_all_cookies2(n):

    if n == 0:

        return 1

    else:

        return 2**(n-1)

    




