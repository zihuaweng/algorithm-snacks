# https://leetcode.com/discuss/interview-question/871512/Amazon-or-OA-2020-or-Shopping-Patterns
"""
products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]

res = 2 4 5

"""
import collections

def shipping_pattern(products_nodes, products_edges, products_from, products_to):
    res = float('inf')
    graph = collections.defaultdict(set)

    for _from, _to in zip(products_from, products_to):
        graph[_from].add(_to)
        graph[_to].add(_from)

    for a, b in zip(products_from, products_to):  # O(N)
        if a in graph[b] and b in graph[a]:
            c_list = graph[a] & graph[b]   #O(M)
            if not c_list:
                continue
            for c in c_list:
                res = min(res, len(graph[a]) + len(graph[b]) + len(graph[c]) - 6)

    if res < float('inf'):
        return res
    return -1



products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]
print(shipping_pattern(products_nodes, products_edges, products_from, products_to))