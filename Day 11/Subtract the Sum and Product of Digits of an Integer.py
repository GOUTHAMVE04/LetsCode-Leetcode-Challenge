class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p,s=1,0
        n=str(n)
        for i in n:
            p*=int(i)
            s+=int(i)
        return p-s
        