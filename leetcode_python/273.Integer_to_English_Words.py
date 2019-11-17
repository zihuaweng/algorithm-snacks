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

# 自己写的啰嗦版本

class Solution:
    def numberToWords(self, num: int) -> str:

        #         1  2   3  4  5  6  7

        #         1,000,000

        #         //10^0 [123...9]
        #         //10^1  [20, ,90]
        #         //10^2 [123..9] + 'hundred'

        #         //10^3  [123..9] + 'thousand'
        #         //10^4 [10, 20, ,90] + 'thousand'
        #         //10^5 [123..9] + 'hundred' + 'thousand'

        #         //10^6 [123..9] + 'million'
        #         //10^7 [10, 20, ,90] + 'million'
        #         //10^8 [123..9] + 'hundred' + 'million'

        #         //10^9 [123..9] + 'billion'
        #         //10^10 [10,20, ,90] + 'billion'
        #         //10^11 [123..9] + 'hundred' + 'billion'

        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def word(n, res):
            if n == 0:
                if res:
                    return res
                else:
                    return 'Zero'
            if n < 20:
                if res:
                    return res + ' ' + to19[n - 1]
                else:
                    return to19[n - 1]
            if n < 100:
                if res:
                    res += ' ' + tens[n // 10 - 2]
                else:
                    res = tens[n // 10 - 2]
                return word(n % 10, res)
            if n < 1000:
                if res:
                    res += ' ' + to19[n // 100 - 1] + ' Hundred'
                else:
                    res = to19[n // 100 - 1] + ' Hundred'
                return word(n % 100, res)
            for i, unit in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if n < 1000 ** (i + 1):
                    res = word(n // (1000 ** i), res)
                    res += ' ' + unit
                    return word(n % (1000 ** i), res)

        res = ''
        return word(num, res)
        return res







