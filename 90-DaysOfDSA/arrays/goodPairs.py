from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for i in count.values():
            res+=((i)*(i-1))/2
        return int(res)

