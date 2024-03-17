def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    s = 0
    i = 0

    while True:
        if n <= 10:
            if n == 8:
                s += 1
            break
        if n % 10 == 8:
            s += 1
        n = n//10
        i += 1
    if s == 2:
        return True
    return False
print(double_eights(88128))