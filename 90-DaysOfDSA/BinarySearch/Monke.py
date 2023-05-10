piles,h=[312884470], 312884469
import math

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = max(piles)
    while l<=r:
        time = 0
        k = (l+r)//2
        for p in piles:
            time += math.ceil(p / k)
        if time <= h:
            
            res = min(res, k)
            r= k-1
        else:
            l=k+1

    return res
            

print(minEatingSpeed(piles, h))