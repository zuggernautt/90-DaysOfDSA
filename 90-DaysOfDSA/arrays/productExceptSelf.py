nums = [1,0,3,4]

def productExceptSelf(nums):
    prod = 1
    res = []
    for i in nums:
        prod = prod*i


    for j in nums:
        if j == 0:
            res.append
        
        
        res.append(int(prod/j))
    return res

print(productExceptSelf(nums))
#division operator not allowed so above method is invaliad
# so take two arrays prefix and postfix and get their product in res array
# or as for this question res array doesnt count for space compllexity so do all operations in
#array


def productExceptSelf(nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


