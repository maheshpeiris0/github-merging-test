def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def count(num):
    count = 0
    while num > 0:

        num = num // 50
        count += 100
    return count





