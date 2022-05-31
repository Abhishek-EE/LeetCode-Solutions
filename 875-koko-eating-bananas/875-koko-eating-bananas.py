class Solution:
    def checkCorrect(self,piles: List[int], h: int, rate: int)-> bool:
        start = 0
        for i in piles:
            if(i%rate == 0):
                h -= i//rate
            else:
                h -= i//rate + 1
            if h < 0:
                return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        So you need at least n hours to finish 
        at most you would need max value in pile hours to eat all the bananana
        at a given speed can she eat bananas check time -> O(n)
        max speed - 11 banana per hour
        min speed - 1 banana per hour
        see if mid speed is good 
        then see if 
        possible space of solutions is from 
        """
        start = 1
        end = max(piles) #O(n) (search is lgn and each search take hlgn)
        last_correct = end
        check = piles
        while end-start>=0:
            mid = start + (end-start)//2
            """
            if mid works then check between start and mid
            if mid doesn't work check between end and mid
            """
            if(self.checkCorrect(piles,h,mid)):
                # print(self.checkCorrect(piles,h,2))
                last_correct = mid
                end = mid-1
            else:
                start = mid + 1
        return last_correct
                
            
            
        