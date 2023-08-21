#iterative approach



# def sw(inp):
#     n=len(inp)
#     res=0
    
#     for i in range(n-k+1):
#         curr_sum=0
#         for j in range(k):
#             curr_sum = curr_sum+ inp[i+j]
                             
#         res= max(curr_sum, res)
#     return res


def sw(inp, k):
    n=len((inp))

    curr_sum = sum(inp[:k])
    max_sum = 0

    for i in range(n-k):

        curr_sum = curr_sum -inp[i] + inp[i+k]
        max_sum = max(curr_sum, max_sum)
    return max_sum

inp = [1, 4, 2, 10, 23, 3, 1, 0, 20] 
k=4
print(sw(inp, k))


def lengthOfLongestSubstring(self, s: str) -> int:
       
        n = len(s)
        profit=0
        for i in range(n):
            for j in range(i, n):
                curr_profit = s[j]-s[i]
                profit = max(curr_profit, profit)

        return profit

print(lengthOfLongestSubstring(s))