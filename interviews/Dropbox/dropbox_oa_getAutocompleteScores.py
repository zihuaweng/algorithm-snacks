# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getAutocompleteScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY documentTitles
#  2. STRING_ARRAY documentBodies
#  3. STRING_ARRAY queries
#

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
        self.score = 0

def getAutocompleteScores(documentTitles, documentBodies, queries):

    # Build trie, each node will be on char from words
    root = TrieNode()
    # Count chars in all words
    counter = {}
    for title in documentTitles:
        for word in title.split():
            counter[word] = counter.get(word, 0) + 10

    for body in documentBodies:
        for word in body.split():
            counter[word] = counter.get(word, 0) + 1

    # Put char in trie and record every max score for the path
    for word, c in counter.items():
        p = root
        for char in word:
            # Keep track of the max value of very path
            p.score = max(p.score, c)
            p = p.children[char]
        p.score = max(p.score, c)
        p.end = True

    res = []
    # search query:
    for query in queries:
        # Check whether all chars in query match, if not return 0
        match = True
        node = root
        for char in query:
            # If not all chars match return 0
            if char not in node.children:
                # print('not char' + query)
                res.append(0)
                match = False
                break
            node = node.children[char]
        if match:
            # if match, then return the score
            res.append(node.score)
    return res

if __name__ == '__main__':
