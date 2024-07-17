import numpy as np
import sys
from math import ceil

# def factorize(n):

# print(ceil(11/2))

n = 12

check_factor = lambda n, i : 0 == n % i 

def check_perfect(n):
    items = np.arange(1, ceil(n/2)+1)
    factors = []
    for i in items:
        # print(i)
        if 0 == (n % i):
            factors.append(i)
            # factors.append(n / i)
            # np.delete(items, n / i)
    if sum(factors) == n:
        return n

# # print(factors)

# for i in np.arange(10_000_000_000):
#     if check_perfect(i):
#         print(i)


print(check_factor(12, 6))
items = np.arange(1, ceil(n/2)+1)
# np.apply_along_axis(check_factor, 0, items)
check_factors = np.vectorize(check_factor)
check_factors(n, items)
