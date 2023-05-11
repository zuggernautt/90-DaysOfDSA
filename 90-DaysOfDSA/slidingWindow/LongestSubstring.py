s = "abcabcbb"

def lengthOfLongestSubstring(s):

    l=r=0
    charSet = set()
    res = 0
    while r<len(s):
        if s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        else:
            charSet.add(s[r])
            r+=1
        res = max(res, r-l)
    return res



print(lengthOfLongestSubstring(s))