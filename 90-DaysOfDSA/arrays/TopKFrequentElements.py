# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#my brute force solution
nums,k=[-1,-1],1

from collections import Counter


def topKFrequent(nums, k):
        dict = Counter(nums)

        sorted_items = sorted(dict.items(),key=lambda x:x[1], reverse=True)

        top_values = [sorted_items[i][0] for i in range(k)]
        return top_values


