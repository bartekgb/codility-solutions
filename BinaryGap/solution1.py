#!/usr/bin/env python3

def solution(integer):
    strint = bin(integer)[2:]
    strint = strint.strip('0').split('1')
    strint.sort()
    strint.reverse()
    
    return len(strint[0])

print(solution(1041))
print(solution(32))
