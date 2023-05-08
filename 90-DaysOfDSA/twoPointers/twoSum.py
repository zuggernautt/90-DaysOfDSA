nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    res= []
    nums.sort()
    n = len(nums)
    
    for i in range(n-2):
        if i>0 and nums[i] == nums[i+1]:
            continue
        j,k = 1, n-1
        while j<k:
            threesum = nums[i]+nums[j]+nums[k]
            if sum == 0:
                while j<k and nums[j]==nums[j+1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
                j+=1
                k-=1
            elif sum>0:
                k-=1
            else:
                j+=1
    return res

                
