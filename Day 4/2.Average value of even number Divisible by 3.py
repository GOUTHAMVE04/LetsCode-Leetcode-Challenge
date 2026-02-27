from ast import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum,count=0,0
        for i in nums:
            if(i%6==0):
                sum=sum+i
                count+=1
        return sum//count if count!=0 else 0