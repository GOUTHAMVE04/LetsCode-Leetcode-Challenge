class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ds=0
        for i in nums:
            while(i>0):
                ds+=i%10
                i=i//10
        return abs(sum(nums)-ds)