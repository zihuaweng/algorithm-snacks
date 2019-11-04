#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        length_s = len(S)
        length_t = len(T)
        t_idx = 0
        res = ''
        min_length = float('inf')
        fast = 0

        while fast < length_s:
            if S[fast] == T[t_idx]:
                t_idx += 1
            if t_idx == length_t:
                t_idx -= 1
                slow = fast
                while slow >= 0 and t_idx >= 0:
                    if S[slow] == T[t_idx]:
                        t_idx -= 1

                        if t_idx == -1:
                            if fast - slow + 1 < min_length:
                                min_length = fast - slow + 1
                                res = S[slow:fast + 1]
                            break
                    slow -= 1

                fast = slow + 1
                t_idx = 0
            else:
                fast += 1

        return res



# dp 做法
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        m = len(T)
        min_length = float('inf')
        res = ''
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = i + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        # print(dp)

        for i in range(1, n + 1):
            if dp[m][i] != 0:
                if i - dp[m][i] + 1 < min_length:
                    min_length = i - dp[m][i] + 1
                    res = S[dp[m][i] - 1:i]

        return res


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        m = len(T)
        min_length = float('inf')
        res = ''
        dp = [i for i in range(1, n + 2)]

        for i in range(m):
            temp = [0] * (n + 1)
            for j in range(1, n + 1):
                if T[i] == S[j - 1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = temp[j - 1]

            dp = temp

        # print(dp)

        for i in range(1, n + 1):
            if dp[i] != 0:
                if i - dp[i] + 1 < min_length:
                    min_length = i - dp[i] + 1
                    res = S[dp[i] - 1:i]

        return res

