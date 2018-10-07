import numpy as np
# GF 2^8
m = 8
mask = 1 << m    # 0x100 => x^8
mask2 = mask - 1 # 0x FF 
irr  = 283 # irreducible x^8 + x^4 + x^3 + x + 1

def multGF(p2,p1):
    p = 0
    while p2 :
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask:
            p1 ^= irr
        p2 >>= 1
    return p & mask2


print(multGF(2,255))
