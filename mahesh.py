def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def count(num):
    count = 0
    while num > 0:

        num = num // 10000
        count += 17000
    return count