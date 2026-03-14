class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=min(prices)
        prices.remove(a)
        b=min(prices)
        if(money<=a or money<=b or (a+b)>money):
            return money
        return money-(a+b)
        


            


        