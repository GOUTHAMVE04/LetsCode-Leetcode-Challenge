class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()

        res=""
        for i in range(0,k):
            res+=str(s[i])
            if(i<k-1):
                res+=" "
        return res
        
        
        