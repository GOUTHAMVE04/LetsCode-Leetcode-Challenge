class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth,count=0,0
        for par in s:
            if(par=="("):
                count+=1
                max_depth=max(max_depth,count)
            elif(par==")"):
                count-=1
        return max_depth
    