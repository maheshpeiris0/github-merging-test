
from itertools import count
def count(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count