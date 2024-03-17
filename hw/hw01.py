import operator
def two_of_three(x,y,z):
    s = max(x,y,z)
    if s == x:
        return operator.mul(y,y)+operator.mul(z, z)
    if s == y:
        return operator.mul(x, x)+operator.mul(z, z)
    if s == z:
        return operator.mul(x, x)+operator.mul(y, y)
print(two_of_three(1, 2, 3))
print(two_of_three(5, 3, 1))
print(two_of_three(10, 2, 8))


##找最大因数
def largest_factor(n):
    i=n-1
    while (i > 0):
        if n % i == 0:
            return i
        i -= 1
print(largest_factor(15))
print(largest_factor(80))
print(largest_factor(13))


##if函数
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
print(if_function(2>3, 2, 3))
print(if_function(3>2, 2, 3))
##把condition换成函数
def with_if_statement():
    if c():##但是这里的c,t,f都是空函数
        return t()
    else:
        return f()

#冰雹数组？
def hailstone(n):
    i=0
    while (True):
        i += 1
        if n == 1:
            return i
        else:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
        
print(hailstone(10))
            