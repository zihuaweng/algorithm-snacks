#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.waitlist = []
        # create a trie
        for word in words:
            temp_dict = self.trie
            for char in word:
                temp_dict = temp_dict.setdefault(char, dict())
            temp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        temp = []
        if letter in self.trie:
            temp.append(self.trie[letter])
        for item in self.waitlist:
            if letter in item:
                temp.append(item[letter])

        self.waitlist = temp
        return any('#' in item for item in self.waitlist)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
