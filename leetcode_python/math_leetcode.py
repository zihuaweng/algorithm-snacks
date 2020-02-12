#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

import math

# 最大公约数   Greatest common divisor
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


# 计算约数个数
# 时间复杂度 O(n)
def divisor1(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count


# count primer
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, n, i):
                    primes[j] = False
        return sum(primes)


# 计算约数个数
# 时间复杂度 O( sqrt(n) )
def divisor2(num):
    count = 0
    sqrt = int(num ** 0.5)
    for x in range(1, sqrt + 1):
        if num % x == 0:
            count += 2
            print(x, num // x)
    return count - (sqrt ** 2 == num)


# power of 4
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


# power of 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


# power of 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(2)) % 1 == 0


# devide
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            shift = 0
            while a >= b << (shift + 1):
                print(a, res)
                shift += 1
            res += 1 << shift
            a -= b << shift
        return min(res if sig else -res, (1 << 31) - 1)


# power
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n & 1 == 0:
            return self.myPow(x * x, n >> 1)
        else:
            return x * self.myPow(x * x, n >> 1)
