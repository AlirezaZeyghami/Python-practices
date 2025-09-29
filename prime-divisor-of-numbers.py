"""
Prime divisor of numbers
"""
import math


def is_prime(i):
    if i == 1:
        return False
    for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                return False
    return True


def prime_divisors_count(n):    
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            count += 1
    return count


numbers = []
for _ in range(10):
    n = int(input())
    numbers.append(n)


the_most_count = -1
the_most_owner = None
for n in numbers:
    prime_count = prime_divisors_count(n)
    if prime_count > the_most_count or (prime_count == the_most_count and \
                                    n > the_most_owner ):
        the_most_count = prime_count
        the_most_owner = n
    
print(the_most_owner, the_most_count)
