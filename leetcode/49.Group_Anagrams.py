# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for string in strs:
            temp = ''.join(sorted(string))
            if temp in dic:
                dic[temp] += [string]
            else:
                dic[temp] = [string]
        res = []
        for value in dic.values():
            res.append(value)
        return res
