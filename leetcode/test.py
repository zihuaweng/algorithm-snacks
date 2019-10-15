#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

def equationsPossible(equations):
    UF = {}

    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]

    for equation in equations:
        x, e1, e2, y = equation
        if x not in UF: UF[x] = x;
        if y not in UF: UF[y] = y;
        if e1 != '!':
            UF[find(x)] = find(y)

    print(UF)

    for equation in equations:
        x, e1, e2, y = equation
        if e1 == '=' and find(x) != find(y): return False
        if e1 == '!' and find(x) == find(y): return False

    return True


equationsPossible(["a==b","a==c","b!=c"])