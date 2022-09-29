class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The most straight forward solution which is brute force is 
        Traverse the array and figure out the existing product of the all the elements
        now if there is zero it is going to be a problem
        so keep track of number of zeros and if there are more than one zero then all the positions will be zero
        otherwise keep track o
        """
        prod = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                prod *= i
        if zeros > 1:
            return [0]*len(nums)
        answer = []
        for i in nums:
            if zeros and i != 0:
                answer.append(0)
            elif i == 0:
                answer.append(prod)
            else:
                answer.append(int(prod/i))
                
        return answer
        