square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def div_by_primes_under_no_lambda(n):
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(m):
                def inner(k,checker=checker):
                    return checker(k) or k % m == 0  
                return inner
            checker = outer(i)
        i = i+1
    return checker

print(div_by_primes_under_no_lambda(10)(12))