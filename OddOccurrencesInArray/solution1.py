#!/usr/bin/env python3

def solution(A):
  xor=0
  for elem in A:
    xor^=elem
  return(xor)

print(solution([9,3,9,3,9,7,9]))
