# question: https://www.1point3acres.com/bbs/thread-670298-1-1.html


import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.nums = set()

def get_num(string):
    # calculate numbers
    if ord(string) >= ord('A') and ord(string) <= ord('R'):
        return str((ord(string)-ord('A')) // 3 + 2)
    d = {'S': '7', 'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X':'9', 'Y':'9', 'Z':'9'}
    return d[string]

def vanity(codes, numbers):
    root = TrieNode()
    numbers = list(set(numbers))
    for i, number in enumerate(numbers):
        for j in range(len(number)):
            sub_num = number[j:]
            node = root
            for n in sub_num:
                if n in ['0', '1', '+', '*', '#']:
                    if node != root:
                        node.nums.add(i)
                    break
                node = node.children[n]
                node.nums.add(i)

    res = set()
    for s in codes:
        res |= search(root, s)

    res_num = []
    for i in res:
        res_num.append(numbers[i])
    return sorted(res_num)

def search(node, s):
    for char in s:
        char = get_num(char)
        if char not in node.children:
            return set()
        node = node.children[char]
    return node.nums

    
print(function(["+17474824380", "+12343423434", "+15109926333", "+14157088956"], ["TWLO", "CODE", "HTCH"]))