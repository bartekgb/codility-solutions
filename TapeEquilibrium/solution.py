#!/usr/bin/env python3

def solution(A):
  lenA=len(A)
  sum=[]
  sum.append(A[0])
  for ind in range(1,lenA):
    sum.append(sum[ind-1]+A[ind])

  min=abs(A[0]-(sum[lenA-1]-A[0]))

  for P in range(2,lenA):
    diff=abs(sum[P-1]-(sum[lenA-1]-sum[P-1]))
    if (diff<min):
      min=diff

  return(min)

print(solution([3,1,2,4,3]))
