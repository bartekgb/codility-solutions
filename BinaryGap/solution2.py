#!/usr/bin/env python3

def solution(integer):
    l = 0
    lmax = 0

    # strip zeros on the right
    while integer:
        if integer & 1 == 1:
            integer >>= 1
            break
        else:
            integer >>= 1

    # perform right bit shift stripping rightmost one and count zeros
    while integer:
        if integer & 1 == 1:
            lmax = max(lmax,l)
            l = 0
        else:
            l += 1
        integer >>= 1

    return lmax

print(solution(1041))
