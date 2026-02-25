class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(1,n+1):
            if(i%n==0 and i%2==0):
                return i
            elif (i%n==0 and i%2==1):
                return 2*i
        """
        :type n: int
        :rtype: int
        """
        