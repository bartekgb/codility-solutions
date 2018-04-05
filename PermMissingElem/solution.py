#!/usr/bin/env python3

def solution(A):
  if len(A)==0:
    return(1)
  else:
    max=A[0]
    sum=0
    for x in A:
      if (x>max):
        max=x
      sum+=x

    sumnk=int((max*(max+1))/2)
    if (sumnk-sum==0):
      return(sumnk+max+1-sum)
    else:
      return(sumnk-sum)

print(solution([2,3,1,5]))
