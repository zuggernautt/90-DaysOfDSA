s = "abcabcbb"

def lengthOfLongestSubstring(s):

    arr= set()
    l=0
    res = 0
    for r in range(len(s)):
        while s[r] in arr:
            arr.remove(s[l])
            l+=1
        arr.add(s[r])
        res= max(res, r-+1)
        return res

print(lengthOfLongestSubstring(s))