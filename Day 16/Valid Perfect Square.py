class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        rt=num**0.5
        if (rt==int(rt)):
            return True
        else:
            return False
        