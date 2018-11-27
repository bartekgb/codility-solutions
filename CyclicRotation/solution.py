#!/usr/bin/env python3

def shiftOne(array):
    newArr=[]
    newArr.append(array[len(array)-1])
    for x in range(0,len(array)-1):
        newArr.append(array[x])
    return(newArr)

def solution(array,k):
    if (k!=len(array) and len(array)!=0):
        for i in range(k%len(array)):
            tmp=shiftOne(array)
            array=tmp
    return(array)


print(solution([1,2,3,4,5],2))
