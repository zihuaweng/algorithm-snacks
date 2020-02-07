#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


import heapq
import collections


def dijkstra(edges, f, t):
    g = collections.defaultdict(list)
    for s, e, c in edges:
        g[s].append((c, e))

    q = [(0, f, [])]
    seen = set()
    mins = {f: 0}

    while q:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            if v1 == t:
                return (cost, path + [v1])

            for c2, v2 in g[v1]:
                if v2 not in seen:
                    new_cost = cost + c2
                    pre = mins.get(v2, None)
                    if pre is None or new_cost < pre:
                        mins[v2] = new_cost
                        heapq.heappush(q, (new_cost, v2, path + [v1]))
    return float('inf')


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("A -> E:")
    print(dijkstra(edges, "A", "E"))
    print("F -> G:")
    print(dijkstra(edges, "F", "G"))