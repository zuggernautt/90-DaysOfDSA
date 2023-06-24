
hmap={}
def twoSum(nums, target):
    for index, item in enumerate(nums):
        item = target-item
        hmap[index]= item
    for i, num in enumerate(nums):
        if num in hmap.keys() and i != hmap[num]:
            return i, hmap[num]