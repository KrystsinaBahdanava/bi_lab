def fizzbuzzz(fizzbuzz):

    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        p = "fizzbuzz"
    elif fizzbuzz % 3 == 0:
        p = "fizz"
    elif fizzbuzz % 5 == 0:
        p = "buzz"
    else:
        p = str(fizzbuzz)
    return p
