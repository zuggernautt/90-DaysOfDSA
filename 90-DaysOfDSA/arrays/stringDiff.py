class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s:
            res=res^ord(i)
        for j in t:
            res=res^ord(j)
        res = chr(res)
        return res