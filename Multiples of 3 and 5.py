#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

result = []

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    a = n - n % 3
    b = n - n % 5
    c = n - n % 15

    if a == n:
        a -= 3
    if b == n:
        b -= 5
    if c == n:
        c -= 15

    d = (3 + a) * a // 6 + (5 + b) * b // 10 - (c + 15) * c // 30

    result.append(d)

for a1 in range(len(result)):
    print(result[a1])
