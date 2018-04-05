#!/usr/bin/env python3

def solution(X,Y,D):
  diff=Y-X
  mod=diff%D
  floor=diff//D
  if (mod==0):
    return(floor)
  else:
    return(floor+1)

print(solution(10,85,30))
