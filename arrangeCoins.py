class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        num=n
        for i in range(1,n+1):
            
            if(num-i>=0):
             
                num-=i
                count+=1
            else:
                return count
        return count
