nums, target =  [1,3,4,5,7,11], 9

# for brute force tc = O(n^2)

#this is optimized way given that nums is non decreasing order
def twoSum(nums,target):
    i,j = 0,len(nums)-1
    while i<j:
        if nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            return i+1,j+1

        
print(twoSum(nums, target))