#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def word(n):
            if n < 20:
                return to19[n - 1:n]
            if n < 100:
                return [tens[n // 10 - 2]] + word(n % 10)
            if n < 1000:
                return [to19[n // 100 - 1]] + ['Hundred'] + word(n % 100)
            for i, j in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if n < 1000 ** (i + 1):
                    return word(n // (1000 ** i)) + [j] + word(n % (1000 ** i))

        return ' '.join(word(num))

