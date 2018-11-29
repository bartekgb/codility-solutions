#!/usr/bin/env python3

def solution(A):
    for x in A:
        if A.count(x) == 1:
            return x

print(solution([9,3,9,3,9,7,9]))
