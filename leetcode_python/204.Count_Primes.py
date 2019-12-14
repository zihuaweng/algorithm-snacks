#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/count-primes/
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(int(n**0.5)+1):
            if primes[i]:
                for j in range(i+i, n, i):
                    primes[j] = False
        return sum(primes)